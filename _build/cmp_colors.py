import numpy as np
from PIL import Image

A = np.asarray(Image.open(r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg").convert("RGB")).astype(float)
B = np.asarray(Image.open(r"C:\Users\HP\OneDrive\Desktop\revoult\_build\render.png").convert("RGB")).astype(float)


def hx(v):
    return "#%02X%02X%02X" % tuple(int(round(x)) for x in v)


def patch(a, x0, x1, y0, y1):
    return a[y0:y1, x0:x1].reshape(-1, 3).mean(0)


pts = [
    ("bg y100", 0, 20, 95, 105),
    ("bg y300", 0, 20, 295, 305),
    ("bg y700", 0, 20, 695, 705),
    ("bg y1000", 0, 20, 995, 1005),
    ("bg y1300", 0, 20, 1295, 1305),
    ("bg y1550", 0, 20, 1545, 1555),
    ("search fill", 420, 480, 95, 110),
    ("avatar fill", 55, 70, 150, 165),
    ("analytics fill", 530, 545, 100, 115),
    ("circle fill", 80, 100, 780, 800),
    ("dots fill", 305, 335, 640, 660),
    ("card fill", 650, 690, 1140, 1160),
    ("feed fill", 650, 690, 1300, 1320),
    ("nav fill", 560, 620, 1480, 1500),
    ("nav active", 100, 140, 1540, 1550),
    ("cta", 100, 160, 1120, 1160),
    ("ring track", 100, 120, 1028, 1034),
]
for name, x0, x1, y0, y1 in pts:
    pa = patch(A, x0, x1, y0, y1)
    pb = patch(B, x0, x1, y0, y1)
    print("%-13s src %s  ren %s  d %s" % (name, hx(pa), hx(pb), (pb - pa).astype(int)))

print("\nbg column x=8")
for y in range(0, 1600, 100):
    print(" y%4d src %s ren %s" % (y, hx(A[y, 8]), hx(B[y, 8])))
