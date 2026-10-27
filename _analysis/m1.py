import numpy as np
from PIL import Image

p = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(p).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape
print("size", W, H)


def hx(v):
    return "#%02X%02X%02X" % (int(v[0]), int(v[1]), int(v[2]))


print("\n-- vertical bg samples (x=4, center 369, right W-5) --")
for y in range(0, H, 25):
    print("y=%4d L=%s C=%s R=%s" % (y, hx(a[y, 4]), hx(a[y, 369]), hx(a[y, W - 5])))
