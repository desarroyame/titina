# Cómo ejecutar: 
#   python3 play_titin.py                    # Reproduce todo
#   python3 play_titin.py --first 100        # Primeras 100 palabras
#   python3 play_titin.py --last 50          # Últimas 50 palabras
#   python3 play_titin.py --range 100 200    # Palabras de la 100 a la 200

import pygame
import time
import os
import sys
import argparse

# Parsear argumentos
parser = argparse.ArgumentParser(description='Reproduce la secuencia de titin en audio')
parser.add_argument('--first', type=int, help='Reproducir solo las primeras N palabras')
parser.add_argument('--last', type=int, help='Reproducir solo las últimas N palabras')
parser.add_argument('--range', nargs=2, type=int, metavar=('START', 'END'), 
                    help='Reproducir palabras desde START hasta END')
parser.add_argument('--no-gap', action='store_true', 
                    help='Eliminar silencios entre palabras (reproducción continua)')
args = parser.parse_args()

# Inicializar pygame mixer con configuración optimizada
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

# Cargar palabras
if not os.path.exists('titin_words.txt'):
    print("ERROR: titin_words.txt no encontrado")
    sys.exit(1)

with open('titin_words.txt', 'r', encoding='utf-8') as f:
    all_words = f.read().split()

# Seleccionar rango de palabras según parámetros
if args.first:
    words = all_words[:args.first]
    print(f"Modo: Primeras {args.first} palabras")
elif args.last:
    words = all_words[-args.last:]
    print(f"Modo: Últimas {args.last} palabras")
elif args.range:
    start, end = args.range
    words = all_words[start-1:end]  # -1 porque el usuario usa índice base 1
    print(f"Modo: Palabras {start} a {end}")
else:
    words = all_words
    print(f"Modo: Secuencia completa")

total_words = len(all_words)
selected_words = len(words)

print(f"Total de palabras en archivo: {total_words}")
print(f"Palabras a reproducir: {selected_words}")
print(f"Primeras 10: {' '.join(words[:10])}")

# Verificar directorio de audio
if not os.path.exists('audio_words'):
    print("\nERROR: Directorio audio_words/ no encontrado")
    print("Ejecuta primero: python3 generate_words.py")
    sys.exit(1)

print(f"Archivos de audio disponibles: {len(os.listdir('audio_words'))}")
print(f"\nIniciando reproducción...\n")
if args.no_gap:
    print("Modo: Reproducción continua (sin silencios entre palabras)")

start_time = time.time()

# Modo sin silencios: usar Sound en lugar de music para mejor control
if args.no_gap:
    for i, word in enumerate(words, 1):
        audio_file = f"audio_words/{word}.mp3"
        
        if not os.path.exists(audio_file):
            print(f"[{i}/{selected_words}] Advertencia: {word}.mp3 no encontrado")
            continue
        
        # Mostrar progreso cada 100 palabras o en las primeras 10
        if i % 100 == 0 or i <= 10 or i == selected_words:
            elapsed = time.time() - start_time
            progress = (i / selected_words) * 100
            print(f"[{i}/{selected_words}] ({progress:.1f}%) - {word} - Tiempo: {elapsed:.1f}s", flush=True)
        
        # Reproducir audio sin gaps
        try:
            sound = pygame.mixer.Sound(audio_file)
            channel = sound.play()
            # Esperar solo hasta que termine, sin delay adicional
            while channel.get_busy():
                pygame.time.wait(1)  # Espera mínima de 1ms
        except Exception as e:
            print(f"[{i}/{selected_words}] Error reproduciendo {word}: {e}", flush=True)
else:
    # Modo normal con pequeños silencios
    for i, word in enumerate(words, 1):
        audio_file = f"audio_words/{word}.mp3"
        
        if not os.path.exists(audio_file):
            print(f"[{i}/{selected_words}] Advertencia: {word}.mp3 no encontrado")
            continue
        
        # Mostrar progreso cada 100 palabras o en las primeras 10
        if i % 100 == 0 or i <= 10 or i == selected_words:
            elapsed = time.time() - start_time
            progress = (i / selected_words) * 100
            print(f"[{i}/{selected_words}] ({progress:.1f}%) - {word} - Tiempo: {elapsed:.1f}s", flush=True)
        
        # Reproducir audio
        try:
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            
            # Esperar a que termine
            while pygame.mixer.music.get_busy():
                time.sleep(0.01)
        except Exception as e:
            print(f"[{i}/{selected_words}] Error reproduciendo {word}: {e}", flush=True)

total_time = time.time() - start_time
print(f"\n¡Reproducción completada!")
print(f"Tiempo total: {total_time:.1f} segundos ({total_time/60:.1f} minutos)")
