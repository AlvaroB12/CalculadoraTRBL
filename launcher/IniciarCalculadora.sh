#!/bin/bash
# Script para lanzar la Calculadora Científica en Linux/Mac
# Ejecuta: chmod +x iniciar_calculadora.sh
# Luego: ./iniciar_calculadora.sh

cd "$(dirname "$0")/.."
python3 main.py
 