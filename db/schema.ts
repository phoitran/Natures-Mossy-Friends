import { sqliteTable, text, integer, index, uniqueIndex } from 'drizzle-orm/sqlite-core';
export const accounts = sqliteTable('accounts', {
 id:text('id').primaryKey(), email:text('email').notNull(), name:text('name').notNull().default(''),
 policyVersion:text('policy_version').notNull(), createdAt:text('created_at').notNull(), photoBytes:integer('photo_bytes').notNull().default(0)
});
export const projects = sqliteTable('projects', {
 id:text('id').primaryKey(), ownerId:text('owner_id').notNull(), activityId:text('activity_id').notNull(),
 variant:text('variant').notNull(), step:integer('step').notNull().default(0), status:text('status').notNull(),
 updatedAt:text('updated_at').notNull(), revision:integer('revision').notNull().default(1)
});
export const favourites = sqliteTable('favourites', {
 id:text('id').primaryKey(), ownerId:text('owner_id').notNull(), activityId:text('activity_id').notNull()
});
export const photos = sqliteTable('photos', {
 id:text('id').primaryKey(), ownerId:text('owner_id').notNull(), projectId:text('project_id').notNull(),
 objectKey:text('object_key').notNull(), bytes:integer('bytes').notNull(), mime:text('mime').notNull(), createdAt:text('created_at').notNull()
});
export const creations = sqliteTable('creations', {
 id:text('id').primaryKey(), ownerId:text('owner_id').notNull(), activityId:text('activity_id').notNull(),
 objectKey:text('object_key').notNull(), bytes:integer('bytes').notNull(),
 state:text('state').notNull().default('public'), createdAt:text('created_at').notNull()
}, table => [index('creations_gallery_idx').on(table.activityId,table.state,table.createdAt),index('creations_owner_idx').on(table.ownerId)]);
export const creationReports = sqliteTable('creation_reports', {
 id:text('id').primaryKey(), creationId:text('creation_id').notNull(), reporterId:text('reporter_id').notNull(),
 reason:text('reason').notNull(), createdAt:text('created_at').notNull()
}, table => [uniqueIndex('creation_report_once_idx').on(table.creationId,table.reporterId)]);

export const authAttempts = sqliteTable('auth_attempts', {
 id:text('id').primaryKey(), attempts:integer('attempts').notNull(), expiresAt:integer('expires_at').notNull()
}, table => [index('auth_attempts_expiry').on(table.expiresAt)]);
