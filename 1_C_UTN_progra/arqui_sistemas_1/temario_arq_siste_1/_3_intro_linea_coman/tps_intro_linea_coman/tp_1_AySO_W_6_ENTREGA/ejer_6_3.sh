#!/bin/bash
# Script que calcula el promedio de 5 números usando un bucle for

suma=0

echo "Ingrese 5 números:"

for i in {1..5}
do
    read -p "Número $i: " num
    suma=$((suma + num))
done

promedio=$((suma / 5))

echo "La suma de los números es: $suma"
echo "El promedio es: $promedio"
