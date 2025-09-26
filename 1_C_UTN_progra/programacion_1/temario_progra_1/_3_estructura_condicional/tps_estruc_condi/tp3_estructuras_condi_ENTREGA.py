# 1)Actividad 1
# Programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad_actual = int(input("Ingrese su edad actual"))

if (edad_actual >= 18):
    print("Es MAYOR de edad")
else:
    print("Es MENOR de edad")    
    
# Actividad 2
# Programa que solicite su nota al usuario. 
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”
# Caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Ingrese su nota"))

if (nota > 0) and (nota < 10):
    if (nota >= 6):
        print("APROBADO")
    else:
        print("DESAPROBADO")
else:
    print("Nota ingresada INCORRECTA")
    
# Actividad 3
# Programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"
# Caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 

num_1 = int(input("Ingrese un numero entero"))

if (num_1 % 2) == 0:
    print("El numero ingresado es PAR")
else:
    print("El numero ingresado el IMPAR")

# Actividad 4
# Programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edad_1 = int(input("Ingrese su edad actual"))

if edad_1 < 0:
    print("Ingrese una edad valida, mayor a 0")
elif edad_1 > 0 and edad_1 < 12:
    print("Niño/a") 
elif edad_1 > 0 and edad_1 >= 12 and edad_1 < 18:
    print("Adolescente")
elif edad_1 > 0 and edad_1 >= 18 and edad_1 < 30:
    print("Adulto/a joven")
elif edad_1 > 0 and edad_1 >= 30 and edad_1 < 65:
    print("Adulto/a")
else:
    print("Adulto/a mayor")

# Actividad 5
# Programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada
# Imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"
# Caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"

contra_1 = input("Ingrese una contraseña entre 8 y 14 caracteres")

print(f"Contraseña de  {len(contra_1)} caracteres")

if len(contra_1) < 8 or len(contra_1) > 14:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
else:
    print("Ha ingresado una contraseña correcta")

# Actividad 6
# Programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media 
# Las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. 
# Imprimir el resultado por pantalla

from statistics import mode, median, mean
import random

num_random = [random.randint(1, 100) for _ in range(50)]

if mean(num_random) > median(num_random) and median(num_random) > mode(num_random):
    print("Sesgo POSITIVO o sesgo a la DERECHA")
elif mean(num_random) < median(num_random) and median(num_random) < mode(num_random):
    print("Sesgo NEGATIVO o sesgo a la IZQUIERDA")
elif mean(num_random) == median(num_random) and median(num_random) == mode(num_random):
    print("Sin sesgo")
else:
    print("Distribución ASIMÉTRICA")

# Actividad 7 
# Programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal
# Añadir un signo de exclamación al final e imprimir el string resultante por pantalla
# Caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase_1 = input("Ingrese una frase o palabra")

if frase_1[-1] in "aeiouAEIOU":
    print(frase_1 + "!")
else:
    print(frase_1)

# Actividad 8
# Programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
nombre_1 = " "
num_1 = 0

nombre_1 = input("Ingrese su nombre")
print(f"Ha ingresado su nombre: {nombre_1}")

print(""" 
Ingrese 1 Si quiere su nombre en mayúsculas. \n
Ingrese 2 Si quiere su nombre en minúsculas. \n
Ingrese 3 Si quiere su nombre con la primera letra mayúscula.\n
     """)

num_1 = int(input("Ingrese una opcion (1, 2 o 3): "))
if num_1 == 1:
    print(f"Ha seleccionado la opcion {num_1} \n")
    print(nombre_1 .upper())
elif num_1 == 2:
    print(f"Ha seleccionado la opcion {num_1} \n")
    print(nombre_1 .lower())
elif num_1 == 3:
    print(f"Ha seleccionado la opcion {num_1} \n")
    print(nombre_1 .capitalize())

# Actividad 9 
# Programa que pida al usuario la magnitud de un terremoto
# Clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_1 = float(input("Ingrese la magnitud del terremoto en numeros")) 

if 3 > magnitud_1:
    print(""" "Muy leve" (imperceptible). """)
elif 3 >= magnitud_1 < 4:
    print(""" "Leve" (ligeramente perceptible). """)
elif 4 >= magnitud_1 < 5:
    print(""" "Moderado" (sentido por personas, pero generalmente no causa daños). """)
elif 5 >= magnitud_1 < 6:
    print(""" "Fuerte" (puede causar daños en estructuras débiles). """)
elif 6 >= magnitud_1 < 7: 
    print(""" "Muy Fuerte" (puede causar daños significativos). """)
elif 7 >= magnitud_1:
    print(""" "Extremo" (puede causar graves daños a gran escala). """)
    
# Actividad 10
# Programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# Imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio_by_us = " "
mes_by_us = 0
dia_by_us = 0

#----------

hemisferio_by_us = input("Ingresa en que hemisferio te encuentras con una N o S, segun corresponda")
if ("n" == hemisferio_by_us) or ("N" == hemisferio_by_us):
    print("Ingresaste Hemisferio NORTE")
else:
    print("Ingresaste Hemisferio SUR")

mes_by_us = int(input("Ingrese el numero del mes en el que te encuentras: "))
print("El mes ingresado es:", mes_by_us)

dia_by_us = int(input("Ingrese el día en el que te encuentras: "))
print("El día ingresado es:", dia_by_us)

#---------

if (mes_by_us == 12 and dia_by_us >= 21) or (mes_by_us in [1, 2]) or (mes_by_us == 3 and dia_by_us <= 20):
    if hemisferio_by_us == "n" or hemisferio_by_us == "N":
        print(f"En el hemisferio NORTE el mes {mes_by_us}, dia {dia_by_us}... es INVIERNO")
    else:
        print(f"En el hemisferio SUR el mes {mes_by_us}, dia {dia_by_us}... es VERANO")
elif (mes_by_us == 3 and dia_by_us >= 21) or (mes_by_us in [4, 5]) or (mes_by_us == 6 and dia_by_us <= 20):
    if hemisferio_by_us == "n" or hemisferio_by_us == "N":
        print(f"En el hemisferio NORTE el mes {mes_by_us}, dia {dia_by_us}... es PRIMAVERA")
    else:
        print(f"En el hemisferio SUR el mes {mes_by_us}, dia {dia_by_us}... es OTOÑO")
elif (mes_by_us == 6 and dia_by_us >= 21) or (mes_by_us in [7, 8]) or (mes_by_us == 9 and dia_by_us <= 20):
    if hemisferio_by_us == "n" or hemisferio_by_us == "N":
        print(f"En el hemisferio NORTE el mes {mes_by_us}, dia {dia_by_us}... es VERANO")
    else:
        print(f"En el hemisferio SUR el mes {mes_by_us}, dia {dia_by_us}... es INVIERNO")
elif (mes_by_us == 9 and dia_by_us >= 21) or (mes_by_us in [10, 11]) or (mes_by_us == 12 and dia_by_us <= 20):
    if hemisferio_by_us == "n" or hemisferio_by_us == "N":
        print(f"En el hemisferio NORTE el mes {mes_by_us}, dia {dia_by_us}... es OTOÑO")
    else:
        print(f"En el hemisferio SUR el mes {mes_by_us}, dia {dia_by_us}... es PRIMAVERA")
