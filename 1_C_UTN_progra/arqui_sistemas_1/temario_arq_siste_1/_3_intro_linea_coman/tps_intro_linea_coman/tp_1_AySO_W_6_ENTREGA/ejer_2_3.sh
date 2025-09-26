#!/bin/bash
# Script que define variables de texto y las muestra concatenadas

# Definir variables
read -p "Ingrese su nombre: " nombre
read -p "Ingrese su edad: " edad
read -p "Ingrese su ciudad: " ciudad

# Mostrar mensaje concatenado
echo "Hola, me llamo $nombre, tengo $edad años y vivo en $ciudad."