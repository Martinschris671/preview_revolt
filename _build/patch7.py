p = 'index.html'
s = open(p, encoding='utf-8').read()

# bank icon (actions) - two columns
old = '''      <svg width="37" height="37" viewBox="0 0 37 37" fill="#fff">
        <path d="M18.5 1 36 11v3H1v-3z"/>
        <rect x="4" y="17" width="7" height="12" rx="1"/>
        <rect x="15" y="17" width="7" height="12" rx="1"/>
        <rect x="26" y="17" width="7" height="12" rx="1"/>
        <rect x="1" y="32" width="35" height="3.6" rx="1.4"/>
      </svg>'''
new = '''      <svg width="38" height="36" viewBox="0 0 38 36" fill="#fff">
        <path d="M19 0 38 10v3.6H0V10z"/>
        <path d="M19 3.4 32.4 10H5.6z" fill="none" stroke="#fff" stroke-width="1.4" opacity=".55"/>
        <rect x="5.4" y="16.4" width="7.6" height="14.2" rx="1.4"/>
        <rect x="25" y="16.4" width="7.6" height="14.2" rx="1.4"/>
        <rect x="0.6" y="32" width="36.8" height="4" rx="1.6"/>
      </svg>'''
assert old in s
s = s.replace(old, new)

# small bank icon in IBAN
old2 = '''    <svg viewBox="0 0 24 22" fill="#fff">
      <path d="M12 0 23 6v2H1V6z"/>
      <rect x="3" y="10" width="4.4" height="8" rx=".6"/>
      <rect x="9.8" y="10" width="4.4" height="8" rx=".6"/>
      <rect x="16.6" y="10" width="4.4" height="8" rx=".6"/>
      <rect x="0.6" y="19.4" width="22.8" height="2.6" rx="1"/>
    </svg>'''
new2 = '''    <svg viewBox="0 0 24 23" fill="#fff">
      <path d="M12 0 24 6.6v2.4H0V6.6z"/>
      <rect x="3.4" y="10.6" width="5" height="8.6" rx=".8"/>
      <rect x="15.6" y="10.6" width="5" height="8.6" rx=".8"/>
      <rect x="0.4" y="20.2" width="23.2" height="2.6" rx="1"/>
    </svg>'''
assert old2 in s
s = s.replace(old2, new2)

# transfer: stronger S curves, thinner
old3 = '''      <svg width="41" height="34" viewBox="0 0 41 34" fill="none">
        <path d="M2 12.5h7.5c6.5 0 7.5-7 14-7H30" stroke="#fff" stroke-width="4.6" stroke-linecap="round"/>
        <path d="M2 21.5h7.5c6.5 0 7.5 7 14 7H30" stroke="#fff" stroke-width="4.6" stroke-linecap="round"/>
        <path d="M28 1.2 39.4 5.7 28 10.2 Z" fill="#fff" stroke="#fff" stroke-width="2" stroke-linejoin="round"/>
        <path d="M28 23.8 39.4 28.3 28 32.8 Z" fill="#fff" stroke="#fff" stroke-width="2" stroke-linejoin="round"/>
      </svg>'''
new3 = '''      <svg width="41" height="34" viewBox="0 0 41 34" fill="none">
        <path d="M2 11.6h6.6c6.4 0 7.2-7.6 13.6-7.6H29" stroke="#fff" stroke-width="4.4" stroke-linecap="round"/>
        <path d="M2 22.4h6.6c6.4 0 7.2 7.6 13.6 7.6H29" stroke="#fff" stroke-width="4.4" stroke-linecap="round"/>
        <path d="M26.5 0.4 39.2 4 26.5 10 Z" fill="#fff" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/>
        <path d="M26.5 24 39.2 30 26.5 33.6 Z" fill="#fff" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/>
      </svg>'''
assert old3 in s
s = s.replace(old3, new3)

# search icon slightly smaller ring / thinner stroke
s = s.replace('''      <circle cx="10.6" cy="10.6" r="7" stroke="#fff" stroke-width="3"/>
      <path d="M16 16 L21.4 21.4" stroke="#fff" stroke-width="3" stroke-linecap="round"/>''',
'''      <circle cx="10.4" cy="10.4" r="7.4" stroke="#fff" stroke-width="2.9"/>
      <path d="M16.1 16.1 L21.4 21.4" stroke="#fff" stroke-width="2.9" stroke-linecap="round"/>''')

# aircash: smaller logo type, wider wings
s = s.replace('''  .aircash .logo{
    color:#fff; font-size:12.5px; font-weight:700; letter-spacing:-.2px;
    display:flex; align-items:center; gap:2px;
  }
  .aircash .wing{ display:flex; flex-direction:column; gap:1.5px; }
  .aircash .wing i{ display:block; width:6px; height:1.6px; background:#fff; border-radius:1px; }''',
'''  .aircash .logo{
    color:#fff; font-size:13px; font-weight:700; letter-spacing:-.3px;
    display:flex; align-items:center; gap:2.5px; margin-top:-1px;
  }
  .aircash .wing{ display:flex; flex-direction:column; gap:1.6px; }
  .aircash .wing i{ display:block; width:6.5px; height:1.7px; background:#fff; border-radius:1px; }''')
s = s.replace('background:#e50134;', 'background:#e10231;')

# feed row2 -1px
s = s.replace('style="left:137px; top:34.7px"', 'style="left:137px; top:33.7px"')
s = s.replace('style="right:32px; top:35.7px"', 'style="right:32px; top:34.7px"')

open(p, 'w', encoding='utf-8').write(s)
print('ok')
