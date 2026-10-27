import numpy as np
from PIL import Image

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape


def hx(v):
    return "#%02X%02X%02X" % (int(v[0]), int(v[1]), int(v[2]))


def runs(vals, tol=3, minrun=2):
    out = []
    start = 0
    cur = np.array(vals[0], dtype=np.float64)
    for i in range(1, len(vals)):
        v = np.array(vals[i], dtype=np.float64)
        if np.abs(v - cur).max() > tol:
            if i - start >= minrun:
                out.append((start, i - 1, cur.copy()))
            start = i
            cur = v
        else:
            cur = cur * 0.7 + v * 0.3
    if len(vals) - start >= minrun:
        out.append((start, len(vals) - 1, cur))
    return out


def row(y, x0=0, x1=W - 1, tol=3):
    print("\n== row y=%d ==" % y)
    for s, e, c in runs([a[y, x] for x in range(x0, x1 + 1)], tol):
        print("  x %3d..%3d (%3d)  %s" % (x0 + s, x0 + e, e - s + 1, hx(c)))


def col(x, y0=0, y1=H - 1, tol=3):
    print("\n== col x=%d ==" % x)
    for s, e, c in runs([a[y, x] for y in range(y0, y1 + 1)], tol):
        print("  y %4d..%4d (%3d)  %s" % (y0 + s, y0 + e, e - s + 1, hx(c)))


for y in [50, 130, 170, 200, 700, 830, 900, 980, 1000, 1060, 1140, 1200, 1260, 1290, 1320, 1450, 1470, 1500, 1540, 1580]:
    row(y)
for x in [20, 45, 55, 150, 369, 690, 710, 725]:
    col(x)
