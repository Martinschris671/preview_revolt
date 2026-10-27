import numpy as np
from PIL import Image
import sys

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape
print("size", W, H)

def px(x, y):
    return tuple(int(v) for v in a[y, x])

# ---- vertical background gradient: sample the far-right edge (x=W-4) where no content
print("\n-- vertical gradient samples (x=W-6) --")
for y in range(0, H, 40):
    print(y, px(W - 6, y))

print("\n-- horizontal at y=400 --")
for x in range(0, W, 40):
    print(x, px(x, 400))

# ---- row activity: distance from the row's median color (background)
med = np.median(a, axis=1)  # per-row median rgb
d = np.abs(a - med[:, None, :]).sum(axis=2)
act = (d > 26).sum(axis=1)
print("\n-- rows with content (activity>3) --")
runs = []
inrun = False
for y in range(H):
    if act[y] > 3 and not inrun:
        start = y; inrun = True
    elif act[y] <= 3 and inrun:
        runs.append((start, y - 1, int(act[start:y].max()))); inrun = False
if inrun: runs.append((start, H - 1, int(act[start:].max())))
for r in runs:
    print("rows %4d..%4d  maxact=%d" % r)
