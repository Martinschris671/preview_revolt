import numpy as np
from PIL import Image

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape


def hx(v):
    return "#%02X%02X%02X" % (int(v[0]), int(v[1]), int(v[2]))


def scan_col(x, y0, y1, step=2):
    print("\ncol x=%d" % x)
    prev = None
    for y in range(y0, y1, step):
        c = a[y, x]
        s = "%4d %s" % (y, hx(c))
        if prev is not None:
            d = int(np.abs(c - prev).max())
            if d >= 3:
                s += "  d=%d" % d
        prev = c
        print(s)


def scan_row(y, x0, x1, step=2):
    print("\nrow y=%d" % y)
    prev = None
    for x in range(x0, x1, step):
        c = a[y, x]
        s = "%4d %s" % (x, hx(c))
        if prev is not None:
            d = int(np.abs(c - prev).max())
            if d >= 3:
                s += "  d=%d" % d
        prev = c
        print(s)


scan_col(688, 940, 1460, 4)
scan_col(45, 940, 1460, 4)
scan_col(690, 1390, 1600, 4)
scan_row(1290, 0, 40, 2)
scan_row(1290, 660, 739, 2)
