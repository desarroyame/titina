#!/bin/bash

# Script para activar el entorno virtual y ejecutar el proyecto de titina

echo "🧬 Activando entorno virtual de Python para el proyecto Titina..."

# Verificar si el entorno virtual existe
if [ ! -d "venv" ]; then
    echo "❌ Error: No se encontró el entorno virtual."
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
    echo "✅ Entorno virtual creado."
fi

# Activar el entorno virtual
source venv/bin/activate

# Verificar si requirements.txt existe e instalar dependencias
if [ -f "requirements.txt" ]; then
    echo "📋 Instalando dependencias..."
    pip install -r requirements.txt --quiet
    echo "✅ Dependencias instaladas."
else
    echo "⚠️  Advertencia: No se encontró requirements.txt"
fi

echo "🚀 Entorno listo. Puedes ejecutar:"
echo "   python main.py"
echo ""
echo "💡 Para desactivar el entorno virtual, ejecuta: deactivate"
