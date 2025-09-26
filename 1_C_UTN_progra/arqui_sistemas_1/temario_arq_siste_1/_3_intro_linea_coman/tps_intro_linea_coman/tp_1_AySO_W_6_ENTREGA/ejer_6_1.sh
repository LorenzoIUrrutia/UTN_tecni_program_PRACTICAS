#!/bin/bash

# Pedir nombre
read -p "Ingrese su nombre: " nombre

# Pedir edad
read -p "Ingrese su edad: " edad

# Verificar si puede votar
if [ $edad -ge 16 ]; then
    echo "Hola $nombre, con $edad años SÍ puedes votar."
else
    echo "Hola $nombre, con $edad años NO puedes votar."
fi
