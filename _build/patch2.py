p = 'index.html'
s = open(p, encoding='utf-8').read()
subs = [
 ('  .t1{ left:49.5px; } .t2{ left:176.5px; } .t3{ left:305px; } .t4{ left:434px; } .t5{ left:563px; }',
  '  .t1{ left:18px; } .t2{ left:145px; } .t3{ left:273.5px; } .t4{ left:402.5px; } .t5{ left:531.5px; }'),
 ('    font-family:"RobotoNum"; font-size:32.8px; font-weight:700;\n    letter-spacing:.2px;',
  '    font-family:"RobotoNum"; font-size:32.8px; font-weight:700;\n    letter-spacing:2.2px;'),
 ('    letter-spacing:.1px; line-height:1; margin-top:1px;',
  '    letter-spacing:.1px; line-height:1; margin-top:2px;'),
 ('      <div class="sub" style="left:137px; top:64.2px">Danas, 00:46</div>',
  '      <div class="sub" style="left:137px">Danas, 00:46</div>'),
 ('    font-size:28.4px; font-weight:600;', '    font-size:28.1px; font-weight:600;'),
 ('<div class="amt" style="right:32px">−10&nbsp;€</div>', '<div class="amt" style="right:32px">-10&nbsp;€</div>'),
 ('      <svg width="38" height="35" viewBox="0 0 38 35" fill="#fff">',
  '      <svg width="37" height="34" viewBox="0 0 38 35" fill="#fff">'),
 ('    <svg width="40" height="30" viewBox="0 0 40 30">',
  '    <svg width="38" height="26" viewBox="0 0 40 30">'),
]
for a, b in subs:
    if a not in s:
        print('MISS:', a[:60])
        continue
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)
print('patched')
