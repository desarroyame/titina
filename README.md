El propósito de este repositorio es abordar el reto de hacer que un  agente de IA pronuncie sin pausa una palabra larguísima, esta simple tarea pone en evidencia los límites de diseño y control en los modelos conversacionales como ChatGPT haciendo que modelo “se resista” a ejecutar una tarea, se aborda con Python para **generar y reproducir el audio de la palabra más larga del mundo**: el nombre químico completo de la proteína Titina.

## Funcionalidades principales:

- **Generación de palabras**: Divide el nombre químico de la Titina en componentes individuales (split.py, `generate_words.py`)
- **Síntesis de voz**: Convierte cada componente a audio usando Text-to-Speech (`tts.py`)
- **Reproducción**: Reproduce el nombre completo concatenando los audios generados (`play_titin.py`)
- **Estimación de tiempo**: Calcula la duración total del audio (`estimate_time.py`)

El proyecto almacena el nombre químico en titin_chemical_name.txt, genera palabras individuales en titin_words.txt, y guarda los archivos de audio de cada componente en el directorio audio_words.
