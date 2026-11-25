// Render authored SVG scenes after their text has been outlined by the Python producer.
import { readFileSync, writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { initWasm, Resvg } from '@resvg/resvg-wasm';
const require = createRequire(import.meta.url);
await initWasm(readFileSync(require.resolve('@resvg/resvg-wasm/index_bg.wasm')));
for (const file of process.argv.slice(2)) {
  const svg = new Resvg(readFileSync(file), { fitTo: {mode:'width', value:760} });
  const image = svg.render();
  writeFileSync(file.replace(/\.svg$/,'.png'),image.asPng());
  image.free(); svg.free();
}
