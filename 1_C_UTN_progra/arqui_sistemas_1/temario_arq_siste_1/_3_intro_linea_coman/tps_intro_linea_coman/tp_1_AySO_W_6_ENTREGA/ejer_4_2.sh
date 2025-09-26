#!/bin/bash

i=1
suma=0

while [ $i -le 100 ]
do
    suma=$((suma + i))
    i=$((i + 1))
done

echo "La suma de los números del 1 al 100 es: $suma"
