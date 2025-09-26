#!/bin/bash

# Crear la carpeta backup si no existe
mkdir -p backup
# Copiar todos los archivos .txt al directorio backup
cp *.txt backup/
echo "Archivos .txt copiados en el directorio backup/"
