import { db, bucket, owner, reply, fail, sameOrigin, validId, jsonBody } from '../../../lib/server-data';
import { readPhoto } from '../../../lib/photo-upload';
import catalogue from '../../../content/activities.json';

type Creation = {id:string;owner_id:string;activity_id:string;object_key:string;bytes:number;state:string;created_at:string};
const activityExists = (id:unknown) => typeof id === 'string' && catalogue.some(a => a.id === id);
const publicFields = (row:Creation, userId?:string) => ({id:row.id,activityId:row.activity_id,createdAt:row.created_at,mine:row.owner_id === userId,state:row.state});

export async function GET(req:Request) {
 try {
  const url = new URL(req.url); const id = url.searchParams.get('id');
  if (id) {
   if (!validId(id)) return fail('Photo not found.',404);
   const row = await db().prepare('SELECT * FROM creations WHERE id=?').bind(id).first<Creation>();
   if (!row) return fail('Photo not found.',404);
   if (row.state !== 'public') {
    const user = await owner();
    if (row.owner_id !== user?.userId) return fail('Photo not found.',404);
   }
   const object = await bucket().get(row.object_key); if (!object) return fail('Photo not found.',404);
   return new Response(object.body,{headers:{'Content-Type':'image/jpeg','Cache-Control':'no-store','X-Content-Type-Options':'nosniff','Content-Disposition':'inline'}});
  }
  const user = await owner();
  if (url.searchParams.get('mine') === '1') {
   if (!user) return fail('Sign in to see your shared creations.',401);
   const rows = await db().prepare('SELECT * FROM creations WHERE owner_id=? ORDER BY created_at DESC,id DESC LIMIT 60').bind(user.userId).all<Creation>();
   return reply({creations:rows.results.map(r => publicFields(r,user.userId)),nextCursor:null});
  }
  const activity = url.searchParams.get('activity');
  if (!activityExists(activity)) return fail('Choose an activity.');
  let cursorClause = ''; const bindings:unknown[] = [activity];
  const cursor = url.searchParams.get('cursor');
  if (cursor) {
   const parts = cursor.split('|');
   if (parts.length !== 2 || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/.test(parts[0]) || !validId(parts[1])) return fail('Invalid gallery page.');
   cursorClause = ' AND (created_at<? OR (created_at=? AND id<?))';bindings.push(parts[0],parts[0],parts[1]);
  }
  const rows = await db().prepare("SELECT * FROM creations WHERE activity_id=? AND state='public'"+cursorClause+' ORDER BY created_at DESC,id DESC LIMIT 13').bind(...bindings).all<Creation>();
  const page = rows.results.slice(0,12), last = page.at(-1);
  return reply({creations:page.map(r => publicFields(r,user?.userId)),nextCursor:rows.results.length > 12 && last ? last.created_at+'|'+last.id : null});
 } catch { return fail('The gallery is temporarily unavailable. Please try again.',503); }
}

export async function POST(req:Request) {
 if (!sameOrigin(req)) return fail('Request origin is not allowed.',403);
 try {
  const user = await owner(); if (!user) return fail('Create an adult account before sharing a creation.',401);
  if (req.headers.get('x-share-confirmed') !== 'yes') return fail('Confirm that you want to share this project photo publicly.');
  const activity = new URL(req.url).searchParams.get('activity'); if (!activityExists(activity)) return fail('Choose an activity.');
  let bytes:Uint8Array; try { bytes = await readPhoto(req); } catch(e) { return fail((e as Error).message); }
  const count = await db().prepare('SELECT COUNT(*) AS total FROM creations WHERE owner_id=?').bind(user.userId).first<{total:number}>();
  if ((count?.total || 0) >= 60) return fail('Your gallery shelf is full. Delete a photo from My projects to make space.');
  const reserved = await db().prepare('UPDATE accounts SET photo_bytes=photo_bytes+? WHERE id=? AND photo_bytes+?<=157286400').bind(bytes.length,user.userId,bytes.length).run();
  if (!reserved.meta.changes) return fail('Your photo storage is full. Delete a photo from My projects to make space.');
  const id = crypto.randomUUID(), key = `creations/${user.userId}/${id}.jpg`, createdAt = new Date().toISOString();
  try {
   await bucket().put(key,bytes,{httpMetadata:{contentType:'image/jpeg'}});
   const inserted = await db().prepare("INSERT INTO creations(id,owner_id,activity_id,object_key,bytes,state,created_at) SELECT ?,?,?,?,?,'public',? WHERE (SELECT COUNT(*) FROM creations WHERE owner_id=?)<60 AND (SELECT COUNT(*) FROM creations WHERE owner_id=? AND activity_id=?)<6").bind(id,user.userId,activity,key,bytes.length,createdAt,user.userId,user.userId,activity).run();
   if (!inserted.meta.changes) {
    await bucket().delete(key); await db().prepare('UPDATE accounts SET photo_bytes=MAX(0,photo_bytes-?) WHERE id=?').bind(bytes.length,user.userId).run();
    return fail('You can keep up to six gallery photos for one activity. Delete one from My projects to add another.');
   }
  } catch (e) {
   await bucket().delete(key).catch(() => {});await db().prepare('UPDATE accounts SET photo_bytes=MAX(0,photo_bytes-?) WHERE id=?').bind(bytes.length,user.userId).run();throw e;
  }
  return reply({id,activityId:activity,createdAt,mine:true,state:'public'});
 } catch { return fail('Could not share your photo. Please try again.',500); }
}

