// Translations (HR / EN). Elements carry data-i18n (text) or data-i18n-aria (aria-label).
var i18n = (function () {
  var KEY = 'app.lang';
  var STRINGS = {
    hr: {
      'page.title': 'Početna',
      'search': 'Pretraživanje',
      'aria.profile': 'Profil',
      'aria.analytics': 'Analitika',
      'aria.cards': 'Kartice',
      'balance.label': 'Osobni · EUR',
      'act.add': 'Dodaj novac',
      'act.move': 'Prebaci',
      'act.details': 'Pojedinosti',
      'act.more': 'Više',
      'setup.title': 'Dovršite postavljanje',
      'setup.desc': 'Najbolje iskoristite Revolut uz par jednostavnih koraka.',
      'setup.cta': 'Dovršite postavljanje',
      'setupSheet.text': 'Želite li zadržati ovu karticu na početnom zaslonu ili je ukloniti?',
      'setupSheet.progress': 'Napredak',
      'progress.dec': 'Smanji napredak',
      'progress.inc': 'Povećaj napredak',
      'tx.today': 'Danas',
      'tx.topup': 'Novac dodan putem Apple Pay',
      'tx.justNow': 'Prije nekoliko trenutaka',
      'tx.yesterday': 'Jučer',
      'all.title': 'Transakcije',
      'all.empty': 'Još nema transakcija',
      'feed.all': 'Prikaži sve',
      'tab.home': 'Početna',
      'tab.invest': 'Ulaganje',
      'tab.payments': 'Plaćanja',
      'tab.crypto': 'Kriptovalute',
      'common.keep': 'Zadrži',
      'common.remove': 'Ukloni',
      'common.save': 'Spremi',
      'common.cancel': 'Odustani',
      'profile.title': 'Profil',
      'profile.upload': 'Učitaj fotografiju',
      'profile.change': 'Promijeni fotografiju',
      'profile.initials': 'Inicijali (najviše 2 slova)',
      'profile.dot': 'Točkica obavijesti',
      'profile.language': 'Jezik',
      'reset.button': 'Vrati na zadano',
      'reset.title': 'Vratiti sve na zadano?',
      'reset.text': 'Inicijali, fotografija, točkica, IBAN, kartica postavljanja i jezik vratit će se na početne postavke.',
      'reset.confirm': 'Vrati na zadano',
      'iban.title': 'Uredi IBAN'
    },
    en: {
      'page.title': 'Home',
      'search': 'Search',
      'aria.profile': 'Profile',
      'aria.analytics': 'Analytics',
      'aria.cards': 'Cards',
      'balance.label': 'Personal · EUR',
      'act.add': 'Add money',
      'act.move': 'Move',
      'act.details': 'Details',
      'act.more': 'More',
      'setup.title': 'Finish setting up',
      'setup.desc': 'Get the most out of Revolut with a few simple steps.',
      'setup.cta': 'Finish setting up',
      'setupSheet.text': 'Do you want to keep this card on your home screen or remove it?',
      'setupSheet.progress': 'Progress',
      'progress.dec': 'Decrease progress',
      'progress.inc': 'Increase progress',
      'tx.today': 'Today',
      'tx.topup': 'Money added via Apple Pay',
      'tx.justNow': 'A few moments ago',
      'tx.yesterday': 'Yesterday',
      'all.title': 'Transactions',
      'all.empty': 'No transactions yet',
      'feed.all': 'See all',
      'tab.home': 'Home',
      'tab.invest': 'Invest',
      'tab.payments': 'Payments',
      'tab.crypto': 'Crypto',
      'common.keep': 'Keep',
      'common.remove': 'Remove',
      'common.save': 'Save',
      'common.cancel': 'Cancel',
      'profile.title': 'Profile',
      'profile.upload': 'Upload photo',
      'profile.change': 'Change photo',
      'profile.initials': 'Initials (max 2 letters)',
      'profile.dot': 'Notification dot',
      'profile.language': 'Language',
      'reset.button': 'Reset to default',
      'reset.title': 'Reset everything?',
      'reset.text': 'Your initials, photo, dot, IBAN, setup card and language will go back to their original settings.',
      'reset.confirm': 'Reset',
      'iban.title': 'Edit IBAN'
    }
  };
  var lang = 'hr';
  try { var saved = localStorage.getItem(KEY); if (STRINGS[saved]) lang = saved; } catch (e) {}
  var listeners = [];

  function t(key) { return STRINGS[lang][key] || STRINGS.hr[key] || key; }
  function apply() {
    document.documentElement.lang = lang;
    document.title = t('page.title');
    document.querySelectorAll('[data-i18n]').forEach(function (el) { el.textContent = t(el.getAttribute('data-i18n')); });
    document.querySelectorAll('[data-i18n-aria]').forEach(function (el) { el.setAttribute('aria-label', t(el.getAttribute('data-i18n-aria'))); });
    listeners.forEach(function (fn) { fn(lang); });
  }
  function set(next) {
    if (!STRINGS[next] || next === lang) return;
    lang = next;
    try {
      if (next === 'hr') localStorage.removeItem(KEY); // Croatian is the default
      else localStorage.setItem(KEY, next);
    } catch (e) {}
    apply();
  }
  return {
    t: t, set: set, apply: apply,
    get lang() { return lang; },
    onChange: function (fn) { listeners.push(fn); }
  };
})();
i18n.apply();

