p = 'index.html'
s = open(p, encoding='utf-8').read()
s = s.replace('<div class="ticon" style="width:34px;height:37px;text-align:center;font-family:Aeonik;',
              '<div class="ticon" style="top:27px;width:34px;height:37px;text-align:center;font-family:Aeonik;')
s = s.replace('transform:translateX(-50%);top:22px;text-align:center;font-size:42px',
              'transform:translateX(-50%);top:31px;text-align:center;font-size:42px')
s = s.replace('<svg class="ticon" style="top:27px" width="34" height="36" viewBox="0 0 34 36" fill="none">',
              '<svg class="ticon" style="top:27px" width="36" height="37" viewBox="0 0 34 36" fill="none">')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
