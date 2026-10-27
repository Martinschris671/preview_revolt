import numpy as np
from PIL import Image
from scipy import ndimage

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape
L = (0.299 * a[:, :, 0] + 0.587 * a[:, :, 1] + 0.114 * a[:, :, 2])


def hx(v):
    return "#%02X%02X%02X" % (int(round(v[0])), int(round(v[1])), int(round(v[2])))


def edges_col(x, y0, y1, t=3):
    print("col %d" % x)
    for y in range(y0 + 1, y1):
        d = np.abs(a[y, x] - a[y - 1, x]).max()
        if d >= t:
            print("  y=%4d %s -> %s (d%d)" % (y, hx(a[y - 1, x]), hx(a[y, x]), d))


def edges_row(y, x0, x1, t=3):
    print("row %d" % y)
    for x in range(x0 + 1, x1):
        d = np.abs(a[y, x] - a[y, x - 1]).max()
        if d >= t:
            print("  x=%4d %s -> %s (d%d)" % (x, hx(a[y, x - 1]), hx(a[y, x]), d))


edges_col(700, 1400, 1595, 4)
edges_col(360, 1560, 1598, 3)
edges_row(1500, 20, 60, 3)
edges_row(1500, 690, 730, 3)

print("\nactive pill mask:")
sub = a[1440:1600, 40:260]
# brightness diff vs nav fill
nav = np.median(a[1500:1560, 660:700].reshape(-1, 3), axis=0)
d = np.abs(sub - nav).max(axis=2)
m = d > 6
m = ndimage.binary_opening(m, np.ones((3, 3)))
lab, n = ndimage.label(m)
for i, sl in enumerate(ndimage.find_objects(lab), 1):
    if sl is None:
        continue
    ys, xs = sl
    area = int((lab[sl] == i).sum())
    if area > 500:
        print("  comp y %d..%d x %d..%d area %d" % (1440 + ys.start, 1440 + ys.stop - 1, 40 + xs.start, 40 + xs.stop - 1, area))
print("nav fill", hx(nav))

print("\nlabels refined:")
for label, x0, x1 in [("Pocetna", 60, 170), ("Ulaganje", 190, 290), ("Placanja", 330, 410), ("Kriptovalute", 440, 550), ("RevPoints", 580, 680)]:
    sub = L[1515:1548, x0:x1]
    m = sub > 110
    ys, xs = np.where(m)
    if len(ys):
        print("  %-12s x %d..%d w%d  y %d..%d h%d" % (label, xs.min() + x0, xs.max() + x0, xs.max() - xs.min() + 1, ys.min() + 1515, ys.max() + 1515, ys.max() - ys.min() + 1))