// Liquid tab indicator: slides the glass blob under the tapped tab.
(function () {
  var bar = document.getElementById('tabbar');
  var blob = document.getElementById('blob');
  var tabs = bar.querySelectorAll('.tab');
  function place(tab) {
    var x = tab.offsetLeft + tab.offsetWidth / 2 - blob.offsetWidth / 2;
    blob.style.transform = 'translateX(' + x + 'px)';
  }
  tabs.forEach(function (t) {
    t.addEventListener('click', function () {
      tabs.forEach(function (o) { o.classList.remove('active'); });
      t.classList.add('active');
      place(t);
    });
  });
  function sync() { place(bar.querySelector('.tab.active')); }
  blob.style.transition = 'none'; sync();
  requestAnimationFrame(function () { blob.style.transition = ''; });
  window.addEventListener('resize', sync);
  if (document.fonts) document.fonts.ready.then(sync);
})();

// Circled-plus badge: show it on the logo of any addition (positive amount).
// Also used for transaction rows drawn later (recent list, "see all").
function addTxBadges(root) {
  var PLUS = '<svg viewBox="0 0 24 24" fill="none" stroke="#1b1b1d" stroke-width="2.7" stroke-linecap="round"><path d="M12 5.9v12.2M5.9 12h12.2"/></svg>';
  root.querySelectorAll('.tx').forEach(function (tx) {
    var amt = tx.querySelector('.amt'), logo = tx.querySelector('.logo');
    var added = amt && (amt.classList.contains('pos') || /^\s*\+/.test(amt.textContent));
    if (added && logo && !tx.querySelector('.badge')) {
      var b = document.createElement('span');
      b.className = 'badge';
      b.innerHTML = PLUS;
      logo.insertAdjacentElement('afterend', b);
    }
  });
}
addTxBadges(document);

