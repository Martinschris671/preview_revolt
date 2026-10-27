import numpy as np
from PIL import Image, ImageDraw, ImageFont

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
A = np.asarray(im).astype(np.float64)
L = 0.299 * A[:, :, 0] + 0.587 * A[:, :, 1] + 0.114 * A[:, :, 2]

INTER = r"C:\Users\HP\OneDrive\Desktop\revoult\res\font\inter_variable.ttf"
AEONIK = r"C:\Users\HP\OneDrive\Desktop\revoult\res\font\aeonik_pro_medium.otf"
AEONIK_BLACK = r"C:\Users\HP\OneDrive\Desktop\revoult\res\font\aeonik_pro_black.otf"

S = 4  # supersample


def render(text, path, size, wght, opsz):
    f = ImageFont.truetype(path, int(round(size * S)))
    if wght:
        f.set_variation_by_axes([opsz, wght])
    img = Image.new("L", (int(size * S * len(text) * 1.2) + 200, int(size * S * 3)), 0)
    d = ImageDraw.Draw(img)
    d.text((60, int(size * S * 1.8)), text, font=f, fill=255, anchor="ls")
    return img


def score(text, crop, path, size, wght, opsz=14.0):
    x0, y0, x1, y1 = crop
    sub = L[y0:y1, x0:x1]
    bg = np.median(np.concatenate([sub[0:2].ravel(), sub[-2:].ravel(), sub[:, 0:2].ravel(), sub[:, -2:].ravel()]))
    alpha = np.clip((sub - bg) / (255 - bg), 0, 1)

    big = render(text, path, size, wght, opsz)
    small = big.resize((big.width // S, big.height // S), Image.LANCZOS)
    r = np.asarray(small).astype(np.float64) / 255.0

    # crop target ink bbox and render ink bbox
    tmask = alpha > 0.15
    ys, xs = np.where(tmask)
    if len(ys) == 0:
        return 9e9
    t = alpha[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    rmask = r > 0.15
    rys, rxs = np.where(rmask)
    rr = r[rys.min():rys.max() + 1, rxs.min():rxs.max() + 1]

    best = 9e9
    H = max(t.shape[0], rr.shape[0]) + 8
    W = max(t.shape[1], rr.shape[1]) + 8
    for dy in range(-4, 5):
        for dx in range(-4, 5):
            a = np.zeros((H, W)); b = np.zeros((H, W))
            ay, ax = 4 + max(0, (rr.shape[0] - t.shape[0]) // 2), 4 + max(0, (rr.shape[1] - t.shape[1]) // 2)
            by, bx = 4 + max(0, (t.shape[0] - rr.shape[0]) // 2), 4 + max(0, (t.shape[1] - rr.shape[1]) // 2)
            a[ay:ay + t.shape[0], ax:ax + t.shape[1]] = t
            b[by + dy:by + dy + rr.shape[0], bx + dx:bx + dx + rr.shape[1]] = rr
            e = np.mean((a - b) ** 2)
            if e < best:
                best = e
    return best


tests = [
    ("Dovršite postavljanje", (160, 958, 505, 1003)),
    ("LT31 3250 0074 9233 9748", (192, 490, 585, 524)),
    ("aircash.eu", (160, 1266, 340, 1303)),
    ("Osobni · EUR", (275, 348, 462, 382)),
]
for text, crop in tests:
    print("\n==", text)
    results = []
    for path, fam in [(INTER, "inter"), (AEONIK, "aeonik")]:
        if fam == "inter":
            for wght in [400, 500, 600, 700]:
                for size in np.arange(26, 40, 0.5):
                    s = score(text, crop, path, float(size), wght, 14.0)
                    results.append((s, fam, wght, float(size)))
        else:
            for wght in [None]:
                for size in np.arange(26, 40, 0.5):
                    s = score(text, crop, path, float(size), wght, 14.0)
                    results.append((s, fam, "med", float(size)))
    results.sort()
    for r in results[:6]:
        print("   score %.4f  %s w=%s size=%.1f" % r)
