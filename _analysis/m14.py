import numpy as np
from PIL import Image

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape
B = a[:, :, 2].astype(np.int16)

m = (B < 112) & (np.arange(H)[:, None] > 1400)
ys, xs = np.where(m)
print("nav bbox y %d..%d (%d)  x %d..%d (%d)" % (ys.min(), ys.max(), ys.max() - ys.min() + 1, xs.min(), xs.max(), xs.max() - xs.min() + 1))
for y in range(1400, 1600, 5):
    row = np.where(m[y])[0]
    if len(row):
        print("  y=%4d  x %3d..%3d  w %3d" % (y, row.min(), row.max(), row.max() - row.min() + 1))
    else:
        print("  y=%4d  -" % y)

print("\nactive pill (lighter inside nav):")
# inside nav region, pixels notably lighter than nav fill
sub = a[1440:1600, 40:260]
navc = np.array([35, 32, 85])
d = np.abs(sub - navc).max(axis=2)
mm = (d > 8) & (d < 60)
from scipy import ndimage
lab, n = ndimage.label(ndimage.binary_opening(mm, np.ones((3, 3))))
for i, sl in enumerate(ndimage.find_objects(lab), 1):
    if sl is None:
        continue
    y0, y1 = sl[0].start + 1440, sl[0].stop - 1 + 1440
    x0, x1 = sl[1].start + 40, sl[1].stop - 1 + 40
    area = int((lab[sl] == i).sum())
    if area > 2000:
        print("  y %d..%d x %d..%d area %d" % (y0, y1, x0, x1, area))
