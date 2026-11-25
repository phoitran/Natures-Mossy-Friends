CREATE TABLE `creation_reports` (
	`id` text PRIMARY KEY NOT NULL,
	`creation_id` text NOT NULL,
	`reporter_id` text NOT NULL,
	`reason` text NOT NULL,
	`created_at` text NOT NULL
);
--> statement-breakpoint
CREATE UNIQUE INDEX `creation_report_once_idx` ON `creation_reports` (`creation_id`,`reporter_id`);--> statement-breakpoint
CREATE TABLE `creations` (
	`id` text PRIMARY KEY NOT NULL,
	`owner_id` text NOT NULL,
	`activity_id` text NOT NULL,
	`object_key` text NOT NULL,
	`bytes` integer NOT NULL,
	`state` text DEFAULT 'public' NOT NULL,
	`created_at` text NOT NULL
);
--> statement-breakpoint
CREATE INDEX `creations_gallery_idx` ON `creations` (`activity_id`,`state`,`created_at`);--> statement-breakpoint
CREATE INDEX `creations_owner_idx` ON `creations` (`owner_id`);