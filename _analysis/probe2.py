import numpy as np
from PIL import Image

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape

def rle(vals, tol=12, minrun=3):
    """vals: list of rgb tuples. returns [(start,end,color)]"""
    out = []
    start = 0
    cur = np.array(vals[0])
    for i in range(1, len(vals)):
        v = np.array(vals[i])
        if np.abs(v - cur).max() > tol:
            if i - start >= minrun:
                out.append((start, i - 1, tuple(int(x) for x in cur)))
            start = i
            cur = v
        else:
            cur = (cur * 3 + v) // 4
    if len(vals) - start >= minrun:
        out.append((start, len(vals) - 1, tuple(int(x) for x in cur)))
    return out

def row(y, tol=12):
    print("\n== row y=%d ==" % y)
    for s, e, c in rle([tuple(int(x) for x in a[y, x]) for x in range(W)], tol):
        print("  x %3d..%3d (%3d)  rgb%s" % (s, e, e - s + 1, c))

def col(x, tol=12):
    print("\n== col x=%d ==" % x)
    for s, e, c in rle([tuple(int(v) for v in a[y, x]) for y in range(H)], tol):
        print("  y %4d..%4d (%3d)  rgb%s" % (s, e, e - s + 1, c))

for y in [50, 70, 100, 120, 140, 160, 175, 300, 366, 440, 510, 560, 668, 690, 800, 885, 950, 1080, 1140, 1180, 1250, 1300, 1420, 1520, 1550, 1575]:
    row(y)
