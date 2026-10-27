import numpy as np
from PIL import Image

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape


def hx(v):
    return "#%02X%02X%02X" % (int(v[0]), int(v[1]), int(v[2]))


def edges_row(y, x0, x1, t=4):
    out = []
    for x in range(x0 + 1, x1 + 1):
        d = int(np.abs(a[y, x] - a[y, x - 1]).max())
        if d >= t:
            out.append((x, hx(a[y, x - 1]), hx(a[y, x]), d))
    print("row %d edges:" % y, out)


def edges_col(x, y0, y1, t=4):
    out = []
    for y in range(y0 + 1, y1 + 1):
        d = int(np.abs(a[y, x] - a[y - 1, x]).max())
        if d >= t:
            out.append((y, hx(a[y - 1, x]), hx(a[y, x]), d))
    print("col %d edges:" % x, out)


print("card/feed horizontal edges")
for y in [1000, 1060, 1200, 1250, 1260, 1400, 1430]:
    edges_row(y, 15, 70, 3)
    edges_row(y, 670, 725, 3)

print("\ncard/feed vertical edges at x=690")
edges_col(690, 930, 1300, 3)
print("\nfeed vertical edges at x=50")
edges_col(50, 1230, 1460, 3)

print("\nnav")
for y in [1440, 1450, 1460, 1555, 1565, 1580]:
    edges_row(y, 15, 80, 3)
    edges_row(y, 660, 730, 3)
for x in [369, 100]:
    edges_col(x, 1380, 1600, 3)
