from PIL import Image, ImageDraw, ImageFont
import numpy as np

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")

# (string, crop box, cap-height-based size in px at 739 scale)
items = [
    ("Osobni · EUR", (275, 348, 465, 382), 30.2, "400"),
    ("Dovršite postavljanje", (160, 960, 505, 1002), 33.0, "600"),
    ("aircash.eu", (160, 1266, 340, 1302), 32.9, "600"),
    ("LT31 3250 0074 9233 9748", (190, 490, 590, 526), 28.7, "400"),
    ("Dodaj novac", (30, 866, 170, 903), 28.7, "600"),
]
fonts = {
    "inter": r"C:\Users\HP\OneDrive\Desktop\revoult\res\font\inter_variable.ttf",
    "aeonik": r"C:\Users\HP\OneDrive\Desktop\revoult\res\font\aeonik_pro_medium.otf",
}
SCALE = 3
rows = []
for text, box, size, wt in items:
    crop = im.crop(box)
    cw, ch = crop.size
    tiles = [crop.resize((cw * SCALE, ch * SCALE), Image.LANCZOS)]
    for fname, fp in fonts.items():
        f = ImageFont.truetype(fp, int(round(size * SCALE)))
        if fname == "inter":
            f.set_variation_by_axes([14.0, float(wt)])
        img = Image.new("RGB", (cw * SCALE, ch * SCALE), (60, 50, 120))
        d = ImageDraw.Draw(img)
        d.text((6, ch * SCALE - 8), text, font=f, fill=(255, 255, 255), anchor="ls")
        tiles.append(img)
    wsum = sum(t.width for t in tiles) + 10 * (len(tiles) - 1)
    row = Image.new("RGB", (wsum, ch * SCALE), (20, 20, 20))
    x = 0
    for t in tiles:
        row.paste(t, (x, 0))
        x += t.width + 10
    rows.append(row)

W = max(r.width for r in rows)
H = sum(r.height for r in rows) + 10 * (len(rows) - 1)
out = Image.new("RGB", (W, H), (20, 20, 20))
y = 0
for r in rows:
    out.paste(r, (0, y))
    y += r.height + 10
out.save(r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\font_compare.png")
print(out.size)
