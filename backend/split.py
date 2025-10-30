# Cómo ejecutar: python split.py

import re

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

with open('titin_chemical_name.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Crear patrón regex con todos los nombres de aminoácidos + "titin"
words = list(set(amino_acids.values())) + ['titin']
pattern = '|'.join(sorted(words, key=len, reverse=True))  # Ordenar por longitud para evitar coincidencias parciales

# Separar en palabras
result = re.findall(pattern, text)

print(f"Total de palabras encontradas: {len(result)}")
print(f"Primeras 20 palabras: {' '.join(result[:20])}")
print(f"Últimas 5 palabras: {' '.join(result[-5:])}")

# Guardar resultado separado por espacios
with open('titin_words.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(result))

print("\nResultado guardado en 'titin_words.txt'")
