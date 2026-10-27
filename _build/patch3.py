p = 'index.html'
s = open(p, encoding='utf-8').read()

# glass tint
s = s.replace('''  .glass{
    background:rgba(255,255,255,.055);
    border:2px solid rgba(255,255,255,.30);
    backdrop-filter:saturate(1.55);
    -webkit-backdrop-filter:saturate(1.55);
  }''', '''  .glass{
    background:rgba(255,255,255,.02);
    border:2px solid rgba(255,255,255,.28);
    backdrop-filter:saturate(1.1);
    -webkit-backdrop-filter:saturate(1.1);
  }''')

# nav colours
s = s.replace('''    background:rgba(14,12,44,.52);
    border:1.5px solid rgba(124,116,235,.75);
    backdrop-filter:blur(18px) saturate(1.2);
    -webkit-backdrop-filter:blur(18px) saturate(1.2);''', '''    background:rgba(10,9,38,.60);
    border:1.5px solid rgba(112,104,225,.55);
    backdrop-filter:blur(20px) saturate(1.15);
    -webkit-backdrop-filter:blur(20px) saturate(1.15);''')

# active blob
s = s.replace('''    background:rgba(255,255,255,.10);
    filter:blur(16px);''', '''    background:rgba(255,255,255,.14);
    filter:blur(14px);''')

# ring svg
old_ring = '''      <svg width="76" height="76" viewBox="0 0 76 76" fill="none">
        <defs>
          <linearGradient id="pg" x1="38" y1="4" x2="38" y2="70" gradientUnits="userSpaceOnUse">
            <stop offset="0" stop-color="#79a7ff"/>
            <stop offset="1" stop-color="#7f8ff2"/>
          </linearGradient>
        </defs>
        <circle cx="38" cy="38" r="34" stroke="rgba(255,255,255,.13)" stroke-width="7"/>
        <circle cx="38" cy="38" r="34" stroke="url(#pg)" stroke-width="7" stroke-linecap="round"
                stroke-dasharray="170.9 213.6" transform="rotate(-90 38 38)"/>
      </svg>'''
new_ring = '''      <svg width="76" height="76" viewBox="0 0 76 76" fill="none">
        <circle cx="38" cy="38" r="34.5" stroke="#6d659e" stroke-width="7" stroke-linecap="round"
                stroke-dasharray="36.1 180.7"/>
        <circle cx="38" cy="38" r="34.5" stroke="#73a2ff" stroke-width="7" stroke-linecap="round"
                stroke-dasharray="144.5 72.3" transform="rotate(120 38 38)"/>
      </svg>'''
assert old_ring in s
s = s.replace(old_ring, new_ring)

# aircash subtitle nudge
s = s.replace('  .row .sub{\n    position:absolute; left:137px; top:43.2px;', '  .row .sub{\n    position:absolute; left:137px; top:45.2px;')

# NN absolute positioning
s = s.replace('''  .avatar span{
    font-size:28.7px; font-weight:600; font-variation-settings:"wght" 600,"opsz" 14;
    letter-spacing:.1px; line-height:1; margin-top:2px;
  }''', '''  .avatar span{
    position:absolute; left:0; top:5px; width:85px; text-align:center;
    font-size:28.7px; font-weight:600; font-variation-settings:"wght" 600,"opsz" 14;
    letter-spacing:.1px; line-height:1;
  }''')

# action labels
s = s.replace('font-size:28.1px; font-weight:600;', 'font-size:27.9px; font-weight:600;')

# amount letter-spacing
s = s.replace('''  .row .amt{
    position:absolute; right:32px; top:5.7px;
    font-size:32.8px; font-weight:500; font-variation-settings:"wght" 500,"opsz" 16;
    line-height:1; color:#fff;
  }''', '''  .row .amt{
    position:absolute; right:32px; top:5.7px;
    font-size:32.8px; font-weight:500; font-variation-settings:"wght" 500,"opsz" 16;
    line-height:1; color:#fff; letter-spacing:.6px;
  }''')

open(p, 'w', encoding='utf-8').write(s)
print('patched')
