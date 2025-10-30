# Cache API Implementation

## ✅ Implementado

Este proyecto ahora usa **Cache API** con **Service Worker** para optimizar el rendimiento.

## 🚀 Beneficios

### Primera carga:
- Descarga los 21 archivos de audio únicos (~2-3MB total)
- Cachea automáticamente en el navegador

### Recargas posteriores:
- **Instantáneas** - los archivos se sirven desde caché
- **Sin descargas** - ahorra ancho de banda
- **Funciona offline** - puedes usar la app sin internet

## 📊 Archivos cacheados

El Service Worker cachea automáticamente:
- 21 archivos de audio MP3 (aminoácidos):
  - alanyl.mp3, arginyl.mp3, asparaginyl.mp3, aspartyl.mp3
  - cysteinyl.mp3, glutaminyl.mp3, glutamyl.mp3, glycyl.mp3
  - histidyl.mp3, isoleucyl.mp3, leucyl.mp3, lysyl.mp3
  - methionyl.mp3, phenylalanyl.mp3, prolyl.mp3, seryl.mp3
  - threonyl.mp3, tryptophanyl.mp3, tyrosyl.mp3, valyl.mp3
- titin_chemical_name.txt (secuencia completa)

## 🔍 Indicador visual

Cuando veas "● Cached" en verde en el header, significa que todos los archivos están cacheados y listos para uso offline.

## 🛠️ Desarrollo

Para ver el Service Worker en acción:

1. **Chrome DevTools**: Application > Service Workers
2. **Firefox DevTools**: Application > Service Workers
3. **Ver caché**: Application > Cache Storage > titin-audio-cache-v1

## 🧹 Limpiar caché

Si necesitas limpiar la caché:

```javascript
// En la consola del navegador
navigator.serviceWorker.controller.postMessage({ type: 'CLEAR_CACHE' });
```

O simplemente:
- Chrome: DevTools > Application > Clear storage
- Firefox: DevTools > Storage > Clear All

## 📈 Comparación de rendimiento

| Escenario | Sin Cache API | Con Cache API |
|-----------|---------------|---------------|
| Primera carga | ~2-3MB descarga | ~2-3MB descarga |
| Segunda carga | ~2-3MB descarga | 0 bytes (caché) |
| Offline | ❌ No funciona | ✅ Funciona |
| Latencia audio | ~50-200ms | ~5-10ms |

## 🔄 Actualizaciones

El Service Worker se actualiza automáticamente cuando:
- Cambias la versión del caché (`CACHE_NAME`)
- Modificas la lista de archivos
- Despliegas una nueva versión

## 💡 Notas técnicas

- **Estrategia**: Cache First, Network Fallback
- **Scope**: Solo archivos de audio y titin_chemical_name.txt
- **Versión actual**: v1
- **Compatible**: Todos los navegadores modernos
