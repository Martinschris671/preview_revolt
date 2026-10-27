p = 'index.html'
s = open(p, encoding='utf-8').read()

s = s.replace('''    position:absolute; left:26px; top:6px; width:110px; height:106px;
    border-radius:53px;
    background:rgba(255,255,255,.13);
    filter:blur(9px);''', '''    position:absolute; left:24px; top:8px; width:136px; height:104px;
    border-radius:52px;
    background:rgba(255,255,255,.11);
    filter:blur(6px);''')

old_r = '''      <svg class="ticon" width="28" height="37" viewBox="0 0 28 37" fill="#fff">
        <path d="M0 0h14.5C23 0 28 4.6 28 12c0 5.2-2.6 9.1-7.1 10.9L27.4 37h-9.3l-5.9-13H8.3v13H0V0zm8.3 6.6v10.7h5.4c4.6 0 6.4-2 6.4-5.4 0-3.4-2.2-5.3-6.4-5.3H8.3z"/>
      </svg>'''
new_r = '''      <svg class="ticon" width="28" height="36" viewBox="0 0 28 36" fill="#fff" fill-rule="evenodd">
        <path d="M0 0H18C24.2 0 28 4.4 28 10.6C28 16 24.6 19.5 19.2 20.2L28 36H19.6L11.6 21.3H7V36H0V0ZM7 6.6V14.6H17.2C19.8 14.6 21.1 13.1 21.1 10.6C21.1 8.1 19.8 6.6 17.2 6.6H7Z"/>
      </svg>'''
assert old_r in s
s = s.replace(old_r, new_r)

open(p, 'w', encoding='utf-8').write(s)
print('ok')
