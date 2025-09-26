# Actividad 1 
# Programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# Incluyendo ambos extremos, en orden creciente, mostrando un número por línea.

contador = 0

for contador in range(1, 101):
    print(contador)
    
# --- IGNORE ---

# Actividad 2 
# Programa que solicite al usuario un número entero
# Determine la cantidad de dígitos que contiene.

num_1 = 0 

num_1 = input("Ingrese el numero del cual quiera saber sus digitos")
print(f"El numero ingresado tiene {len(num_1)} digitos")

# --- IGNORE ---

# Actividad 3
# Programa que sume todos los números enteros entre dos valores
# Dados por el usuario, excluyendo esos dos valores.

num_1 = int(input("Ingrese el 1 numero de la lista"))
num_2 = int(input("Ingrese el 2 numero de la lista"))

maximo = max(num_1, num_2)
minimo = min(num_1, num_2)
sumatoria = 0


for contador in range((minimo + 1), (maximo)):
    sumatoria += contador
    
print(f"""
    Ha ingresado el {num_1} y el {num_2}.
    La suma de todos sus enteros es {sumatoria}.
""")

# --- IGNORE ---

# Actividad 4
# Programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

num_by_us = 0
contador = 1
sumatoria = 0 

print("Ingrese los numeros de desee sumar, para finalizar ingrese 0.\n")

print(f"Ingrese el {contador} numero diferente de 0.")
num_by_us = int(input())
print(f"{num_by_us} + {sumatoria} = {num_by_us + sumatoria}")

while num_by_us != 0:
    sumatoria += num_by_us
    contador += 1
    print(f"Ingrese el {contador} numero diferente de 0.")
    num_by_us = int(input())
    if num_by_us == 0:
        print(f"\nEl resultado final de la suamtoria de numeros es: {sumatoria}.")
        break
    
    print(f"{sumatoria} + {num_by_us} = {num_by_us + sumatoria}")

# --- IGNORE ---

# Actividad 5 
# Juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

num_by_us = 0
contador = 1
num_aleatorio = random.randint(0, 9)

print("Ingrese un numero entre el 0 y 9")
num_by_us = int(input())

while num_by_us >= 0 and num_by_us <= 9: 
    while num_by_us != num_aleatorio: 
        print(f"INCORRECTO, intento numero {contador}, ingrese otro numero entre el 0 y 9")
        contador += 1
        num_by_us = int(input())
    if num_by_us == num_aleatorio:
        print(f"Felicidades ha adivinado en su intento {contador}... el numero aleatorio es {num_aleatorio}")
        break

print(f"Ha acertado en {contador} intentos")

# --- IGNORE ---

# Actividad 6
# Programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for contador in range(100, -1, -2):
    print(contador)
    
# --- IGNORE ---

# Actividad 7 
# Programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo x usuario.

sumatoria = 0 
num_by_us = 0 


print("Ingrese un numero entero positivo")
num_by_us = int(input())

for contador in range(0, (num_by_us + 1)):
    sumatoria = sumatoria + contador
print(f"La suma de todos los números entre 0 y {num_by_us} es: {sumatoria}")

# --- IGNORE ---

# Actividad 8 
# Programa que permita al usuario ingresar 100 números enteros. 
# Debe indicar cuántos de estos números son pares, impares, negativos y cuántos son positivos. 

num_by_us = 0 
acum_positivo = 0
acum_negativo =0
acum_par = 0
acum_impar = 0
acum_cero = 0
contador = 1


for contador in range(1, 101):
    print(f"Ingrese su {contador}º numero entero")
    num_by_us = int(input())
    print(f"Ha ingresado el numero {num_by_us} \n")
    contador += 1
    
    if num_by_us == 0:
        acum_cero += 1
    elif num_by_us > 0:
        acum_positivo += 1 
    elif num_by_us < 0:
        acum_negativo += 1

    if (num_by_us != 0) and (num_by_us % 2 == 0):
        acum_par += 1
    elif (num_by_us != 0) and (num_by_us % 2 != 0):
        acum_impar += 1

print(f"Total de números positivos: {acum_positivo}")
print(f"Total de números negativos: {acum_negativo}")
print(f"Total de números pares: {acum_par}")
print(f"Total de números impares: {acum_impar}")
print(f"Total de veces que coloco el cero: {acum_cero}")

# --- IGNORE ---

# Actividad 9 
# Programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.

num_by_us = 0 
acumulador = 0
contador = 0
rango = 100 # Cambiar al rango que se desee llegar


for contador in range(1, (rango + 1)):
    print(f"Ingrese su {contador}º numero entero")
    num_by_us = int(input())
    acumulador = acumulador + num_by_us
    print(f"Ha ingresado el numero {num_by_us} \n")
    contador += 1

media = acumulador / rango

print(f"La suma de todos los numeros es {acumulador}, la media es {media}")

# --- IGNORE ---

# Actividad 10
# Programa que invierta el orden de los dígitos de un número ingresado por el usuario.

num_by_us = " "

print("Ingrese el numero que desee invertir")
num_by_us = input()

print(f"El numero ingresado es {num_by_us}, su inverso es {num_by_us[::-1]}")

# --- IGNORE ---