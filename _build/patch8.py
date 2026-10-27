p = 'index.html'
s = open(p, encoding='utf-8').read()

old_r = '''      <svg class="ticon" width="28" height="36" viewBox="0 0 28 36" fill="#fff" fill-rule="evenodd">
        <path d="M0 0H18C24.2 0 28 4.4 28 10.6C28 16 24.6 19.5 19.2 20.2L28 36H19.6L11.6 21.3H7V36H0V0ZM7 6.6V14.6H17.2C19.8 14.6 21.1 13.1 21.1 10.6C21.1 8.1 19.8 6.6 17.2 6.6H7Z"/>
      </svg>'''
new_r = '''      <div class="ticon" style="width:34px;height:37px;text-align:center;font-family:Aeonik;font-size:52px;line-height:36px;font-weight:500;color:#fff">R</div>'''
if old_r in s:
    s = s.replace(old_r, new_r)
    print('R replaced')
else:
    print('R NOT FOUND')

s = s.replace('font-size:47px;line-height:32px', 'font-size:50px;line-height:34px')
open(p, 'w', encoding='utf-8').write(s)
