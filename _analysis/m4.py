import numpy as np
from PIL import Image
from scipy import ndimage

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape


def hx(v):
    return "#%02X%02X%02X" % (int(round(v[0])), int(round(v[1])), int(round(v[2])))


strip = np.concatenate([a[:, 0:20, :], a[:, W - 20:W, :]], axis=1)
bg = np.median(strip, axis=1)


def bbox(x0, x1, y0, y1, t=15, label=""):
    sub = a[y0:y1, x0:x1]
    bgs = bg[y0:y1]
    d = np.abs(sub - bgs[:, None, :]).max(axis=2)
    m = d > t
    m = ndimage.binary_opening(m, np.ones((2, 2)))
    lab, n = ndimage.label(m)
    sizes = ndimage.sum(m, lab, range(1, n + 1))
    keep = np.isin(lab, np.where(sizes >= 30)[0] + 1)
    ys, xs = np.where(keep)
    if len(ys) == 0:
        print("%-22s none" % label)
        return
    Y0, Y1, X0, X1 = ys.min() + y0, ys.max() + y0, xs.min() + x0, xs.max() + x0
    print("%-22s x %3d..%3d (w %3d)  y %4d..%4d (h %3d)  n=%d" % (label, X0, X1, X1 - X0 + 1, Y0, Y1, Y1 - Y0 + 1, keep.sum()))


print("--- text/objects ---")
bbox(55, 190, 20, 80, 30, "time")
bbox(520, 710, 20, 80, 20, "status icons")
bbox(20, 145, 95, 220, 8, "avatar")
bbox(150, 500, 95, 220, 8, "search pill")
bbox(505, 600, 95, 220, 8, "btn analytics")
bbox(600, 705, 95, 220, 8, "btn cards")
bbox(240, 500, 340, 395, 25, "Osobni EUR")
bbox(300, 460, 390, 500, 40, "0 EUR")
bbox(150, 590, 490, 540, 25, "IBAN row")
bbox(270, 470, 615, 720, 8, "dots pill")
bbox(0, 739, 860, 905, 30, "action labels")
bbox(30, 710, 955, 1290, 5, "setup card")
bbox(30, 710, 1240, 1440, 5, "feed card")

print("\n--- label bboxes ---")
for x0, x1, name in [(20, 150, "Dodaj novac"), (160, 320, "Prebaci"), (330, 500, "Pojedinosti"), (500, 700, "Vise")]:
    bbox(x0, x1, 860, 905, 30, name)

print("\n--- colors ---")
pts = {
    "bg y=0": (5, 0), "bg y=100": (5, 100), "bg y=300": (5, 300), "bg y=500": (5, 500),
    "bg y=700": (5, 700), "bg y=900": (5, 900), "bg y=1000": (5, 1000),
    "bg y=1300": (5, 1300), "bg y=1500": (5, 1500),
    "avatar fill": (80, 130), "search fill": (400, 170), "action circle fill": (115, 806),
    "dots fill": (300, 668), "card fill": (350, 950), "CTA white": (300, 1130),
    "nav fill": (700, 1500), "nav border": (370, 1402),
    "feed fill": (400, 1300),
}
for k, (x, y) in pts.items():
    print("%-18s (%3d,%4d) %s  bg %s" % (k, x, y, hx(a[y, x]), hx(bg[y])))
