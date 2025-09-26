#!/bin/bash

# Pedir al usuario su edad
read -p "Ingrese su edad: " edad

# Evaluar si es mayor o menor de edad
if [ $edad -ge 18 ]; then
    echo "Usted es mayor de edad."
else
    echo "Usted es menor de edad."
fi