export async function PATCH(req:Request) {
 if (!sameOrigin(req)) return fail('Request origin is not allowed.',403);
 try {
  const user = await owner(); if (!user) return fail('Sign in to manage this photo.',401);
  const body = await jsonBody(req);
  if (!validId(body.id)) return fail('Photo not found.',404);
  const row = await db().prepare('SELECT * FROM creations WHERE id=?').bind(body.id).first<Creation>();
  if (!row) return fail('Photo not found.',404);
  if (body.action === 'report') {
   if (row.owner_id === user.userId) return fail('You can make your own photo private instead.');
   if (row.state !== 'public') return reply({ok:true});
   if (!['privacy','inappropriate','not-a-project'].includes(body.reason)) return fail('Choose a reason.');
   // A report immediately removes a photo from the family gallery. It cannot
   // be republished through the owner controls, even by replaying a request.
   await db().batch([
    db().prepare('INSERT OR IGNORE INTO creation_reports(id,creation_id,reporter_id,reason,created_at) VALUES(?,?,?,?,?)').bind(crypto.randomUUID(),row.id,user.userId,body.reason,new Date().toISOString()),
    db().prepare("UPDATE creations SET state='hidden' WHERE id=? AND state IN ('public','private')").bind(row.id)
   ]);
   return reply({ok:true});
  }
  if (row.owner_id !== user.userId) return fail('Photo not found.',404);
  if (body.action === 'private') {
   // Retain a reported state so an owner cannot clear it by toggling privacy.
   await db().prepare("UPDATE creations SET state='private' WHERE id=? AND owner_id=? AND state='public'").bind(row.id,user.userId).run();
   return reply({ok:true});
  }
  if (body.action === 'public') {
   if (body.confirmed !== true) return fail('Confirm public sharing first.');
   if (row.state === 'hidden') return fail('This photo was removed after a report and cannot be shared again.',409);
   const result = await db().prepare("UPDATE creations SET state='public' WHERE id=? AND owner_id=? AND state='private'").bind(row.id,user.userId).run();
   if (!result.meta.changes && row.state !== 'public') return fail('The photo changed. Refresh and try again.',409);
   return reply({ok:true});
  }
  return fail('Choose a valid photo action.');
 } catch { return fail('Could not update this photo. Please try again.',500); }
}

export async function DELETE(req:Request) {
 if (!sameOrigin(req)) return fail('Request origin is not allowed.',403);
 try {
  const user = await owner(); if (!user) return fail('Sign in to delete this photo.',401);
  const id = new URL(req.url).searchParams.get('id'); if (!validId(id)) return fail('Photo not found.',404);
  const row = await db().prepare('SELECT * FROM creations WHERE id=? AND owner_id=?').bind(id,user.userId).first<Creation>();
  if (!row) return fail('Photo not found.',404);
  // Remove public access first; a failed object deletion remains private and retryable.
  await db().prepare("UPDATE creations SET state='private' WHERE id=? AND owner_id=? AND state='public'").bind(id,user.userId).run();
  await bucket().delete(row.object_key);
  await db().batch([
   db().prepare('DELETE FROM creation_reports WHERE creation_id=?').bind(id),
   db().prepare('UPDATE accounts SET photo_bytes=MAX(0,photo_bytes-?) WHERE id=? AND EXISTS (SELECT 1 FROM creations WHERE id=? AND owner_id=?)').bind(row.bytes,user.userId,id,user.userId),
   db().prepare('DELETE FROM creations WHERE id=? AND owner_id=?').bind(id,user.userId)
  ]);
  return reply({ok:true});
 } catch { return fail('Could not delete this photo. Please try again.',500); }
}
