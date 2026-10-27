import numpy as np
from PIL import Image, ImageFilter

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.float32)
H, W, _ = a.shape
L = 0.299 * a[:, :, 0] + 0.587 * a[:, :, 1] + 0.114 * a[:, :, 2]
Lb = np.asarray(Image.fromarray(L.astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32)

base = np.percentile(Lb, 4, axis=1)[:, None]
ex = Lb - base

print("excess stats", ex.min(), ex.max())
Image.fromarray(np.clip(ex * 4, 0, 255).astype(np.uint8)).save(r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\excess.png")

# projection with threshold
th = 3.0
m = ex > th
ys = m.sum(axis=1)
print("\n-- row bands (excess>%.1f, count>=4) --" % th)
inr = False
for y in range(H):
    if ys[y] >= 4 and not inr:
        s = y; inr = True
    elif ys[y] < 4 and inr:
        d = m[s:y].sum(axis=0)
        xs = np.where(d > 0)[0]
        print("rows %4d..%4d h=%3d  x %3d..%3d w=%3d  maxcount=%d" % (s, y - 1, y - s, xs.min(), xs.max(), xs.max() - xs.min() + 1, ys[s:y].max()))
        inr = False
