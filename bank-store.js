// Shared account state for the home screen (home.html) and the add-money screen (add-money.html).
// Kept in localStorage; amounts are whole cents so there are no rounding errors.
var BankStore = (function () {
  var KEY = 'bank.state';
  var MAX_TX = 1000; // every transaction is kept (capped at 1000 only so storage can't overflow)

  // First run: the two transactions from the original screenshot (+10 € then −10 €, balance 0 €),
  // dated today at 00:44 / 00:46 (or yesterday if it isn't 00:46 yet).
  function seed() {
    var day = new Date(); day.setHours(0, 46, 0, 0);
    if (day.getTime() > Date.now()) day.setDate(day.getDate() - 1);
    var t46 = day.getTime(), t44 = t46 - 2 * 60 * 1000;
    return {
      balance: 0,
      tx: [
        { id: 'seed-aircash', kind: 'aircash', amount: -1000, ts: t46 },
        { id: 'seed-topup', kind: 'topup', amount: 1000, ts: t44 }
      ]
    };
  }

  function valid(s) {
    return s && typeof s.balance === 'number' && isFinite(s.balance) && Array.isArray(s.tx) &&
      s.tx.every(function (t) { return t && typeof t.amount === 'number' && typeof t.ts === 'number' && typeof t.kind === 'string'; });
  }

  function load() {
    try {
      var s = JSON.parse(localStorage.getItem(KEY));
      if (valid(s)) return s;
    } catch (e) {}
    return seed();
  }

  function save(s) {
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { /* storage blocked: lasts until reload */ }
  }

  // Money added with Apple Pay: newest first, balance goes up by the same amount.
  function addTopUp(cents) {
    cents = Math.round(cents);
    if (!(cents > 0)) return load();
    var s = load();
    s.tx.unshift({ id: 'tx-' + Date.now(), kind: 'topup', amount: cents, ts: Date.now() });
    s.tx = s.tx.slice(0, MAX_TX);
    s.balance += cents;
    save(s);
    return s;
  }

  function reset() {
    try { localStorage.removeItem(KEY); } catch (e) {}
  }

  // 1000 -> "10", 1250 -> "12,50", 123456789 -> "1 234 567,89" (thin-space thousands)
  function formatAmount(cents) {
    var abs = Math.abs(Math.round(cents));
    var whole = String(Math.floor(abs / 100)).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    var rest = abs % 100;
    return whole + (rest ? ',' + (rest < 10 ? '0' : '') + rest : '');
  }

  return { KEY: KEY, MAX_TX: MAX_TX, load: load, addTopUp: addTopUp, reset: reset, formatAmount: formatAmount };
})();
