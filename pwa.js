// Registers the service worker so the app is installable and works offline.
// Guarded so it does nothing when opened from file:// (service workers need http/https or localhost).
(function () {
  if (!('serviceWorker' in navigator)) return;
  if (location.protocol !== 'https:' && location.hostname !== 'localhost' && location.hostname !== '127.0.0.1') return;
  window.addEventListener('load', function () {
    navigator.serviceWorker.register('sw.js').catch(function () { /* ignore: app still runs online */ });
  });
})();
