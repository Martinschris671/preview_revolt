p = 'index.html'
s = open(p, encoding='utf-8').read()
subs = [
 ('  .avatar span{\n    font-size:28.7px; font-weight:600; font-variation-settings:"wght" 600,"opsz" 14;\n    letter-spacing:.1px; line-height:1; margin-top:-2px;\n  }',
  '  .avatar span{\n    font-size:28.7px; font-weight:600; font-variation-settings:"wght" 600,"opsz" 14;\n    letter-spacing:.1px; line-height:1; margin-top:1px;\n  }'),
 ('    position:absolute; left:82px; top:30.6px;', '    position:absolute; left:78px; top:27.6px;'),
 ('    left:0; top:351.4px; width:739px; text-align:center;\n    font-size:28.5px; font-weight:500; font-variation-settings:"wght" 500,"opsz" 14;\n    line-height:1; color:rgba(255,255,255,.95); letter-spacing:.1px;',
  '    left:0; top:353.4px; width:739px; text-align:center;\n    font-size:28.5px; font-weight:500; font-variation-settings:"wght" 500,"opsz" 14;\n    line-height:1; color:rgba(255,255,255,.95); letter-spacing:-.05px;'),
 ('    position:absolute; left:385px; top:430px;', '    position:absolute; left:388px; top:433px;'),
 ('    margin-top:0; position:absolute; top:106.2px; left:-40px; width:171px;\n    font-size:28.7px; font-weight:600;',
  '    margin-top:0; position:absolute; top:109.2px; left:-40px; width:171px;\n    font-size:28.4px; font-weight:600;'),
 ('    position:absolute; left:138px; top:23.7px;\n    font-size:32.8px; font-weight:700; font-variation-settings:"wght" 700,"opsz" 16;\n    line-height:1; letter-spacing:-.1px; color:#fff;',
  '    position:absolute; left:138px; top:24.7px;\n    font-size:32.8px; font-weight:700; font-variation-settings:"wght" 700,"opsz" 16;\n    line-height:1; letter-spacing:-.35px; color:#fff;'),
 ('    position:absolute; left:138px; top:61.6px; width:470px;', '    position:absolute; left:138px; top:62.6px; width:470px;'),
 ('    position:absolute; left:0; top:21.7px; width:619px; text-align:center;\n    font-size:32.8px; font-weight:700; font-variation-settings:"wght" 700,"opsz" 16;\n    color:#0a0a0f; letter-spacing:-.15px; line-height:1;',
  '    position:absolute; left:0; top:23.2px; width:619px; text-align:center;\n    font-size:28.7px; font-weight:700; font-variation-settings:"wght" 700,"opsz" 14;\n    color:#0a0a0f; letter-spacing:-.15px; line-height:1;'),
]
for a, b in subs:
    if a not in s:
        print('MISS:', a[:70])
        continue
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)
print('patched')
