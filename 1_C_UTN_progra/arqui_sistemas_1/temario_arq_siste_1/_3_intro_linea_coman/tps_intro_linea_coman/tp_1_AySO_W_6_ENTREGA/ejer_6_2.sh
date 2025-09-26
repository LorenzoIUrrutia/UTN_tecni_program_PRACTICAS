#!/bin/bash
# Script que lee nombres desde un archivo y saluda a cada uno

archivo="nombres.txt"

# Verificar que el archivo existe
if [ -f "$archivo" ]; then
    while IFS= read -r nombre
    do
        echo "Hola, $nombre. ¡Bienvenido!"
    done < "$archivo"
else
    echo "El archivo $archivo no existe."
fi
