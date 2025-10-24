# Cómo ejecutar: python3 generate_words.py
# (Asegúrate de tener instalado: pip install elevenlabs python-dotenv)

import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save

load_dotenv()

amino_acids = {
    'A': 'alanyl',
    'R': 'arginyl',
    'N': 'asparaginyl',
    'D': 'aspartyl',
    'C': 'cysteinyl',
    'E': 'glutamyl',
    'Q': 'glutaminyl',
    'G': 'glycyl',
    'H': 'histidyl',
    'I': 'isoleucyl',
    'L': 'leucyl',
    'K': 'lysyl',
    'M': 'methionyl',
    'F': 'phenylalanyl',
    'P': 'prolyl',
    'S': 'seryl',
    'T': 'threonyl',
    'W': 'tryptophanyl',
    'Y': 'tyrosyl',
    'V': 'valyl'
}

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Crear directorio para los audios
os.makedirs('audio_words', exist_ok=True)

# Generar audio para cada palabra única
words = list(set(amino_acids.values())) + ['titin']
total = len(words)

print(f"Generando audio para {total} palabras únicas...\n")

for i, word in enumerate(words, 1):
    filename = f"audio_words/{word}.mp3"
    
    if os.path.exists(filename):
        print(f"[{i}/{total}] {word} - Ya existe, omitiendo")
        continue
    
    try:
        print(f"[{i}/{total}] Generando: {word}...", end=" ")
        
        audio = client.text_to_speech.convert(
            text=word,
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        
        save(audio, filename)
        print("✓")
        
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n¡Generación completada!")
