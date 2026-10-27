import numpy as np
from PIL import Image, ImageChops, ImageDraw

SRC = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
REN = r"C:\Users\HP\OneDrive\Desktop\revoult\_build\render.png"

a = Image.open(SRC).convert("RGB")
b = Image.open(REN).convert("RGB")
if b.size != a.size:
    print("SIZE MISMATCH", a.size, b.size)
    b = b.resize(a.size)

A = np.asarray(a).astype(np.int16)
B = np.asarray(b).astype(np.int16)
d = np.abs(A - B).max(axis=2)
print("mean abs diff %.2f  p95 %d  p99 %d  max %d" % (np.abs(A - B).mean(), np.percentile(d, 95), np.percentile(d, 99), d.max()))
print("pixels >24: %.2f%%" % ((d > 24).mean() * 100))

# heatmap
heat = np.zeros((*d.shape, 3), np.uint8)
heat[..., 0] = np.clip(d * 3, 0, 255)
heat[..., 1] = np.clip((d - 16) * 2, 0, 255)
Image.fromarray(heat).save(r"C:\Users\HP\OneDrive\Desktop\revoult\_build\diff.png")

# side by side + overlay
w, h = a.size
out = Image.new("RGB", (w * 3 + 20, h), (10, 10, 10))
out.paste(a, (0, 0))
out.paste(b, (w + 10, 0))
blend = Image.blend(a, b, 0.5)
out.paste(blend, (w * 2 + 20, 0))
out.save(r"C:\Users\HP\OneDrive\Desktop\revoult\_build\compare.png")
print("saved diff.png / compare.png")
