#!/bin/bash

# Definición de variables
read -p "Ingrese el primer numero: " num1
read -p "Ingrese el segundo numero: " num2

# Operaciones
suma=$((num1 + num2))
resta=$((num1 - num2))
multiplicacion=$((num1 * num2))
division=$((num1 / num2))

# Mostrar resultados
echo "Número 1: $num1"
echo "Número 2: $num2"
echo "Suma: $suma"
echo "Resta: $resta"
echo "Multiplicación: $multiplicacion"
echo "División: $division"
