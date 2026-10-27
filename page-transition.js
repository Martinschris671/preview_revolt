// Page transition between the home screen and the add-money screen, so the two feel like one app:
// the leaving page slides a little and fades to black (0.13s), the arriving page slides in from the
// side and fades up from black (0.28s). Load it in <head> so the arriving page starts on the right frame.
//   PageTransition.go('fwd' | 'back', function () { location.href = ... });
var PageTransition = (function () {
  var KEY = 'pt.dir';
  var OUT_MS = 130, IN_MS = 280;
  var root = document.documentElement;

  var css =
    '@keyframes pt-bg{from{background-color:#000}}' +
    '@keyframes pt-in-fade{from{opacity:0}}' +
    '@keyframes pt-in-fwd{from{opacity:0;translate:12% 0}}' +
    '@keyframes pt-in-back{from{opacity:0;translate:-12% 0}}' +
    'html.pt-in,html.pt-in body{animation:pt-bg ' + IN_MS + 'ms cubic-bezier(.2,.8,.2,1) both}' +
    'html.pt-in body>*:not(script){animation:pt-in-fade ' + IN_MS + 'ms cubic-bezier(.2,.8,.2,1) both}' +
    'html.pt-in.pt-fwd body>*:not(script){animation-name:pt-in-fwd}' +
    'html.pt-in.pt-back body>*:not(script){animation-name:pt-in-back}' +
    'html.pt-out,html.pt-out body{background-color:#000!important;transition:background-color ' + OUT_MS + 'ms ease-in}' +
    'html.pt-out body>*:not(script){opacity:0!important;pointer-events:none!important;transition:opacity ' + OUT_MS + 'ms ease-in,translate ' + OUT_MS + 'ms ease-in!important}' +
    'html.pt-out.pt-fwd body>*:not(script){translate:-6% 0}' +
    'html.pt-out.pt-back body>*:not(script){translate:6% 0}' +
    '@media (prefers-reduced-motion:reduce){html.pt-in body>*:not(script){animation-name:pt-in-fade!important}html.pt-out body>*:not(script){translate:none!important}}';
  var style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  function takeDir() {
    var d = null;
    try { d = sessionStorage.getItem(KEY); sessionStorage.removeItem(KEY); } catch (e) {}
    return d;
  }

  var inTimer = null;
  function playIn(dir) {
    root.classList.remove('pt-out', 'pt-in', 'pt-fwd', 'pt-back');
    void root.offsetWidth;   // restart the animation
    root.classList.add('pt-in');
    if (dir === 'fwd' || dir === 'back') root.classList.add('pt-' + dir);
    clearTimeout(inTimer);
    inTimer = setTimeout(function () { root.classList.remove('pt-in', 'pt-fwd', 'pt-back'); }, IN_MS + 60);
  }

  function go(dir, navigate) {
    try { sessionStorage.setItem(KEY, dir); } catch (e) {}
    clearTimeout(inTimer);
    root.classList.remove('pt-in', 'pt-fwd', 'pt-back');
    root.classList.add('pt-out', 'pt-' + dir);
    setTimeout(navigate, OUT_MS);
    // if the navigation never happens (blocked, nothing to go back to), bring this page back
    setTimeout(function () {
      if (root.classList.contains('pt-out')) { takeDir(); playIn(dir === 'fwd' ? 'back' : 'fwd'); }
    }, 1500);
  }

  playIn(takeDir());   // arriving: 'fwd' / 'back' from the page we came from, plain fade otherwise

  // coming back from the browser's back/forward cache: the page still has its "leaving" look
  window.addEventListener('pageshow', function (e) {
    if (e.persisted) playIn(takeDir() || 'back');
  });

  return { go: go };
})();
