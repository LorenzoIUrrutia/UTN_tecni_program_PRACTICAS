#!/bin/bash

clave=""

until [ "$clave" = "secreto" ]
do
    read -sp "Ingrese la contraseña: " clave
    echo  # salto de línea después de la entrada oculta
done

echo "¡Contraseña correcta!"
