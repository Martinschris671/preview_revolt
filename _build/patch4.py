p = 'index.html'
s = open(p, encoding='utf-8').read()

# ---------- header border / NN ----------
s = s.replace('border:2px solid rgba(255,255,255,.28);', 'border:2px solid rgba(206,74,255,.85);')
s = s.replace('font-size:28.7px; font-weight:600; font-variation-settings:"wght" 600,"opsz" 14;\n    letter-spacing:.1px; line-height:1;\n  }',
              'font-size:28.7px; font-weight:500; font-variation-settings:"wght" 500,"opsz" 14;\n    letter-spacing:.1px; line-height:1;\n  }')

# ---------- analytics icon ----------
s = s.replace('''      <svg width="37" height="34" viewBox="0 0 38 35" fill="#fff">
      <rect x="0"  y="14" width="10" height="21" rx="5"/>
      <rect x="13" y="0"  width="11" height="35" rx="5.5"/>
      <rect x="28" y="9"  width="10" height="26" rx="5"/>
    </svg>''', '''      <svg width="37" height="34" viewBox="0 0 37 34" fill="#fff">
      <rect x="0"  y="22" width="10" height="12" rx="5"/>
      <rect x="14" y="0"  width="10" height="34" rx="5"/>
      <rect x="27" y="11" width="10" height="23" rx="5"/>
    </svg>''')

# ---------- card icon ----------
s = s.replace('''    <svg width="38" height="26" viewBox="0 0 40 30">
      <defs><mask id="cardmask">
        <rect width="40" height="30" fill="#fff"/>
        <rect x="0" y="9" width="40" height="4" fill="#000"/>
        <rect x="5" y="21" width="13" height="3.6" rx="1.8" fill="#000"/>
      </mask></defs>
      <rect width="40" height="30" rx="6.5" fill="#fff" mask="url(#cardmask)"/>
    </svg>''', '''    <svg width="38" height="26" viewBox="0 0 38 26">
      <defs><mask id="cardmask">
        <rect width="38" height="26" fill="#fff"/>
        <rect x="0" y="6.4" width="38" height="2.8" fill="#000"/>
        <rect x="5.5" y="17.6" width="12" height="3.4" rx="1.7" fill="#000"/>
      </mask></defs>
      <rect width="38" height="26" rx="6.2" fill="#fff" mask="url(#cardmask)"/>
    </svg>''')

# ---------- transfer icon ----------
s = s.replace('''      <svg width="44" height="38" viewBox="0 0 44 38" fill="none">
        <path d="M2 10.5h9.5c8 0 6.5-7 15.5-7h6" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
        <path d="M2 27.5h9.5c8 0 6.5 7 15.5 7h6" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
        <path d="M33 0l9 4.8-9 4.8z" fill="#fff"/>
        <path d="M33 33l9 4.8-9 4.8z" fill="#fff"/>
      </svg>''', '''      <svg width="41" height="34" viewBox="0 0 41 34" fill="none">
        <path d="M2 12.5h7.5c6.5 0 7.5-7 14-7H30" stroke="#fff" stroke-width="4.6" stroke-linecap="round"/>
        <path d="M2 21.5h7.5c6.5 0 7.5 7 14 7H30" stroke="#fff" stroke-width="4.6" stroke-linecap="round"/>
        <path d="M28 1.2 39.4 5.7 28 10.2 Z" fill="#fff" stroke="#fff" stroke-width="2" stroke-linejoin="round"/>
        <path d="M28 23.8 39.4 28.3 28 32.8 Z" fill="#fff" stroke="#fff" stroke-width="2" stroke-linejoin="round"/>
      </svg>''')

# ---------- pay icon ----------
s = s.replace('''      <svg class="ticon" width="40" height="38" viewBox="0 0 40 38" fill="rgba(255,255,255,.75)">
        <path d="M20.5 1.5h10.2l8.8 8.4-8.8 8.4H20.5V1.5z"/>
        <path d="M19.5 36.5H9.3L.5 28.1l8.8-8.4h10.2v16.8z"/>
        <rect x="9.5" y="14" width="21" height="5.2" rx="1"/>
      </svg>''', '''      <svg class="ticon" width="39" height="38" viewBox="0 0 39 38" fill="rgba(255,255,255,.8)">
        <rect x="4" y="5.5" width="22" height="7.4" rx="3.2"/>
        <path d="M25 0.5 39 9.2 25 17.9 Z" stroke="rgba(255,255,255,.8)" stroke-width="2.5" stroke-linejoin="round"/>
        <rect x="13" y="25.1" width="22" height="7.4" rx="3.2"/>
        <path d="M14 19.1 0 27.8 14 36.5 Z" stroke="rgba(255,255,255,.8)" stroke-width="2.5" stroke-linejoin="round"/>
      </svg>''')

