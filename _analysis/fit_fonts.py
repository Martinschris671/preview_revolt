from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
import os

FONTS = {
    "aeonik-medium": r"C:\Users\HP\OneDrive\Desktop\revoult\res\font\aeonik_pro_medium.otf",
    "aeonik-black": r"C:\Users\HP\OneDrive\Desktop\revoult\res\font\aeonik_pro_black.otf",
    "inter-var": r"C:\Users\HP\OneDrive\Desktop\revoult\res\font\inter_variable.ttf",
}
STRINGS = {
    "0": (55, 66),
    "Osobni · EUR": (173, 22),
    "Dodaj novac": (124, 26),
    "Prebaci": (96, 21),
    "Pojedinosti": (142, 26),
    "Dovršite postavljanje": (326, 31),
    "LT31 3250 0074 9233 9748": (383, 23),
    "aircash.eu": (161, 25),
    "-10 €": (80, 24),
}
SZ = 220


def ink_bbox(font, text):
    img = Image.new("L", (3000, 600), 255)
    d = ImageDraw.Draw(img)
    d.text((100, 150), text, font=font, fill=0)
    bbox = img.getbbox()
    return bbox


def metrics(font):
    return TTFont(font)["head"].unitsPerEm


for name, path in FONTS.items():
    print("\n===", name)
    for wght in ([400, 500, 600, 700] if name == "inter-var" else [None]):
        f = ImageFont.truetype(path, SZ)
        if wght:
            try:
                f.set_variation_by_axes([14.0, wght])
            except Exception as e:
                print("var err", e)
        for text, (mw, mh) in STRINGS.items():
            bb = ink_bbox(f, text)
            w = bb[2] - bb[0]
            h = bb[3] - bb[1]
            if h == 0:
                continue
            # width if scaled to measured height
            w_at = w * mh / h
            print("  %-24s ratio %.3f  w@h=%3d  meas %3dx%2d  err %+5.1f%%" % (
                text.encode("ascii", "replace").decode(), w / h, round(w_at), mw, mh, (w_at - mw) / mw * 100))
