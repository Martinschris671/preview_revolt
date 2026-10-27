import numpy as np
from PIL import Image

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.float64)
L = 0.299 * a[:, :, 0] + 0.587 * a[:, :, 1] + 0.114 * a[:, :, 2]


def hx(v):
    return "#%02X%02X%02X" % (int(round(v[0])), int(round(v[1])), int(round(v[2])))


def core(x0, x1, y0, y1, bright=True, pct=96):
    sub = a[y0:y1, x0:x1].reshape(-1, 3)
    l = 0.299 * sub[:, 0] + 0.587 * sub[:, 1] + 0.114 * sub[:, 2]
    th = np.percentile(l, pct if bright else 100 - pct)
    sel = sub[l >= th] if bright else sub[l <= th]
    return sel.mean(axis=0)


def bg(y0, y1):
    return (a[y0:y1, 0:25].reshape(-1, 3).mean(axis=0) + a[y0:y1, -25:].reshape(-1, 3).mean(axis=0)) / 2


regions = {
    "NN": (58, 100, 119, 143),
    "search text": (233, 420, 118, 146),
    "Osobni": (283, 456, 353, 378),
    "IBAN": (196, 579, 495, 521),
    "label Dodaj": (36, 160, 870, 899),
    "banner title": (169, 495, 965, 999),
    "banner desc": (169, 520, 1005, 1035),
    "aircash title": (168, 329, 1271, 1299),
    "aircash sub": (169, 347, 1311, 1341),
    "amount -10": (594, 677, 1272, 1299),
    "amount +10": (593, 677, 1408, 1437),
    "nav active": (79, 145, 1521, 1537),
    "nav inactive": (206, 276, 1521, 1541),
    "ring 4/5": (78, 120, 983, 1012),
}
for k, (x0, x1, y0, y1) in regions.items():
    c = core(x0, x1, y0, y1)
    b = bg(y0, y1)
    al = (c - b) / (255 - b)
    print("%-14s core %s  bg %s  alpha %s" % (k, hx(c), hx(b), np.round(al, 2)))

print("\nCTA text (dark):", hx(core(220, 520, 1118, 1160, bright=False)))
print("CTA white:", hx(core(80, 160, 1110, 1165)))
print("aircash red:", hx(core(70, 125, 1280, 1330)))
print("apple circle:", hx(core(70, 125, 1390, 1430)))
