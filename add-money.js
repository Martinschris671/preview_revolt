// Add money: calculator keypad + Apple Pay sheet.
(function () {
  var amountVal = document.getElementById('amountVal');
  var amountEl = document.getElementById('amount');
  var payBtn = document.getElementById('payBtn');
  var keys = document.getElementById('keys');
  var ops = document.querySelectorAll('.op');

  var MAX = 99999;       // highest amount: 99 999,00 €
  var rem = function () { return parseFloat(getComputedStyle(document.documentElement).fontSize); };

  var current = '100';   // what is shown / being typed
  var stored = null;     // left operand after an operator
  var pending = null;    // '+', '-', '*', '/'
  var fresh = false;     // next digit starts a new number

  function format(str) {
    // thousands separator (thin space), decimal comma kept as typed
    var parts = str.split(',');
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    return parts.join(',');
  }
  function render() {
    amountVal.textContent = format(current);
    payBtn.disabled = num(current) <= 0;   // nothing to pay at 0
    fitAmount();
  }
  function num(str) { return parseFloat(str.replace(/\s/g, '').replace(',', '.')) || 0; }

  // Amount scale: short amounts keep the full size; once the amount gets wider than about
  // half the screen it shrinks smoothly to stay there, and it never runs past the side margins.
  var BASE_REM = 4.57, KEEP_WIDTH = 0.49, MIN_SCALE = 0.55;
  function fitAmount(instant) {
    if (instant === true) amountEl.style.transition = 'none';
    var r = rem(), base = BASE_REM * r;
    var size = parseFloat(getComputedStyle(amountEl).fontSize) || base;  // may be mid-transition
    var natural = amountEl.getBoundingClientRect().width * base / size;   // width at full size
    var room = amountEl.parentNode.clientWidth;
    var target = Math.min(room * KEEP_WIDTH, room - 3.28 * r);
    var scale = natural > target ? Math.max(MIN_SCALE, target / natural) : 1;
    amountEl.style.setProperty('--amt-size', (base * scale).toFixed(2) + 'px');
    if (instant === true) { void amountEl.offsetWidth; amountEl.style.transition = ''; }
  }

  var shakeTimer = null;
  function shake() {   // feedback when the 99 999,00 limit is hit
    amountEl.classList.remove('shake');
    void amountEl.offsetWidth;
    amountEl.classList.add('shake');
    clearTimeout(shakeTimer);   // fallback in case animationend never fires (reduced motion etc.)
    shakeTimer = setTimeout(function () { amountEl.classList.remove('shake'); }, 360);
  }
  amountEl.addEventListener('animationend', function (e) {
    if (e.animationName === 'amt-shake') amountEl.classList.remove('shake');
  });
  function toStr(n) {
    var r = Math.round(n * 100) / 100;
    return (Number.isInteger(r) ? String(r) : r.toFixed(2)).replace('.', ',');
  }

  function inputDigit(d) {
    var next = fresh ? '0' : current;
    if (d === ',') {
      if (next.indexOf(',') === -1) next += ',';
    } else if (next === '0') {
      next = d;
    } else {
      var dec = next.split(',')[1];
      if (dec && dec.length >= 2) return;              // max 2 decimals
      next += d;
    }
    if (num(next) > MAX) { shake(); return; }          // max 99 999,00
    current = next; fresh = false;
    render();
  }
  function backspace() {
    if (fresh) return;
    current = current.length > 1 ? current.slice(0, -1) : '0';
    if (current === '-' || current === '') current = '0';
    render();
  }
  function compute(a, b, op) {
    if (op === '+') return a + b;
    if (op === '-') return a - b;
    if (op === '*') return a * b;
    if (op === '/') return b === 0 ? a : a / b;
    return b;
  }
  function setOp(op) {
    if (pending !== null && !fresh) {
      var result = compute(num(stored), num(current), pending);
      // an amount to add can't be negative or above the limit
      var clamped = Math.min(MAX, Math.max(0, result));
      if (clamped !== result) shake();
      stored = clamped;
      current = toStr(stored);
      render();
    } else {
      stored = current;
    }
    if (op === '=') { pending = null; stored = null; }
    else pending = op;
    fresh = true;
  }

  function paying() { return document.body.classList.contains('paying'); }

  keys.addEventListener('click', function (e) {
    var btn = e.target.closest('.key'); if (!btn || paying()) return;
    var k = btn.getAttribute('data-k');
    if (k === 'back') backspace(); else inputDigit(k);
  });
  ops.forEach(function (op) {
    op.addEventListener('click', function () { if (!paying()) setOp(op.getAttribute('data-op')); });
  });
  document.addEventListener('keydown', function (e) {
    if (paying()) { if (e.key === 'Escape') closePay(); return; }
    if (e.key >= '0' && e.key <= '9') inputDigit(e.key);
    else if (e.key === ',' || e.key === '.') inputDigit(',');
    else if (e.key === 'Backspace') backspace();
    else if ('+-*/'.indexOf(e.key) > -1) setOp(e.key);
    else if (e.key === 'Enter' || e.key === '=') setOp('=');
  });

  render();

  // ---- Apple Pay sheet ----
  // The page stays behind the sheet, dimmed: the amount and the method pill slide down
  // until the pill tucks under the sheet's top edge (as in the screenshot), the keypad hides.
  var layer = document.getElementById('payLayer');
  var sheet = document.getElementById('paySheet');
  var mid = document.getElementById('mid');
  var method = document.getElementById('method');
  var psAmount = document.getElementById('psAmount');

  // "Potvrdite bočnom tipkom": a still glyph (the arrow never moves). Tapping it (or Enter/Space
  // on it) records the top-up (home balance + recent transactions), plays the success animation
  // (phone out, ring green, checkmark in), waits a second, then goes back home.
  var glyphEl = document.getElementById('sideGlyph');
  var confirmed = false;
  var SUCCESS_HOLD_MS = 1300;   // ~0.3s checkmark + 1s pause before going home
  function confirmPay() {
    if (confirmed || !layer.classList.contains('open')) return;
    confirmed = true;
    BankStore.addTopUp(Math.round(num(current) * 100));
    glyphEl.classList.add('is-done');
    glyphEl.setAttribute('aria-label', 'Potvrđeno');
    setTimeout(leave, SUCCESS_HOLD_MS);
  }
  glyphEl.addEventListener('click', confirmPay);
  glyphEl.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); confirmPay(); }
  });

  function placeBehindSheet() {
    // measure the amount and pill at their resting place (no transform, no transition running)
    mid.style.transition = 'none';
    mid.style.transform = 'none';
    var amtRect = document.getElementById('amount').getBoundingClientRect();
    var pillRect = method.getBoundingClientRect();
    // the sheet may still be mid-slide: take its resting top (without the current translate)
    var slide = new DOMMatrix(getComputedStyle(sheet).transform).m42 || 0;
    var sheetTop = sheet.getBoundingClientRect().top - slide;
    var overlap = 0.42 * rem(); // the pill sits 8px under the sheet's top rim
    var shift = sheetTop + overlap - pillRect.bottom;

    void mid.offsetHeight; // commit the resting position, then animate down from it
    mid.style.transition = '';
    mid.style.transform = 'translateY(' + shift + 'px)';

    // short screens: if the moved amount or pill would land under the side-button hint, fade them out
    var hint = document.querySelector('.side-hint').getBoundingClientRect();
    var clash = [amtRect, pillRect].some(function (r) {
      return r.top + shift < hint.bottom && r.bottom + shift > hint.top && r.right > hint.left && r.left < hint.right;
    });
    document.body.classList.toggle('pay-tight', clash);
  }
  function openPay() {
    if (num(current) <= 0) return;
    confirmed = false;
    glyphEl.classList.remove('is-done');
    glyphEl.setAttribute('aria-label', 'Potvrdite bočnom tipkom');
    psAmount.textContent = num(current).toFixed(2).replace('.', ',').replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + ' €';
    document.body.classList.add('paying');
    layer.classList.add('open');
    layer.setAttribute('aria-hidden', 'false');
    placeBehindSheet();
  }
  function closePay() {
    document.body.classList.remove('paying', 'pay-tight');
    layer.classList.remove('open');
    layer.setAttribute('aria-hidden', 'true');
    mid.style.transform = '';
  }
  document.getElementById('payBtn').addEventListener('click', openPay);
  document.getElementById('psClose').addEventListener('click', closePay);
  window.addEventListener('resize', function () {
    fitAmount();
    if (layer.classList.contains('open')) placeBehindSheet();
  });
  if (document.fonts) document.fonts.ready.then(function () { fitAmount(true); });   // re-measure once Inter has loaded

  // Leave this page: back to the home page we came from (keeps its history), otherwise open it.
  function leave() {
    var fromHome = false;
    try { fromHome = sessionStorage.getItem('addmoney.from') === 'home'; sessionStorage.removeItem('addmoney.from'); } catch (e) {}
    PageTransition.go('back', function () {
      if (fromHome && history.length > 1) history.back();
      else location.replace('index.html');
    });
  }
  document.getElementById('back').addEventListener('click', leave);

  // "Saldo" shows the real balance
  document.getElementById('balance').textContent = BankStore.formatAmount(BankStore.load().balance) + ' €';
})();