# ---------- invest icon ----------
s = s.replace('''      <svg class="ticon" width="35" height="37" viewBox="0 0 35 37" fill="none">
        <path d="M1.6 16.4c4.6 0 5.6-4.4 9.3-4.4 3 0 4.4 2.2 6.2 4.4" stroke="rgba(255,255,255,.75)" stroke-width="3" stroke-linecap="round"/>
        <rect x="1"  y="24" width="4.4" height="13" rx="2.2" fill="rgba(255,255,255,.75)"/>
        <rect x="9.4" y="19" width="4.4" height="18" rx="2.2" fill="rgba(255,255,255,.75)"/>
        <rect x="17.8" y="24" width="4.4" height="13" rx="2.2" fill="rgba(255,255,255,.75)"/>
        <rect x="26.2" y="10" width="4.4" height="27" rx="2.2" fill="rgba(255,255,255,.75)"/>
      </svg>''', '''      <svg class="ticon" width="34" height="36" viewBox="0 0 34 36" fill="none">
        <path d="M1.6 11.6c3.2-4.4 5.9-4.8 9-1.4 3.2 3.5 5.8 3.2 8.8-.6 3-3.8 5.8-5.6 9.4-5.8"
              stroke="rgba(255,255,255,.8)" stroke-width="3.2" stroke-linecap="round"/>
        <rect x="0.6" y="24" width="4.6" height="12" rx="2.3" fill="rgba(255,255,255,.8)"/>
        <rect x="9.6" y="19" width="4.6" height="17" rx="2.3" fill="rgba(255,255,255,.8)"/>
        <rect x="18.6" y="24" width="4.6" height="12" rx="2.3" fill="rgba(255,255,255,.8)"/>
        <rect x="27.6" y="9" width="4.6" height="27" rx="2.3" fill="rgba(255,255,255,.8)"/>
      </svg>''')

# ---------- bitcoin icon ----------
old_btc = s[s.index('<div class="tab t4">'):s.index('<div class="tab t5">')]
new_btc = '''<div class="tab t4">
      <div class="ticon" style="width:40px;height:38px;position:absolute;left:50%;transform:translateX(-50%);top:28px;text-align:center;font-size:47px;line-height:32px;font-weight:500;font-variation-settings:"wght" 500,"opsz" 24;color:rgba(255,255,255,.8)">₿</div>
      <div class="tlabel">Kriptovalute</div>
    </div>

    '''
s = s.replace(old_btc, new_btc)

# ---------- revpoints icon ----------
old_rev = s[s.index('<div class="tab t5">'):s.index('</nav>')]
new_rev = '''<div class="tab t5">
      <svg class="ticon" width="36" height="40" viewBox="0 0 36 40">
        <defs><mask id="revmask">
          <path d="M18 0 36 10v20L18 40 0 30V10z" fill="#fff"/>
          <path d="M18 9.2c1 5.1 2.7 6.8 7.8 7.8-5.1 1-6.8 2.7-7.8 7.8-1-5.1-2.7-6.8-7.8-7.8 5.1-1 6.8-2.7 7.8-7.8z" fill="#000"/>
        </mask></defs>
        <rect width="36" height="40" fill="#d9d8e6" mask="url(#revmask)"/>
      </svg>
      <div class="tlabel">RevPoints</div>
    </div>
  '''
s = s.replace(old_rev, new_rev)

# ---------- active blob ----------
s = s.replace('''    position:absolute; left:23px; top:3px; width:190px; height:110px;
    border-radius:55px;
    background:rgba(255,255,255,.14);
    filter:blur(14px);''', '''    position:absolute; left:26px; top:6px; width:110px; height:106px;
    border-radius:53px;
    background:rgba(255,255,255,.13);
    filter:blur(9px);''')

open(p, 'w', encoding='utf-8').write(s)
print('patched')
