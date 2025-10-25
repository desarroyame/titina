Este repositorio explora el desafío de lograr que un agente de inteligencia artificial pronuncie, sin interrupciones, una palabra extremadamente larga. Esta tarea —en apariencia simple— revela los límites de diseño y control en modelos conversacionales como ChatGPT, que tienden a “resistirse” a ejecutar instrucciones poco comunes o fuera de contexto.

Para abordar el reto, se utiliza **Python** con el objetivo de **generar y reproducir el audio de la palabra más larga del mundo**: el nombre químico completo de la proteína **Titin**.

### Funcionalidades principales

* **Generación de palabras:** divide el nombre químico de la Titina en componentes individuales.
  *(Archivos: `split.py`, `generate_words.py`)*

* **Síntesis de voz:** convierte cada componente en audio mediante un motor de Text-to-Speech.
  *(Archivo: `tts.py`)*

* **Reproducción:** concatena los audios generados para reproducir el nombre completo.
  *(Archivo: `play_titin.py`)*

* **Estimación de tiempo:** calcula la duración total del audio resultante.
  *(Archivo: `estimate_time.py`)*

El proyecto almacena el nombre químico completo en `titin_chemical_name.txt`, genera las palabras individuales en `titin_words.txt` y guarda los archivos de audio de cada componente en el directorio `audio_words/`.

