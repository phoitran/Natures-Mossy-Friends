CREATE TABLE `accounts` (
	`id` text PRIMARY KEY NOT NULL,
	`email` text NOT NULL,
	`name` text DEFAULT '' NOT NULL,
	`policy_version` text NOT NULL,
	`created_at` text NOT NULL,
	`photo_bytes` integer DEFAULT 0 NOT NULL
);
--> statement-breakpoint
CREATE TABLE `favourites` (
	`id` text PRIMARY KEY NOT NULL,
	`owner_id` text NOT NULL,
	`activity_id` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `photos` (
	`id` text PRIMARY KEY NOT NULL,
	`owner_id` text NOT NULL,
	`project_id` text NOT NULL,
	`object_key` text NOT NULL,
	`bytes` integer NOT NULL,
	`mime` text NOT NULL,
	`created_at` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `projects` (
	`id` text PRIMARY KEY NOT NULL,
	`owner_id` text NOT NULL,
	`activity_id` text NOT NULL,
	`variant` text NOT NULL,
	`step` integer DEFAULT 0 NOT NULL,
	`status` text NOT NULL,
	`updated_at` text NOT NULL,
	`revision` integer DEFAULT 1 NOT NULL
);
