export async function preparePhoto(file: File): Promise<Blob> {
 if (file.size > 10 * 1024 * 1024) throw new Error('Choose a photo under 10 MB.');
 if (!['image/jpeg', 'image/png', 'image/webp'].includes(file.type)) throw new Error('Choose a JPG, PNG or WebP photo. For HEIC, export a JPEG first.');
 const bitmap = await createImageBitmap(file);
 if (bitmap.width * bitmap.height > 25_000_000) { bitmap.close(); throw new Error('Choose a photo smaller than 25 megapixels.'); }
 const scale = Math.min(1, 2048 / Math.max(bitmap.width, bitmap.height));
 const canvas = document.createElement('canvas');
 canvas.width = Math.max(1, Math.round(bitmap.width * scale)); canvas.height = Math.max(1, Math.round(bitmap.height * scale));
 const ctx = canvas.getContext('2d');
 if (!ctx) { bitmap.close(); throw new Error('Photo processing is unavailable in this browser.'); }
 ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, canvas.width, canvas.height);
 ctx.drawImage(bitmap, 0, 0, canvas.width, canvas.height); bitmap.close();
 return new Promise((resolve, reject) => canvas.toBlob(b => b ? resolve(b) : reject(new Error('Could not process the photo.')), 'image/jpeg', .88));
}
