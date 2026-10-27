import numpy as np
from PIL import Image

SRC = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
REN = r"C:\Users\HP\OneDrive\Desktop\revoult\_build\render.png"

A = np.asarray(Image.open(SRC).convert("RGB")).astype(np.float64)
B = np.asarray(Image.open(REN).convert("RGB")).astype(np.float64)
LA = 0.299 * A[:, :, 0] + 0.587 * A[:, :, 1] + 0.114 * A[:, :, 2]
LB = 0.299 * B[:, :, 0] + 0.587 * B[:, :, 1] + 0.114 * B[:, :, 2]

items = [
    ("clock", 50, 200, 25, 75),
    ("NN", 45, 115, 110, 150),
    ("search txt", 220, 440, 110, 155),
    ("Osobni", 250, 490, 345, 385),
    ("zero", 300, 380, 395, 480),
    ("euro", 380, 430, 425, 480),
    ("IBAN", 190, 600, 488, 528),
    ("labels", 20, 700, 862, 905),
    ("banner t", 150, 520, 955, 1005),
    ("desc1", 150, 530, 1000, 1038),
    ("desc2", 150, 480, 1038, 1072),
    ("CTA label", 100, 640, 1105, 1170),
    ("aircash t", 150, 350, 1262, 1302),
    ("aircash s", 150, 360, 1305, 1342),
    ("amt1", 580, 690, 1265, 1302),
    ("navlabels", 60, 690, 1515, 1545),
]
for name, x0, x1, y0, y1 in items:
    res = []
    for L in (LA, LB):
        sub = L[y0:y1, x0:x1]
        m = sub > max(120, np.percentile(sub, 80))
        ys, xs = np.where(m)
        if len(ys) == 0:
            res.append(None)
        else:
            res.append((x0 + xs.min(), x0 + xs.max(), y0 + ys.min(), y0 + ys.max()))
    if all(res):
        dx0 = res[1][0] - res[0][0]
        dx1 = res[1][1] - res[0][1]
        dy0 = res[1][2] - res[0][2]
        dy1 = res[1][3] - res[0][3]
        print("%-11s src x%3d-%3d y%3d-%3d | ren x%3d-%3d y%3d-%3d | d %+d/%+d %+d/%+d  w %d/%d" % (
            name, *res[0], *res[1], dx0, dx1, dy0, dy1,
            res[0][1] - res[0][0] + 1, res[1][1] - res[1][0] + 1))
    else:
        print(name, res)
