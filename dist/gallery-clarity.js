// A local, feathered adjustment for the two girls in the fourth photograph.
// The original file stays unchanged; no facial features are generated.
function sharpenGalleryFaces(pixels, width, height) {
  const source = new Uint8ClampedArray(pixels);
  const faces = [{x: .335, y: .386}, {x: .724, y: .384}];
  for (const face of faces) {
    const cx = face.x * width, cy = face.y * height;
    const rx = .025 * width, ry = .047 * height;
    for (let y = Math.max(1, Math.floor(cy - ry)); y < Math.min(height - 1, cy + ry); y++) {
      for (let x = Math.max(1, Math.floor(cx - rx)); x < Math.min(width - 1, cx + rx); x++) {
        const distance = Math.hypot((x - cx) / rx, (y - cy) / ry);
        if (distance >= 1) continue;
        const weight = Math.min(1, (1 - distance) / .4);
        const index = (y * width + x) * 4;
        for (let channel = 0; channel < 3; channel++) {
          let average = 0;
          for (let dy = -1; dy <= 1; dy++) {
            for (let dx = -1; dx <= 1; dx++) {
              average += source[((y + dy) * width + x + dx) * 4 + channel];
            }
          }
          average /= 9;
          const value = source[index + channel];
          const detail = Math.max(-10, Math.min(10, (value - average) * .6));
          pixels[index + channel] = value + weight * (detail + value * .07);
        }
      }
    }
  }
  return pixels;
}

(() => {
  const photo = document.querySelector('#gallery .gallery-photo:nth-child(4) img');
  if (!photo) return;
  const enhance = () => {
    if (!photo.naturalWidth || photo.dataset.clarityApplied) return;
    photo.dataset.clarityApplied = 'true';
    try {
      const canvas = document.createElement('canvas');
      canvas.width = photo.naturalWidth;
      canvas.height = photo.naturalHeight;
      const context = canvas.getContext('2d', {willReadFrequently: true});
      context.drawImage(photo, 0, 0);
      const frame = context.getImageData(0, 0, canvas.width, canvas.height);
      sharpenGalleryFaces(frame.data, canvas.width, canvas.height);
      context.putImageData(frame, 0, 0);
      canvas.toBlob(blob => {
        if (!blob) return;
        const url = URL.createObjectURL(blob);
        photo.addEventListener('load', () => URL.revokeObjectURL(url), {once: true});
        photo.src = url;
      }, 'image/png');
    } catch (_) {
      // Keep the original photograph if processing is unavailable.
    }
  };
  if (photo.complete) enhance();
  else photo.addEventListener('load', enhance, {once: true});
})();
