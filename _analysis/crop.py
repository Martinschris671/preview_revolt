from PIL import Image

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
W, H = im.size
regions = {
    "r1_status_header": (0, 0, W, 230),
    "r2_balance": (0, 230, W, 560),
    "r3_dots": (0, 560, W, 740),
    "r4_actions": (0, 740, W, 975),
    "r5_card": (0, 940, W, 1290),
    "r6_list": (0, 1250, W, 1600),
    "r7_nav": (0, 1430, W, 1600),
}
for name, box in regions.items():
    c = im.crop(box)
    c = c.resize((c.width * 2, c.height * 2), Image.LANCZOS)
    c.save(rf"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\{name}.png")
    print(name, c.size)
