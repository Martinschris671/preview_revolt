import numpy as np
from PIL import Image
from scipy import ndimage

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape


def hx(v):
    return "#%02X%02X%02X" % (int(round(v[0])), int(round(v[1])), int(round(v[2])))


# background from side strips
strip = np.concatenate([a[:, 0:24, :], a[:, W - 24:W, :]], axis=1)
bg = np.median(strip, axis=1)  # H,3
print("-- bg curve every 20px --")
for y in range(0, H, 20):
    print("y=%4d %s" % (y, hx(bg[y])))

print("\n-- left vs right diff --")
for y in range(0, H, 100):
    d = np.abs(a[y, 0:20].mean(0) - a[y, W - 20:W].mean(0))
    print(y, d.astype(int))

diff = np.abs(a - bg[:, None, :]).max(axis=2)
mask = diff > 22
lab, n = ndimage.label(mask, structure=np.ones((3, 3)))
print("\ncomponents:", n)
objs = ndimage.find_objects(lab)
rows = []
for i, sl in enumerate(objs, start=1):
    if sl is None:
        continue
    ys, xs = sl
    h = ys.stop - ys.start
    w = xs.stop - xs.start
    area = int((lab[sl] == i).sum())
    if area < 200 or w < 10 or h < 8:
        continue
    sub = a[sl][lab[sl] == i]
    mean = sub.mean(axis=0)
    rows.append((ys.start, xs.start, ys.stop - 1, xs.stop - 1, w, h, area, mean))
rows.sort(key=lambda r: (r[0], r[1]))
print("%5s %5s %5s %5s %4s %4s %7s %6s  %s" % ("y0", "y1", "x0", "x1", "w", "h", "area", "fill", "mean"))
for y0, x0, y1, x1, w, h, area, mean in rows:
    fill = area / (w * h)
    if fill < 0.12:
        continue
    print("%5d %5d %5d %5d %4d %4d %7d %6.2f  %s" % (y0, y1, x0, x1, w, h, area, fill, hx(mean)))
