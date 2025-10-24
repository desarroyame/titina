# Cómo ejecutar: python3 estimate_time.py

import os
import sys

# Evitar output de pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

import pygame
import time

amino_acids_words = [
    'alanyl', 'arginyl', 'asparaginyl', 'aspartyl', 'cysteinyl',
    'glutamyl', 'glutaminyl', 'glycyl', 'histidyl', 'isoleucyl',
    'leucyl', 'lysyl', 'methionyl', 'phenylalanyl', 'prolyl',
    'seryl', 'threonyl', 'tryptophanyl', 'tyrosyl', 'valyl', 'titin'
]

# Inicializar pygame
pygame.mixer.init()

print("Midiendo duración de cada palabra...\n")

durations = {}
total_duration = 0

for word in amino_acids_words:
    audio_file = f"audio_words/{word}.mp3"
    
    if not os.path.exists(audio_file):
        print(f"Advertencia: {word}.mp3 no encontrado")
        continue
    
    # Cargar y medir duración
    sound = pygame.mixer.Sound(audio_file)
    duration = sound.get_length()
    durations[word] = duration
    total_duration += duration
    
    print(f"{word:15} - {duration:.2f}s")

avg_duration = total_duration / len(durations)
print(f"\n{'='*40}")
print(f"Duración promedio por palabra: {avg_duration:.2f}s")
print(f"{'='*40}\n")

# Leer titin_words.txt
with open('titin_words.txt', 'r', encoding='utf-8') as f:
    words = f.read().split()

total_words = len(words)

# Calcular tiempo estimado basado en frecuencia de cada palabra
estimated_time = 0
word_count = {}

for word in words:
    if word in durations:
        estimated_time += durations[word]
        word_count[word] = word_count.get(word, 0) + 1

# Estimación simple con promedio
simple_estimate = total_words * avg_duration

print(f"Total de palabras en titin_words.txt: {total_words:,}")
print(f"\nEstimación SIMPLE (promedio): {simple_estimate:.1f}s")
print(f"  = {simple_estimate/60:.1f} minutos")
print(f"  = {simple_estimate/3600:.2f} horas")

print(f"\nEstimación PRECISA (por frecuencia): {estimated_time:.1f}s")
print(f"  = {estimated_time/60:.1f} minutos")
print(f"  = {estimated_time/3600:.2f} horas")

print(f"\n{'='*40}")
print("Palabras más frecuentes:")
print(f"{'='*40}")
sorted_counts = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_counts[:5]:
    print(f"{word:15} - {count:,} veces ({count/total_words*100:.1f}%)")
