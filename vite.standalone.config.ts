import vinext from 'vinext';
import { defineConfig } from 'vite';
import { existsSync } from 'node:fs';

export default defineConfig(async () => {
  const { cloudflare } = await import('@cloudflare/vite-plugin');
  return {
    server: { host: '0.0.0.0', allowedHosts: ['terminal.local'] },
    define: { __MOSSY_STANDALONE__: 'true' },
    plugins: [vinext(), cloudflare({
      configPath: existsSync('wrangler.standalone.json') ? 'wrangler.standalone.json' : 'deploy/wrangler.example.json',
      viteEnvironment: { name: 'rsc', childEnvironments: ['ssr'] },
      inspectorPort: false,
    })],
  };
});
