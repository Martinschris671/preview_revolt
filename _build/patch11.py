p = 'index.html'
s = open(p, encoding='utf-8').read()

s = s.replace('position:absolute; left:0; top:23.2px; width:619px; text-align:center;',
              'position:absolute; left:0; top:25.2px; width:619px; text-align:center;')

script = '''
<script>
/* Fit the fixed 739x1600 reference frame into a narrower viewport.
   At width >= 739 the stage renders at exactly 1:1 (no transform). */
(function () {
  var stage = document.getElementById('stage');
  function fit() {
    var s = Math.min(1, window.innerWidth / 739);
    if (s < 1) {
      stage.style.transformOrigin = 'top left';
      stage.style.transform = 'scale(' + s + ')';
      document.body.style.width = (739 * s) + 'px';
      document.body.style.height = (1600 * s) + 'px';
      document.body.style.overflow = 'hidden';
    } else {
      stage.style.transform = 'none';
      document.body.style.width = '';
      document.body.style.height = '';
      document.body.style.overflow = '';
    }
  }
  window.addEventListener('resize', fit);
  fit();
})();
</script>
</body>'''
s = s.replace('</body>', script, 1)
open(p, 'w', encoding='utf-8').write(s)
print('ok')
