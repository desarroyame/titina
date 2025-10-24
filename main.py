# Cómo ejecutar: python main.py
# (Asegúrate de tener instalado requests: pip install requests)

import requests
import re

# Lista de los 20 aminoácidos estándar en inglés y sufijo -yl
amino_acids = {
    'A': 'alanyl',     # Alanine
    'R': 'arginyl',    # Arginine
    'N': 'asparaginyl',# Asparagine
    'D': 'aspartyl',   # Aspartic acid
    'C': 'cysteinyl',  # Cysteine
    'E': 'glutamyl',   # Glutamic acid
    'Q': 'glutaminyl', # Glutamine
    'G': 'glycyl',     # Glycine
    'H': 'histidyl',   # Histidine
    'I': 'isoleucyl',  # Isoleucine
    'L': 'leucyl',     # Leucine
    'K': 'lysyl',      # Lysine
    'M': 'methionyl',  # Methionine
    'F': 'phenylalanyl',# Phenylalanine
    'P': 'prolyl',     # Proline
    'S': 'seryl',      # Serine
    'T': 'threonyl',   # Threonine
    'W': 'tryptophanyl',# Tryptophan
    'Y': 'tyrosyl',    # Tyrosine
    'V': 'valyl'       # Valine
}

def download_titin_sequence():
    """
    Descarga la secuencia de titina desde UniProtKB y extrae solo la secuencia de aminoácidos.
    """
    url = "https://rest.uniprot.org/uniprotkb/Q8WZ42.fasta"
    
    try:
        print("Descargando secuencia de titina desde UniProtKB...")
        response = requests.get(url)
        response.raise_for_status()  # Lanza excepción si hay error HTTP
        
        fasta_content = response.text
        print("Descarga completada exitosamente!")
        
        # Procesa el contenido FASTA
        lines = fasta_content.strip().split('\n')
        
        # La primera línea es el encabezado (comienza con >)
        if not lines[0].startswith('>'):
            raise ValueError("El formato FASTA no es válido")
        
        print(f"Encabezado: {lines[0]}")
        
        # Las líneas restantes contienen la secuencia
        sequence = ''.join(lines[1:])
        
        # Limpia la secuencia: solo caracteres válidos de aminoácidos
        sequence = re.sub(r'[^ACDEFGHIKLMNPQRSTVWY]', '', sequence.upper())
        
        print(f"Longitud de la secuencia: {len(sequence)} aminoácidos")
        
        return sequence
        
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la secuencia: {e}")
        return None
    except Exception as e:
        print(f"Error al procesar la secuencia: {e}")
        return None

# Descarga la secuencia oficial de titina
sequence = download_titin_sequence()

if sequence is None:
    print("No se pudo obtener la secuencia. Usando secuencia de ejemplo.")
    sequence = 'MST'  # Secuencia de respaldo para pruebas

# Construye el nombre químico
print("Construyendo el nombre químico de la titina...")
chemical_name = ""
total_aa = len(sequence)

for i, aa in enumerate(sequence):
    if aa in amino_acids:
        chemical_name += amino_acids[aa]
        
        # Muestra progreso cada 1000 aminoácidos
        if (i + 1) % 1000 == 0:
            progress = ((i + 1) / total_aa) * 100
            print(f"Progreso: {i + 1}/{total_aa} aminoácidos ({progress:.1f}%)")
    else:
        print(f"Advertencia: Aminoácido desconocido '{aa}' en posición {i + 1}")
        # Continúa sin añadir nada para aminoácidos desconocidos

chemical_name += "titin"  # Así termina la nomenclatura de la proteína titina
print("¡Nombre químico completado!")

# Guarda el resultado en un archivo de texto
print("Guardando resultado en 'titin_chemical_name.txt'...")
with open('titin_chemical_name.txt', 'w', encoding='utf-8') as file:
    file.write(chemical_name)

print(f"Archivo guardado exitosamente!")
print(f"Longitud del nombre químico: {len(chemical_name)} caracteres")

# Imprime los primeros 500 caracteres como muestra
print("\nPrimeros 500 caracteres del nombre químico:")
print(chemical_name[:500] + "...")

# Imprime los últimos 20 caracteres para confirmar que termina en "titin"
print(f"\nÚltimos 20 caracteres: ...{chemical_name[-20:]}")
