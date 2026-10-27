// Service worker: makes the app installable and work offline.
// App-shell cache: precache everything on install, serve cache-first, fall back to the network.
// Bump CACHE whenever a file changes so clients pick up the new version.
var CACHE = 'revolut-pwa-v3';

var ASSETS = [
  './',
  'index.html',
  'add-money.html',
  'styles.css',
  'add-money.css',
  'page-transition.js',
  'bank-store.js',
  'app.js',
  'add-money.js',
  'manifest.json',
  '_build/fonts/inter-var.ttf',
  'assets/aircash-card.png',
  'icons/icon-192.png',
  'icons/icon-512.png',
  'icons/icon-maskable-512.png',
  'icons/apple-touch-icon-180.png'
];

self.addEventListener('install', function (e) {
  self.skipWaiting();
  e.waitUntil(
    caches.open(CACHE).then(function (c) {
      // add one by one so a single 404 can't fail the whole install
      return Promise.all(ASSETS.map(function (url) {
        return fetch(url, { cache: 'reload' }).then(function (res) {
          if (res && (res.ok || res.type === 'opaque')) return c.put(url, res);
        }).catch(function () {});
      }));
    })
  );
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (k) { return k === CACHE ? null : caches.delete(k); }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') return;
  var url = new URL(req.url);
  if (url.origin !== self.location.origin) return;   // leave cross-origin requests alone

  e.respondWith(
    caches.match(req, { ignoreSearch: true }).then(function (hit) {
      if (hit) return hit;
      return fetch(req).then(function (res) {
        if (res && res.ok && res.type === 'basic') {
          var copy = res.clone();
          caches.open(CACHE).then(function (c) { c.put(req, copy); });
        }
        return res;
      }).catch(function () {
        // offline and not cached: for a page navigation, fall back to home
        if (req.mode === 'navigate') return caches.match('index.html');
      });
    })
  );
});
