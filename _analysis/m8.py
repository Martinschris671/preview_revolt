import numpy as np
from PIL import Image

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape


def hx(v):
    return "#%02X%02X%02X" % (int(v[0]), int(v[1]), int(v[2]))


def seg_row(y, x0, x1):
    print("row %d:" % y, " ".join("%d:%s" % (x, hx(a[y, x])) for x in range(x0, x1 + 1)))


def seg_col(x, y0, y1):
    print("col %d:" % x, " ".join("%d:%s" % (y, hx(a[y, x])) for y in range(y0, y1 + 1)))


print("AVATAR")
seg_row(131, 28, 48)
seg_row(131, 112, 132)
seg_col(79, 80, 96)
seg_col(79, 165, 181)
print("\nSEARCH")
seg_row(131, 143, 160)
seg_row(131, 490, 508)
seg_col(320, 80, 96)
seg_col(320, 165, 181)
print("\nBTN 1")
seg_row(131, 512, 532)
seg_row(131, 582, 602)
seg_col(565, 80, 96)
seg_col(565, 165, 181)
print("\nBTN 2")
seg_row(131, 604, 624)
seg_row(131, 688, 710)
seg_col(670, 80, 96)
seg_col(670, 165, 181)
