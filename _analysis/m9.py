import numpy as np
from PIL import Image
from scipy import ndimage

P = r"C:\Users\HP\OneDrive\Desktop\revoult\_analysis\shot.jpg"
im = Image.open(P).convert("RGB")
a = np.asarray(im).astype(np.int16)
H, W, _ = a.shape
L = 0.299 * a[:, :, 0] + 0.587 * a[:, :, 1] + 0.114 * a[:, :, 2]


def ink(x0, x1, y0, y1, delta=55, label=""):
    sub = L[y0:y1, x0:x1]
    bg = np.percentile(sub, 30)
    m = sub > bg + delta
    m = ndimage.binary_closing(m, np.ones((2, 2)))
    m = ndimage.binary_opening(m, np.ones((2, 2)))
    ys, xs = np.where(m)
    if len(ys) == 0:
        print("%-22s none" % label)
        return
    print("%-22s x %3d..%3d (w %3d)  y %4d..%4d (h %3d)  bgL=%.0f" % (
        label, xs.min() + x0, xs.max() + x0, xs.max() - xs.min() + 1,
        ys.min() + y0, ys.max() + y0, ys.max() - ys.min() + 1, bg))


ink(50, 190, 25, 70, 55, "time 20:33")
ink(240, 500, 345, 385, 45, "Osobni EUR")
ink(300, 460, 395, 480, 45, "0 EUR")
ink(150, 600, 490, 530, 40, "IBAN")
ink(20, 160, 865, 905, 60, "Dodaj novac")
ink(200, 370, 865, 905, 60, "Prebaci")
ink(370, 540, 865, 905, 60, "Pojedinosti")
ink(560, 700, 865, 905, 60, "Vise")
ink(160, 520, 960, 1000, 50, "banner title")
ink(160, 520, 1000, 1040, 40, "banner desc l1")
ink(160, 520, 1040, 1070, 40, "banner desc l2")
ink(60, 680, 1110, 1170, 80, "CTA label")
ink(150, 400, 1265, 1300, 50, "aircash title")
ink(150, 400, 1300, 1340, 35, "aircash sub")
ink(560, 690, 1265, 1310, 45, "amount -10")
ink(60, 200, 1510, 1545, 45, "nav label Pocetna")
ink(200, 340, 1510, 1545, 25, "nav label Ulaganje")
