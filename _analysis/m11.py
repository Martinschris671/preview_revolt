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


def bg_at(y0, y1):
    return (patch(0, 26, y0, y1) + patch(W - 26, W, y0, y1)) / 2


surfaces = {
    "search": (x0 := 420, 480, [(94, 104), (120, 130), (158, 168)]),
    "avatar": (96, 112, [(94, 104), (155, 165)]),
    "dots": (300, 340, [(636, 646), (690, 700)]),
    "card": (650, 690, [(950, 965), (1180, 1192)]),
    "feed": (650, 690, [(1270, 1285), (1400, 1415)]),
    "nav": (720, 735, [(1470, 1490), (1550, 1565)]),
}
for name, (x0, x1, ys) in surfaces.items():
    print("\n", name)
    for (y0, y1) in ys:
        p = patch(x0, x1, y0, y1)
        b = bg_at(y0, y1)
        print("  y %d-%d fill %s bg %s   diff %s" % (y0, y1, hx(p), hx(b), (p - b).round(1)))
