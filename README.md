Este repositorio explora el desafío de lograr que un agente de inteligencia artificial pronuncie, sin interrupciones, una palabra extremadamente larga. Esta tarea —en apariencia simple— revela los límites de diseño y control en modelos conversacionales como ChatGPT, que tienden a "resistirse" a ejecutar instrucciones poco comunes o fuera de contexto.

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

### Reproducción de audio

Para reproducir el audio del nombre químico de la Titina, utiliza el script `play_titin.py` con las siguientes opciones:

#### Reproducir el audio completo
```bash
python3 play_titin.py
```

#### Reproducir solo las primeras N palabras
```bash
python3 play_titin.py --first 100
```

#### Reproducir solo las últimas N palabras
```bash
python3 play_titin.py --last 50
```

#### Reproducir un rango específico de palabras
```bash
python3 play_titin.py --range 100 200
```
*(Reproduce desde la palabra 100 hasta la 200)*

#### Reproducir sin silencios entre palabras
```bash
python3 play_titin.py --no-gap
```
*(Reproducción continua, eliminando los silencios entre palabras)*

#### Combinar opciones
```bash
python3 play_titin.py --first 100 --no-gap
python3 play_titin.py --range 1 50 --no-gap
```
*(Puedes combinar --no-gap con --first, --last o --range)*

