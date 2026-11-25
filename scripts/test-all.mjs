import { spawnSync } from 'node:child_process';

// Each suite creates isolated fixtures. Stop immediately if a suite fails.
const suites = ['content.test.cjs', 'discovery.test.mjs', 'routes.test.mjs',
  'auth.test.mjs', 'feedback.test.mjs', 'narration.test.mjs'];
for (const suite of suites) {
  console.log(`\nRunning ${suite}`);
  const result = spawnSync(process.execPath, [`tests/${suite}`], { stdio: 'inherit' });
  if (result.error) throw result.error;
  if (result.status !== 0) process.exit(result.status ?? 1);
}
console.log('\nAll JavaScript suites passed. Run npm run test:media separately for media checks.');
