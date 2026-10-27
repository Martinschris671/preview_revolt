p = 'index.html'
s = open(p, encoding='utf-8').read()

# R size/pos
s = s.replace('font-family:Aeonik;font-size:52px;line-height:36px;font-weight:500;color:#fff',
              'font-family:Aeonik;font-size:51px;line-height:35px;font-weight:500;color:#fff')
# btc size
s = s.replace('font-size:50px;line-height:34px', 'font-size:42px;line-height:30px')

# per-icon tweaks via inline top
s = s.replace('<svg class="ticon" width="34" height="36" viewBox="0 0 34 36" fill="none">',
              '<svg class="ticon" style="top:27px" width="34" height="36" viewBox="0 0 34 36" fill="none">')
s = s.replace('<svg class="ticon" width="39" height="38" viewBox="0 0 39 38" fill="rgba(255,255,255,.8)">',
              '<svg class="ticon" style="top:26px" width="39" height="38" viewBox="0 0 39 38" fill="rgba(255,255,255,.8)">')
s = s.replace('<div class="ticon" style="width:40px;height:38px;position:absolute;left:50%;transform:translateX(-50%);top:28px;',
              '<div class="ticon" style="width:40px;height:38px;position:absolute;left:50%;transform:translateX(-50%);top:22px;')
s = s.replace('<svg class="ticon" width="36" height="40" viewBox="0 0 36 40">',
              '<svg class="ticon" style="top:25px" width="36" height="40" viewBox="0 0 36 40">')

# blob stronger
s = s.replace('''    position:absolute; left:24px; top:8px; width:136px; height:104px;
    border-radius:52px;
    background:rgba(255,255,255,.11);
    filter:blur(6px);''', '''    position:absolute; left:22px; top:6px; width:140px; height:106px;
    border-radius:53px;
    background:rgba(255,255,255,.14);
    filter:blur(7px);''')

# 4/5 up 1
s = s.replace('position:absolute; left:0; top:27px; width:76px; text-align:center;',
              'position:absolute; left:0; top:26px; width:76px; text-align:center;')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
