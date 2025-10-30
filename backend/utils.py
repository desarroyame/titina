#!/usr/bin/env python3
"""
Script de utilidades para el proyecto Titina
Proporciona funciones adicionales para analizar el resultado generado
"""

import os
import sys

def analyze_chemical_name():
    """Analiza el archivo generado del nombre químico de titina"""
    filename = "titin_chemical_name.txt"
    
    if not os.path.exists(filename):
        print(f"❌ Error: El archivo {filename} no existe.")
        print("🔄 Ejecuta primero: python main.py")
        return
    
    print("🧬 ANÁLISIS DEL NOMBRE QUÍMICO DE TITINA")
    print("=" * 50)
    
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    print(f"📊 Longitud total: {len(content):,} caracteres")
    print(f"📁 Tamaño del archivo: {os.path.getsize(filename):,} bytes")
    
    # Contar sufijos de aminoácidos
    amino_suffixes = ['alanyl', 'arginyl', 'asparaginyl', 'aspartyl', 'cysteinyl', 
                     'glutamyl', 'glutaminyl', 'glycyl', 'histidyl', 'isoleucyl', 
                     'leucyl', 'lysyl', 'methionyl', 'phenylalanyl', 'prolyl', 
                     'seryl', 'threonyl', 'tryptophanyl', 'tyrosyl', 'valyl']
    
    total_amino_count = 0
    print("\n🔬 Frecuencia de aminoácidos:")
    for suffix in amino_suffixes:
        count = content.count(suffix)
        total_amino_count += count
        if count > 0:
            print(f"   {suffix:>15}: {count:>4}")
    
    print(f"\n📈 Total de aminoácidos procesados: {total_amino_count:,}")
    
    # Verificar que termina correctamente
    if content.endswith('titin'):
        print("✅ El nombre termina correctamente en 'titin'")
    else:
        print("⚠️  Advertencia: El nombre no termina en 'titin'")
    
    # Mostrar primeros y últimos caracteres
    print(f"\n📝 Primeros 100 caracteres:")
    print(f"   {content[:100]}...")
    print(f"\n📝 Últimos 50 caracteres:")
    print(f"   ...{content[-50:]}")

def show_help():
    """Muestra la ayuda del script"""
    print("🔧 UTILIDADES PARA EL PROYECTO TITINA")
    print("=" * 40)
    print("Uso: python utils.py <comando>")
    print("\nComandos disponibles:")
    print("  analyze    - Analizar el archivo del nombre químico")
    print("  help       - Mostrar esta ayuda")

def main():
    """Función principal del script de utilidades"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "analyze":
        analyze_chemical_name()
    elif command == "help":
        show_help()
    else:
        print(f"❌ Comando desconocido: {command}")
        print("💡 Usa 'python utils.py help' para ver los comandos disponibles")

if __name__ == "__main__":
    main()
