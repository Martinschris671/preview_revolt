import numpy as np
from PIL import Image

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape


def hx(v):
    return "#%02X%02X%02X" % (int(v[0]), int(v[1]), int(v[2]))


def col(x, y0, y1, step=4):
    print("\ncol x=%d" % x)
    for y in range(y0, y1, step):
        print("  y=%4d %s" % (y, hx(a[y, x])))


def row(y, x0, x1, step=4):
    print("\nrow y=%d" % y)
    for x in range(x0, x1, step):
        print("  x=%4d %s" % (x, hx(a[y, x])))


col(79, 80, 240, 3)
row(160, 20, 730, 4)
col(320, 80, 230, 3)