// Bottom sheets: setup-card options (keep / remove) and profile (initials / photo).
(function () {
  var backdrop = document.getElementById('sheetBackdrop');
  var current = null;

  function open(sheet) {
    if (current) close();
    current = sheet;
    backdrop.hidden = false;
    sheet.hidden = false;
    void sheet.offsetHeight; // lay out the closed position first so the slide-up animates
    backdrop.classList.add('open');
    sheet.classList.add('open');
  }

  function close() {
    if (!current) return;
    var sheet = current;
    current = null;
    backdrop.classList.remove('open');
    sheet.classList.remove('open');
    setTimeout(function () {
      if (current !== sheet) sheet.hidden = true;
      if (!current) backdrop.hidden = true;
    }, 400);
  }

  backdrop.addEventListener('click', close);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });

  // ---- setup card: keep or remove ----
  var KEY_SETUP_REMOVED = 'setup.removed';
  var setup = document.querySelector('.setup');
  var setupSheet = document.getElementById('setupSheet');

  if (load(KEY_SETUP_REMOVED) === '1') setup.remove(); // removed earlier: keep it gone

  // ---- setup progress: 0-5 steps, set with the stepper in the setup sheet ----
  var KEY_SETUP_PROGRESS = 'setup.progress';
  var STEPS = 5, DEFAULT_STEPS = 4;
  var RING_C = 2 * Math.PI * 34.3;          // circumference of the ring circles
  var ring = document.getElementById('setupRing');
  var progressValue = document.getElementById('progressValue');
  var progressDec = document.getElementById('progressDec');
  var progressInc = document.getElementById('progressInc');
  var steps = parseInt(load(KEY_SETUP_PROGRESS), 10);
  if (!(steps >= 0 && steps <= STEPS)) steps = DEFAULT_STEPS;

  function renderProgress(instant) {
    var label = steps + '/' + STEPS;
    progressValue.textContent = label;
    progressDec.disabled = steps <= 0;
    progressInc.disabled = steps >= STEPS;
    if (!ring || !ring.isConnected) return;   // card removed
    // 300° track from 7 o'clock round to 5 o'clock: blue covers 60° per done step, grey the rest
    var doneDeg = 300 * steps / STEPS;
    var fill = ring.querySelector('.ring-fill'), track = ring.querySelector('.ring-track');
    if (instant) { fill.style.transition = track.style.transition = 'none'; }
    fill.style.strokeDasharray = (RING_C * doneDeg / 360).toFixed(2) + ' ' + RING_C.toFixed(2);
    fill.style.transform = 'rotate(120deg)';
    fill.style.opacity = steps > 0 ? '1' : '0';          // a zero-length round cap would show a dot
    track.style.strokeDasharray = (RING_C * (300 - doneDeg) / 360).toFixed(2) + ' ' + RING_C.toFixed(2);
    track.style.transform = 'rotate(' + (doneDeg - 240) + 'deg)';
    track.style.opacity = steps < STEPS ? '1' : '0';
    ring.querySelector('b').textContent = label;
    ring.setAttribute('aria-label', label);
    if (instant) { void ring.offsetWidth; fill.style.transition = track.style.transition = ''; }
  }
  function setSteps(n) {
    n = Math.max(0, Math.min(STEPS, n));
    if (n === steps) return;
    steps = n;
    store(KEY_SETUP_PROGRESS, String(steps));
    renderProgress(false);
  }
  progressDec.addEventListener('click', function () { setSteps(steps - 1); });
  progressInc.addEventListener('click', function () { setSteps(steps + 1); });
  renderProgress(true);

  setup.querySelector('.cta').addEventListener('click', function () { open(setupSheet); });
  setupSheet.querySelector('[data-action="keep"]').addEventListener('click', close);
  setupSheet.querySelector('[data-action="remove"]').addEventListener('click', function () {
    close();
    store(KEY_SETUP_REMOVED, '1');
    var gone = false;
    function finish() {
      if (gone) return;
      gone = true;
      setup.remove();
    }
    setup.style.height = setup.offsetHeight + 'px';
    setup.style.overflow = 'hidden';
    void setup.offsetHeight; // commit the start height before animating
    setup.classList.add('removing');
    setup.addEventListener('transitionend', function (e) {
      if (e.target === setup && e.propertyName === 'height') finish();
    });
    setTimeout(finish, 600); // fallback if transitions are disabled
  });

  // ---- profile: initials (max 2 letters) and photo ----
  var KEY_INITIALS = 'profile.initials';
  var KEY_PHOTO = 'profile.photo';
  var KEY_DOT = 'profile.dot';

  function load(key) {
    try { return localStorage.getItem(key); } catch (e) { return null; }
  }
  function store(key, value) {
    try {
      if (value) localStorage.setItem(key, value);
      else localStorage.removeItem(key);
    } catch (e) { /* storage unavailable: changes last until reload */ }
  }

  function cleanInitials(value) {
    var letters = value.replace(/[^\p{L}]/gu, '').toUpperCase();
    return Array.from(letters).slice(0, 2).join('');
  }

  function paint(el, s) {
    el.textContent = '';
    if (s.photo) {
      var img = new Image();
      img.className = 'avatar-img';
      img.alt = '';
      img.src = s.photo;
      el.appendChild(img);
    } else {
      el.textContent = s.initials;
    }
    if (s.dot) {
      var dot = document.createElement('span');
      dot.className = 'avatar-dot';
      el.appendChild(dot);
    }
  }

  var avatar = document.querySelector('.header .avatar');
  var profileSheet = document.getElementById('profileSheet');
  var preview = document.getElementById('profilePreview');
  var input = document.getElementById('initialsInput');
  var fileInput = document.getElementById('photoInput');
  var uploadBtn = document.getElementById('photoUpload');
  var removeBtn = document.getElementById('photoRemove');
  var saveBtn = document.getElementById('profileSave');
  var cancelBtn = document.getElementById('profileCancel');
  var dotToggle = document.getElementById('dotToggle');

  var state = {
    initials: cleanInitials(load(KEY_INITIALS) || '') || cleanInitials(avatar.textContent) || 'NN',
    photo: load(KEY_PHOTO),
    dot: load(KEY_DOT) === '1'
  };
  var draft = null;

  function applyAvatar() {
    paint(avatar, state);
    avatar.setAttribute('aria-label', i18n.t('aria.profile') + ' ' + state.initials);
  }

  function refreshDraft() {
    paint(preview, draft);
    removeBtn.hidden = !draft.photo;
    uploadBtn.textContent = i18n.t(draft.photo ? 'profile.change' : 'profile.upload');
    saveBtn.disabled = !draft.initials;
  }

  applyAvatar();

  avatar.addEventListener('click', function () {
    draft = { initials: state.initials, photo: state.photo, dot: state.dot };
    input.value = draft.initials;
    dotToggle.checked = draft.dot;
    refreshDraft();
    open(profileSheet);
  });

  input.addEventListener('input', function (e) {
    if (e.isComposing) return;
    var clean = cleanInitials(input.value);
    if (input.value !== clean) input.value = clean;
    draft.initials = clean;
    refreshDraft();
  });
  input.addEventListener('compositionend', function () {
    input.dispatchEvent(new Event('input'));
  });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !saveBtn.disabled) saveBtn.click();
  });

  uploadBtn.addEventListener('click', function () { fileInput.click(); });

  fileInput.addEventListener('change', function () {
    var file = fileInput.files && fileInput.files[0];
    fileInput.value = ''; // allow picking the same file again
    if (!file || !/^image\//.test(file.type)) return;
    var reader = new FileReader();
    reader.onload = function () {
      var img = new Image();
      img.onload = function () {
        // centre-crop to a square and shrink to 256px so it stays light to store
        var size = 256;
        var side = Math.min(img.naturalWidth, img.naturalHeight);
        var canvas = document.createElement('canvas');
        canvas.width = canvas.height = size;
        canvas.getContext('2d').drawImage(
          img,
          (img.naturalWidth - side) / 2, (img.naturalHeight - side) / 2, side, side,
          0, 0, size, size
        );
        draft.photo = canvas.toDataURL('image/jpeg', 0.9);
        refreshDraft();
      };
      img.src = reader.result;
    };
    reader.readAsDataURL(file);
  });

  removeBtn.addEventListener('click', function () {
    draft.photo = null;
    refreshDraft();
  });

  saveBtn.addEventListener('click', function () {
    if (!draft.initials) return;
    state = { initials: draft.initials, photo: draft.photo, dot: draft.dot };
    store(KEY_INITIALS, state.initials);
    store(KEY_PHOTO, state.photo);
    store(KEY_DOT, state.dot ? '1' : null);
    applyAvatar();
    close();
  });

  dotToggle.addEventListener('change', function () {
    draft.dot = dotToggle.checked;
    refreshDraft();
  });

  cancelBtn.addEventListener('click', close);

  // ---- IBAN: tap the row to edit (letters and digits, max 34 characters) ----
  var KEY_IBAN = 'account.iban';
  var IBAN_MAX = 34;
  var ibanRow = document.querySelector('.balance .iban');
  var ibanText = ibanRow.querySelector('span');
  var ibanSheet = document.getElementById('ibanSheet');
  var ibanInput = document.getElementById('ibanInput');
  var ibanCount = document.getElementById('ibanCount');
  var ibanSave = document.getElementById('ibanSave');
  var ibanCancel = document.getElementById('ibanCancel');

  function ibanRaw(value) { return value.replace(/[^A-Za-z0-9]/g, '').toUpperCase().slice(0, IBAN_MAX); }
  function ibanFormat(raw) { return raw.replace(/(.{4})(?=.)/g, '$1 '); }

  var savedIban = ibanRaw(load(KEY_IBAN) || '');
  if (savedIban) ibanText.textContent = ibanFormat(savedIban);

  ibanRow.setAttribute('role', 'button');
  ibanRow.setAttribute('tabindex', '0');
  ibanRow.setAttribute('aria-label', i18n.t('iban.title'));

  function ibanRefresh() {
    var raw = ibanRaw(ibanInput.value);
    ibanCount.textContent = raw.length + '/' + IBAN_MAX;
    ibanSave.disabled = !raw;
  }

  function ibanOpen() {
    ibanInput.value = ibanFormat(ibanRaw(ibanText.textContent));
    ibanRefresh();
    open(ibanSheet);
  }
  ibanRow.addEventListener('click', ibanOpen);
  ibanRow.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); ibanOpen(); }
  });

  // keep groups of 4 while typing, without the caret jumping
  ibanInput.addEventListener('input', function () {
    var value = ibanInput.value, caret = ibanInput.selectionStart || 0;
    var raw = ibanRaw(value);
    var before = Math.min(value.slice(0, caret).replace(/[^A-Za-z0-9]/g, '').length, raw.length);
    var formatted = ibanFormat(raw);
    if (formatted !== value) {
      ibanInput.value = formatted;
      var pos = before ? before + Math.floor((before - 1) / 4) : 0;
      if (document.activeElement === ibanInput) ibanInput.setSelectionRange(pos, pos);
    }
    ibanRefresh();
  });
  // backspace / delete next to a group space removes the character beside it
  ibanInput.addEventListener('keydown', function (e) {
    var v = ibanInput.value, a = ibanInput.selectionStart, b = ibanInput.selectionEnd;
    if (a !== b) return;
    if (e.key === 'Backspace' && a > 1 && v[a - 1] === ' ') {
      e.preventDefault();
      ibanInput.value = v.slice(0, a - 2) + v.slice(a);
      ibanInput.setSelectionRange(a - 2, a - 2);
      ibanInput.dispatchEvent(new Event('input'));
    } else if (e.key === 'Delete' && v[a] === ' ') {
      e.preventDefault();
      ibanInput.value = v.slice(0, a + 1) + v.slice(a + 2);
      ibanInput.setSelectionRange(a, a);
      ibanInput.dispatchEvent(new Event('input'));
    } else if (e.key === 'Enter' && !ibanSave.disabled) {
      ibanSave.click();
    }
  });

  ibanSave.addEventListener('click', function () {
    var raw = ibanRaw(ibanInput.value);
    if (!raw) return;
    ibanText.textContent = ibanFormat(raw);
    store(KEY_IBAN, raw);
    ibanInput.blur();
    close();
  });
  ibanCancel.addEventListener('click', function () { ibanInput.blur(); close(); });

  // ---- language (HR / EN): applies at once and is remembered ----
  var langButtons = profileSheet.querySelectorAll('.seg [data-lang]');
  function syncLang() {
    langButtons.forEach(function (b) {
      b.setAttribute('aria-checked', String(b.getAttribute('data-lang') === i18n.lang));
    });
    applyAvatar();
    ibanRow.setAttribute('aria-label', i18n.t('iban.title'));
    if (draft) refreshDraft();
  }
  langButtons.forEach(function (b) {
    b.addEventListener('click', function () { i18n.set(b.getAttribute('data-lang')); });
  });
  i18n.onChange(syncLang);
  syncLang();

  // ---- reset: clear everything saved and reload the original page ----
  var resetSheet = document.getElementById('resetSheet');
  document.getElementById('resetOpen').addEventListener('click', function () { open(resetSheet); });
  document.getElementById('resetCancel').addEventListener('click', close);
  document.getElementById('resetConfirm').addEventListener('click', function () {
    [KEY_INITIALS, KEY_PHOTO, KEY_DOT, KEY_SETUP_REMOVED, KEY_SETUP_PROGRESS, KEY_IBAN, 'app.lang', BankStore.KEY].forEach(function (key) {
      store(key, null);
    });
    location.reload();
  });

  // ---- account: live balance, recent transactions, "see all", add money ----
  var HOME_ROWS = 3;   // rows on the home card; "see all" lists every transaction
  var balanceEl = document.querySelector('.balance .amount');
  var balanceInt = balanceEl.querySelector('.int');
  var balanceCur = balanceEl.querySelector('.cur');
  var feed = document.querySelector('.feed');
  var seeAll = feed.querySelector('.see-all');
  var txSheet = document.getElementById('txSheet');
  var txList = document.getElementById('txList');
  var APPLE = '<svg viewBox="0 0 384 512" fill="#fff" style="width:1.55rem;height:2rem;margin-top:-.2rem"><path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg>';
  var AIRCASH = '<div class="aircash-mark"><div class="w"><i></i><i></i><i></i></div>aircash<div class="w"><i></i><i></i><i></i></div></div>';

  function pad2(n) { return (n < 10 ? '0' : '') + n; }
  function whenLabel(ts) {
    if (Date.now() - ts < 60 * 1000) return i18n.t('tx.justNow');
    var d = new Date(ts), now = new Date();
    var time = pad2(d.getHours()) + ':' + pad2(d.getMinutes());
    var today = new Date(now.getFullYear(), now.getMonth(), now.getDate()).getTime();
    var yesterday = new Date(now.getFullYear(), now.getMonth(), now.getDate() - 1).getTime();
    if (ts >= today) return i18n.t('tx.today') + ', ' + time;
    if (ts >= yesterday) return i18n.t('tx.yesterday') + ', ' + time;
    var date;
    try { date = new Intl.DateTimeFormat(i18n.lang === 'en' ? 'en-GB' : 'hr-HR', { day: 'numeric', month: 'short' }).format(d); }
    catch (e) { date = d.getDate() + '. ' + (d.getMonth() + 1) + '.'; }
    return date + ', ' + time;
  }

  function txRow(t) {
    var row = document.createElement('div');
    row.className = 'tx';
    var aircash = t.kind === 'aircash';
    row.innerHTML = (aircash ? '<div class="logo aircash">' + AIRCASH + '</div>' : '<div class="logo apple">' + APPLE + '</div>') +
      '<div class="body"><div class="name"></div><div class="when"></div></div>' +
      '<div class="amt' + (t.amount > 0 ? ' pos' : '') + '"></div>';
    row.querySelector('.name').textContent = aircash ? 'aircash.eu' : i18n.t('tx.topup');
    row.querySelector('.when').textContent = whenLabel(t.ts);
    row.querySelector('.amt').textContent = (t.amount < 0 ? '−' : '+') + BankStore.formatAmount(t.amount) + ' €';
    return row;
  }

  function renderRows(container, list, before) {
    container.querySelectorAll('.tx, .tx-empty').forEach(function (r) { r.remove(); });
    list.forEach(function (t) { container.insertBefore(txRow(t), before || null); });
    addTxBadges(container);
  }

  // Balance scale: it follows the screen width (sizes are in rem, which scale with the phone) and
  // once the balance gets wider than ~62% of the column it shrinks smoothly so it always fits.
  var BAL_REM = 4.8, BAL_KEEP = 0.62, BAL_MIN = 0.4;
  function fitBalance(instant) {
    if (instant === true) balanceEl.style.transition = 'none';   // first paint / font load: no shrink animation
    var r = parseFloat(getComputedStyle(document.documentElement).fontSize), base = BAL_REM * r;
    var size = parseFloat(getComputedStyle(balanceEl).fontSize) || base;   // may be mid-transition
    var w = balanceInt.offsetWidth + balanceCur.offsetWidth + (parseFloat(getComputedStyle(balanceCur).marginLeft) || 0);
    var natural = w * base / size;                                         // width at full size
    var room = balanceEl.clientWidth;
    var target = Math.min(room * BAL_KEEP, room - 3.2 * r);
    var scale = natural > target ? Math.max(BAL_MIN, target / natural) : 1;
    balanceEl.style.setProperty('--bal-size', (base * scale).toFixed(2) + 'px');
    if (instant === true) { void balanceEl.offsetWidth; balanceEl.style.transition = ''; }
  }

  var firstRender = true;
  function renderAccount() {
    var s = BankStore.load();
    s.tx = s.tx.slice().sort(function (a, b) { return b.ts - a.ts; });   // newest first, always
    balanceInt.textContent = (s.balance < 0 ? '−' : '') + BankStore.formatAmount(s.balance);
    fitBalance(firstRender);
    firstRender = false;
    renderRows(feed, s.tx.slice(0, HOME_ROWS), seeAll);
    seeAll.hidden = s.tx.length === 0;
    renderRows(txList, s.tx);
    if (!s.tx.length) {
      var empty = document.createElement('p');
      empty.className = 'tx-empty';
      empty.textContent = i18n.t('all.empty');
      txList.appendChild(empty);
    }
  }

  seeAll.addEventListener('click', function () { renderAccount(); open(txSheet); });
  document.getElementById('addMoney').addEventListener('click', function () {
    try { sessionStorage.setItem('addmoney.from', 'home'); } catch (e) {}
    PageTransition.go('fwd', function () { location.href = 'add-money.html'; });
  });
  i18n.onChange(renderAccount);
  window.addEventListener('pageshow', function (e) { if (e.persisted) renderAccount(); }); // back from add money
  window.addEventListener('storage', function (e) { if (e.key === BankStore.KEY) renderAccount(); });
  window.addEventListener('resize', fitBalance);
  setInterval(function () { if (!document.hidden) renderAccount(); }, 30000); // keeps "a few moments ago" fresh
  if (document.fonts) document.fonts.ready.then(function () { fitBalance(true); });
  renderAccount();
})();
