import { readFileSync, existsSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

// Deliberately separate from the Sites publishing workflow.
const path = 'wrangler.standalone.json';
if (!existsSync(path)) throw new Error('Configure wrangler.standalone.json using docs/independent-hosting.md first.');
const config = JSON.parse(readFileSync(path, 'utf8'));
if (!config.vars?.FIREBASE_PROJECT_ID || !config.vars?.PRIVACY_CONTACT_EMAIL ||
    !config.d1_databases?.[0]?.database_id || config.d1_databases[0].database_id.startsWith('00000000-') ||
    !config.r2_buckets?.[0]?.bucket_name) throw new Error('Set the Firebase project, privacy contact, D1 database and photo bucket before deployment.');
if (config.main !== './worker/standalone.ts') throw new Error('The independent deployment must use ./worker/standalone.ts.');
if (config.vars.FIREBASE_API_KEY) throw new Error('Store FIREBASE_API_KEY using Wrangler secrets, outside the configuration file.');
function run(args) {
  const result = spawnSync(process.execPath, args, { stdio: 'inherit' });
  if (result.error) throw result.error;
  if (result.status !== 0) process.exit(result.status || 1);
}
run(['node_modules/typescript/bin/tsc', '--noEmit']);
run(['tests/auth.test.mjs']);
run(['node_modules/vite/bin/vite.js', 'build', '--config', 'vite.standalone.config.ts']);
run(['node_modules/wrangler/bin/wrangler.js', 'deploy', '--config', 'dist/server/wrangler.json']);
