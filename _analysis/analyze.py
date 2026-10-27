import numpy as np
from PIL import Image
import sys

im = Image.open(r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg").convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape
print("size", W, H)

# ---- background gradient model: left edge columns 1..9 ----
bg = np.median(a[:, 1:10, :], axis=1)  # H x 3
print("\n-- gradient background (x=1..9 median) --")
for y in range(0, H, 40):
    print(f"y={y:4d}  #{int(bg[y,0]):02X}{int(bg[y,1]):02X}{int(bg[y,2]):02X}")

diff = np.abs(a - bg[:, None, :]).max(axis=2)
mask = diff > 26

try:
    from scipy import ndimage
    lab, n = ndimage.label(mask, structure=np.ones((3, 3)))
    print("\ncomponents:", n)
    objs = ndimage.find_objects(lab)
    comps = []
    for i, sl in enumerate(objs, start=1):
        if sl is None:
            continue
        ys, xs = sl
        h = ys.stop - ys.start
        w = xs.stop - xs.start
        area = int((lab[sl] == i).sum())
        if area < 150 or w < 8 or h < 8:
            continue
        sub = a[sl][lab[sl] == i]
        mean = sub.mean(axis=0).astype(int)
        comps.append((ys.start, xs.start, ys.stop, xs.stop, w, h, area, w * h, mean))
    comps.sort(key=lambda c: (c[0], c[1]))
    print(f"{'y0':>5}{'y1':>5}{'x0':>5}{'x1':>5}{'w':>5}{'h':>5}{'area':>7}{'box':>7}  mean   fill")
    for c in comps:
        y0, x0, y1, x1, w, h, area, box, mean = c
        fill = area / box
        if box > 0 and fill > 0.25:
            print(f"{y0:5d}{y1:5d}{x0:5d}{x1:5d}{w:5d}{h:5d}{area:7d}{box:7d}  #{mean[0]:02X}{mean[1]:02X}{mean[2]:02X} {fill:.2f}")
except ImportError:
    print("no scipy")
