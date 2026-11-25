export function jpegInfo(a: Uint8Array) {
 if (a[0] !== 255 || a[1] !== 216 || a.at(-2) !== 255 || a.at(-1) !== 217) return null;
 let width = 0, height = 0;
 for (let p = 2; p + 4 < a.length;) {
  if (a[p] !== 255) return null;
  const marker = a[p + 1];
  if (marker === 0xda || marker === 0xd9) break;
  const len = (a[p + 2] << 8) | a[p + 3];
  if (len < 2 || p + 2 + len > a.length) return null;
  if ([0xe1, 0xed, 0xfe].includes(marker)) return null;
  if ([0xc0, 0xc1, 0xc2].includes(marker)) {
   if (len < 8) return null;
   height = (a[p + 5] << 8) | a[p + 6]; width = (a[p + 7] << 8) | a[p + 8];
  }
  p += len + 2;
 }
 return width && height && width <= 2048 && height <= 2048 ? { width, height } : null;
}

export async function readPhoto(req: Request) {
 if (req.headers.get('content-type') !== 'image/jpeg') throw new Error('Choose a JPG, PNG or WebP photo.');
 const limit = 10 * 1024 * 1024;
 if (Number(req.headers.get('content-length') || 0) > limit) throw new Error('Choose a photo under 10 MB.');
 const reader = req.body?.getReader();
 if (!reader) throw new Error('Choose a photo.');
 const chunks: Uint8Array[] = []; let total = 0;
 while (true) {
  const { done, value } = await reader.read(); if (done) break;
  total += value.byteLength;
  if (total > limit) { await reader.cancel(); throw new Error('Choose a photo under 10 MB.'); }
  chunks.push(value);
 }
 const bytes = new Uint8Array(total); let offset = 0;
 for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
 if (!jpegInfo(bytes)) throw new Error('This photo could not be processed. Please choose it again.');
 return bytes;
}
