from fontTools.ttLib import TTFont

for p in [
    r"C:\Users\HP\OneDrive\Desktop\revoult\res\font\aeonik_pro_medium.otf",
    r"C:\Users\HP\OneDrive\Desktop\revoult\res\font\aeonik_pro_black.otf",
    r"C:\Users\HP\OneDrive\Desktop\revoult\res\font\inter_variable.ttf",
]:
    f = TTFont(p)
    head = f["head"]
    os2 = f["OS/2"]
    hhea = f["hhea"]
    print(p.split("\\")[-1])
    print("  upem", head.unitsPerEm, "cap", os2.sCapHeight, "x", os2.sxHeight,
          "asc", hhea.ascent, "desc", hhea.descent, "typoAsc", os2.sTypoAscender,
          "typoDesc", os2.sTypoDescender, "lineGap", hhea.lineGap)
    if "fvar" in f:
        for a in f["fvar"].axes:
            print("  axis", a.axisTag, a.minValue, a.defaultValue, a.maxValue)
    print("  name", f["name"].getDebugName(1), "|", f["name"].getDebugName(2))
