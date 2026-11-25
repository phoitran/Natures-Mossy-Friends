CREATE TABLE `auth_attempts` (
	`id` text PRIMARY KEY NOT NULL,
	`attempts` integer NOT NULL,
	`expires_at` integer NOT NULL
);
--> statement-breakpoint
CREATE INDEX `auth_attempts_expiry` ON `auth_attempts` (`expires_at`);