p = 'index.html'
s = open(p, encoding='utf-8').read()

s = s.replace('.row{ position:absolute; left:0; width:679px; height:108px; }',
              '.row{ position:absolute; left:0; width:679px; height:136px; }')
s = s.replace('.row .ico{ position:absolute; left:29px; top:0; width:80px; height:80px; border-radius:50%; }',
              '.row .ico{ position:absolute; left:30px; top:0; width:76px; height:76px; border-radius:50%; }')
s = s.replace('    position:absolute; left:137px; top:4.7px;\n    font-size:32.8px; font-weight:600;',
              '    position:absolute; left:137px; top:2.7px;\n    font-size:32.8px; font-weight:600;')
s = s.replace('    position:absolute; left:137px; top:45.2px;',
              '    position:absolute; left:137px; top:42.2px;')
s = s.replace('    position:absolute; right:32px; top:5.7px;',
              '    position:absolute; right:32px; top:3.7px;')

# row1 top 22 / row2 top 158
s = s.replace('<div class="row" style="top:21px">', '<div class="row" style="top:22px">')
s = s.replace('<div class="row" style="top:129px">', '<div class="row" style="top:158px">')
# row2 inner offsets
s = s.replace('style="left:137px; top:33.7px"', 'style="left:137px; top:4.7px"')
s = s.replace('style="right:32px; top:34.7px"', 'style="right:32px; top:4.7px"')

# icon colour tweaks
s = s.replace('.aircash{ left:59px; top:21px;', '.aircash{ left:60px; top:22px;')
s = s.replace('.apple{ left:59px; top:21px; background:#111;', '.apple{ left:60px; top:22px; background:#0d0c14;')
s = s.replace('.apple svg{ width:34px; height:40px; margin-top:-2px; }',
              '.apple svg{ width:30px; height:36px; margin-top:-4px; opacity:.93; }')

open(p, 'w', encoding='utf-8').write(s)
print('ok')
