p = 'index.html'
s = open(p, encoding='utf-8').read()
subs = [
 # header border less green
 ('border:2px solid rgba(206,74,255,.85);', 'border:2px solid rgba(199,38,255,.88);'),
 # 5G position/size
 ('''  .fiveg{
    left:589px; top:33px;
    font-family:"RobotoNum"; font-size:26.5px; font-weight:700;
    letter-spacing:.2px;
  }''', '''  .fiveg{
    left:590px; top:36px;
    font-family:"RobotoNum"; font-size:28.5px; font-weight:700;
    letter-spacing:.3px;
  }'''),
 # battery digits
 ('''  .battery span{
    font-family:"RobotoNum"; font-weight:700; font-size:20.5px; line-height:1;
    color:#7b2bd6; letter-spacing:-.2px;
  }''', '''  .battery span{
    font-family:"RobotoNum"; font-weight:700; font-size:21px; line-height:1;
    color:#8f33dd; letter-spacing:1.4px; margin-left:1px;
  }'''),
 # nav fill a touch lighter
 ('background:rgba(10,9,38,.60);', 'background:rgba(12,10,42,.56);'),
 # ring pos + pct
 ('.ring{ position:absolute; left:30px; top:20px; width:76px; height:76px; }',
  '.ring{ position:absolute; left:31px; top:21px; width:76px; height:76px; }'),
 ('    position:absolute; left:0; top:23px; width:76px; text-align:center;',
  '    position:absolute; left:0; top:27px; width:76px; text-align:center;'),
]
for a, b in subs:
    if a not in s:
        print('MISS:', a[:60]); continue
    s = s.replace(a, b)

# signal icon: re-place
s = s.replace('  .signal{ left:539px; top:40px; width:52px; height:22px; }',
              '  .signal{ left:541px; top:40px; width:46px; height:21px; }')
s = s.replace('''  <svg class="abs signal" viewBox="0 0 52 22" fill="none">
    <rect x="0"  y="13" width="6" height="9"  rx="1.6" fill="#fff"/>
    <rect x="11" y="8"  width="6" height="14" rx="1.6" fill="#fff"/>
    <rect x="22" y="3"  width="6" height="19" rx="1.6" fill="rgba(255,255,255,.38)"/>
    <rect x="33" y="0"  width="6" height="22" rx="1.6" fill="rgba(255,255,255,.38)"/>
  </svg>''', '''  <svg class="abs signal" viewBox="0 0 46 21" fill="none">
    <rect x="0"  y="12" width="6" height="9"  rx="1.6" fill="#fff"/>
    <rect x="10" y="8"  width="6" height="13" rx="1.6" fill="#fff"/>
    <rect x="22" y="4"  width="6" height="17" rx="1.6" fill="rgba(255,255,255,.36)"/>
    <rect x="34" y="0"  width="6" height="21" rx="1.6" fill="rgba(255,255,255,.36)"/>
  </svg>''')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
