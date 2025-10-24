# Cómo ejecutar: python3 tts.py
# (Asegúrate de tener instalado: pip install elevenlabs python-dotenv)

import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
print(f"API Key cargada: {api_key[:10]}..." if api_key else "ERROR: No se encontró API key")

client = ElevenLabs(api_key=api_key)

print("\nLeyendo titin_words.txt...")
with open('titin_words.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Total de caracteres: {len(text)}")

# Limitar a los primeros 5000 caracteres para prueba
text_sample = text[:5000]
print(f"Usando muestra de: {len(text_sample)} caracteres para prueba")
print(f"Primeras palabras: {' '.join(text_sample.split()[:10])}...")

print("\nGenerando audio con ElevenLabs...")

try:
    audio = client.text_to_speech.convert(
        text=text_sample,
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )

    print("Guardando audio en 'titin_audio_sample.mp3'...")
    save(audio, 'titin_audio_sample.mp3')

    print("¡Audio generado exitosamente!")
    
except Exception as e:
    print(f"\nError: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    
    if hasattr(e, 'status_code'):
        print(f"Status code: {e.status_code}")
    if hasattr(e, 'body'):
        print(f"Body: {e.body}")
