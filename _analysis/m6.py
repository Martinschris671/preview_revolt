import numpy as np
from PIL import Image

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.float64)
H, W, _ = a.shape


def hx(v):
    return "#%02X%02X%02X" % (int(round(v[0])), int(round(v[1])), int(round(v[2])))


def patch(x0, x1, y0, y1):
    return a[y0:y1, x0:x1].reshape(-1, 3).mean(axis=0)


tests = {
    "search pill": (200, 280, 150, 165),
    "avatar": (60, 100, 148, 163),
    "analytics circle": (90, 135, 770, 785),
    "dots pill": (300, 320, 660, 680),
    "card": (650, 690, 990, 1015),
    "feed": (650, 690, 1310, 1340),
    "nav": (560, 600, 1540, 1560),
    "nav active": (200, 230, 1480, 1500),
    "CTA white": (200, 400, 1120, 1155),
    "aircash red": (75, 115, 1290, 1320),
}
for k, (x0, x1, y0, y1) in tests.items():
    p = patch(x0, x1, y0, y1)
    bgl = patch(0, 25, y0, y1)
    bgr = patch(W - 25, W, y0, y1)
    bgm = (bgl + bgr) / 2
    print("%-18s fill %s   bg %s   (L %s R %s)" % (k, hx(p), hx(bgm), hx(bgl), hx(bgr)))
    # solve alpha for white overlay
    al = (p - bgm) / (255 - bgm)
    print("                   alpha white: %.3f %.3f %.3f" % tuple(al))
    # solve alpha for black overlay
    ab = 1 - p / bgm
    print("                   alpha black: %.3f %.3f %.3f" % tuple(ab))
