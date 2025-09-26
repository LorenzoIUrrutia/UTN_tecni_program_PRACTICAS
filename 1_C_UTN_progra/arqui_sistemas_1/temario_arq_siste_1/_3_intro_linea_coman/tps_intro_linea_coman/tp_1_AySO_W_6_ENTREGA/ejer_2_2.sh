#!/bin/bash

# Definición de variables
read -p "Ingrese la base: " base
read -p "Ingrese la altura: " altura

# Calcular área (base * altura)
area=$((base * altura))

# Mostrar resultados
echo "Base: $base"
echo "Altura: $altura"
echo "El área del rectángulo es: $area"