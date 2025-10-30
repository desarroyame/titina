// Service Worker for Titin Visualizer
// Caches all audio files for offline use and faster performance

const CACHE_NAME = 'titin-audio-cache-v1';
const AUDIO_FILES = [
  '/audio_words/alanyl.mp3',
  '/audio_words/arginyl.mp3',
  '/audio_words/asparaginyl.mp3',
  '/audio_words/aspartyl.mp3',
  '/audio_words/cysteinyl.mp3',
  '/audio_words/glutaminyl.mp3',
  '/audio_words/glutamyl.mp3',
  '/audio_words/glycyl.mp3',
  '/audio_words/histidyl.mp3',
  '/audio_words/isoleucyl.mp3',
  '/audio_words/leucyl.mp3',
  '/audio_words/lysyl.mp3',
  '/audio_words/methionyl.mp3',
  '/audio_words/phenylalanyl.mp3',
  '/audio_words/prolyl.mp3',
  '/audio_words/seryl.mp3',
  '/audio_words/threonyl.mp3',
  '/audio_words/tryptophanyl.mp3',
  '/audio_words/tyrosyl.mp3',
  '/audio_words/valyl.mp3',
  '/titin_chemical_name.txt'
];

// Install event - cache all audio files
self.addEventListener('install', (event) => {

  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {

        return cache.addAll(AUDIO_FILES);
      })
      .then(() => {

        return self.skipWaiting(); // Activate immediately
      })
      .catch((error) => {

      })
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
  console.log('[Service Worker] Activating...');
  event.waitUntil(
    caches.keys()
      .then((cacheNames) => {
        return Promise.all(
          cacheNames.map((cacheName) => {
            if (cacheName !== CACHE_NAME) {

              return caches.delete(cacheName);
            }
          })
        );
      })
      .then(() => {

        return self.clients.claim(); // Take control immediately
      })
  );
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
  // Only handle audio files and titin text file
  const url = new URL(event.request.url);
  const isAudioOrText = 
    url.pathname.startsWith('/audio_words/') || 
    url.pathname === '/titin_chemical_name.txt';

  if (isAudioOrText) {
    event.respondWith(
      caches.match(event.request)
        .then((response) => {
          if (response) {
            // Cache hit - return cached version
            return response;
          }
          
          // Cache miss - fetch from network and cache it

          return fetch(event.request)
            .then((response) => {
              // Clone the response before caching
              const responseToCache = response.clone();
              
              caches.open(CACHE_NAME)
                .then((cache) => {
                  cache.put(event.request, responseToCache);
                });
              
              return response;
            });
        })
        .catch(() => {
          throw new Error('Fetch failed');
        })
    );
  }
  // For non-audio/text files, just fetch normally
});

// Message event - for manual cache updates
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
  
  if (event.data && event.data.type === 'CLEAR_CACHE') {
    event.waitUntil(
      caches.delete(CACHE_NAME)
        .then(() => {

          return self.clients.matchAll();
        })
        .then((clients) => {
          clients.forEach((client) => {
            client.postMessage({ type: 'CACHE_CLEARED' });
          });
        })
    );
  }
});
