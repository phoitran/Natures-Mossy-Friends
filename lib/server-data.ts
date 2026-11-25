import { env } from 'cloudflare:workers';
import { getChatGPTUser } from '../app/chatgpt-auth';
import { standaloneAuth } from './auth-mode';
import { firebaseSession } from './firebase-auth';
export const POLICY_VERSION='2026-11-22-public-sharing';
export const fail=(error:string,status=400)=>Response.json({error},{status,headers:{'Cache-Control':'no-store'}});
export const reply=(data:unknown)=>Response.json(data,{headers:{'Cache-Control':'no-store'}});
export function db(){if(!env.DB)throw new Error('Account storage is temporarily unavailable.');return env.DB;}
export function bucket(){if(!env.BUCKET)throw new Error('Photo storage is temporarily unavailable.');return env.BUCKET;}
export function sameOrigin(req:Request){const origin=req.headers.get('origin');return !!origin && origin===new URL(req.url).origin;}
export async function identity(){if(!standaloneAuth)return getChatGPTUser();const session=await firebaseSession();return session?.emailVerified?session:null;}
export async function owner(){const user=await identity(); if(!user)return null; const account=await db().prepare('SELECT id, email, name FROM accounts WHERE id=?').bind(user.userId).first(); return account ? user : null;}
export async function jsonBody(req:Request){if(Number(req.headers.get('content-length')||0)>64000)throw new Error('Request is too large.');const reader=req.body?.getReader();if(!reader)throw new Error('Missing request.');const chunks:Uint8Array[]=[];let size=0;while(true){const {done,value}=await reader.read();if(done)break;size+=value.length;if(size>64000){await reader.cancel();throw new Error('Request is too large.');}chunks.push(value);}const buffer=new Uint8Array(size);let offset=0;for(const chunk of chunks){buffer.set(chunk,offset);offset+=chunk.length;}return JSON.parse(new TextDecoder().decode(buffer));}
export const validId=(id:unknown)=>typeof id==='string'&&/^[a-zA-Z0-9_-]{1,80}$/.test(id);
export async function removePhotos(ownerId:string, projectId?:string){
 const q=projectId?'SELECT * FROM photos WHERE owner_id=? AND project_id=?':'SELECT * FROM photos WHERE owner_id=?';
 const rows=await db().prepare(q).bind(...(projectId?[ownerId,projectId]:[ownerId])).all<{id:string,object_key:string,bytes:number}>();
 for(const photo of rows.results){await bucket().delete(photo.object_key);await db().batch([db().prepare('DELETE FROM photos WHERE id=? AND owner_id=?').bind(photo.id,ownerId),db().prepare('UPDATE accounts SET photo_bytes=MAX(0,photo_bytes-?) WHERE id=?').bind(photo.bytes,ownerId)]);}
}
export async function removeCreations(ownerId:string){
 const rows=await db().prepare('SELECT id,object_key,bytes FROM creations WHERE owner_id=?').bind(ownerId).all<{id:string,object_key:string,bytes:number}>();
 await db().prepare("UPDATE creations SET state='private' WHERE owner_id=? AND state='public'").bind(ownerId).run();
 for(const row of rows.results){
  await bucket().delete(row.object_key);
  await db().batch([
   db().prepare('DELETE FROM creation_reports WHERE creation_id=?').bind(row.id),
   db().prepare('UPDATE accounts SET photo_bytes=MAX(0,photo_bytes-?) WHERE id=? AND EXISTS (SELECT 1 FROM creations WHERE id=? AND owner_id=?)').bind(row.bytes,ownerId,row.id,ownerId),
   db().prepare('DELETE FROM creations WHERE id=? AND owner_id=?').bind(row.id,ownerId)
  ]);
 }
 await db().prepare('DELETE FROM creation_reports WHERE reporter_id=?').bind(ownerId).run();
}
