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


def masks(x0, x1, y0, y1, t):
    sub = L[y0:y1, x0:x1]
    m = sub > t
    m = ndimage.binary_opening(m, np.ones((2, 2)))
    lab, n = ndimage.label(m)
    out = []
    for i, sl in enumerate(ndimage.find_objects(lab), start=1):
        if sl is None:
            continue
        ys, xs = sl
        area = int((lab[sl] == i).sum())
        if area < 12:
            continue
        out.append((y0 + ys.start, y0 + ys.stop - 1, x0 + xs.start, x0 + xs.stop - 1, xs.stop - xs.start, ys.stop - ys.start, area))
    out.sort()
    return out


print("dots:")
for r in masks(300, 440, 645, 690, 170):
    print("   y %d..%d x %d..%d w%d h%d area%d" % r)

print("\nnav bright items (labels/icons):")
for r in masks(35, 705, 1450, 1575, 90):
    print("   y %d..%d x %d..%d w%d h%d area%d" % r)

print("\nstatus bar:")
for r in masks(0, 739, 0, 80, 170):
    print("   y %d..%d x %d..%d w%d h%d area%d" % r)

print("\nsecond feed row:")
for r in masks(40, 700, 1350, 1450, 80):
    print("   y %d..%d x %d..%d w%d h%d area%d" % r)

print("\ncolors:")
pts = {
    "search text": (245, 130),
    "search border": (152, 130),
    "card title": (200, 980),
    "card desc": (200, 1020),
    "iban": (250, 508),
    "label": (60, 885),
    "nav active label": (100, 1530),
    "nav inactive label": (240, 1530),
    "subtitle": (200, 1325),
    "positive": (640, 1410),
    "negative": (610, 1285),
}
for k, (x, y) in pts.items():
    print("  %-18s %s (L %.0f)" % (k, hx(a[y, x]), L[y, x]))
