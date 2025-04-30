#Ejercicio 1
for i in range(0, 101):
    print(i)

#Ejercicio 2
numero = int(input("Ingrese un número: "))
suma_digitos = 0

for digito in str(numero):
    suma_digitos += 1
print(f"La cantidad de dígitos en el número {numero} es: {suma_digitos}")

#Ejercicio 3
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
max_num = max(numero1, numero2)
min_num = min(numero1, numero2)
suma = 0

for i in range(min_num + 1, max_num):
    suma += i
print(f"La suma de los números entre {min_num} y {max_num} es: {suma}")

#Ejercicio 4
suma = 0
while True:
    numero = int(input("Ingresá un número: "))
    suma += numero
    if numero == 0:
        break

print(f"La suma de los números ingresados es: {suma}")

#Ejercicio 5
from random import *
intentos = 0
numero_aleatorio = randint(1, 9)
while True:
    numero = int(input("Ingresá un número entre 1 y 9: "))
    intentos += 1
    if numero != numero_aleatorio:
        print("Número inválido. Intenta de nuevo.")
    else:
        break
print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")

#Ejercicio 6
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

#Ejercicio 7
numero = int(input("Ingrese un número: "))
suma = 0

for i in range(0, numero):
    suma += i
print(f"La suma de los números desde 0 hasta {numero} es: {suma}")

#Ejercicio 8
cantidad_numeros = int(input("Ingrese la cantidad de números a evaluar: "))
numeros_pares = 0
numeros_impares = 0
numeros_negativos = 0
numeros_positivos = 0

for i in range(cantidad_numeros):
    numero = int(input("Ingrese un número: "))
    if numero < 0:
        numeros_negativos += 1
    elif numero > 0:
        numeros_positivos += 1
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

print(f"Cantidad de números pares: {numeros_pares}")
print(f"Cantidad de números impares: {numeros_impares}")
print(f"Cantidad de números negativos: {numeros_negativos}")
print(f"Cantidad de números positivos: {numeros_positivos}")

#Ejercicio 9
cantidad_numeros = int(input("Ingrese la cantidad de números a evaluar: "))
suma_numeros = 0

for i in range(cantidad_numeros):
    numero = int(input("Ingrese un número: "))
    suma_numeros += numero

promedio = suma_numeros / cantidad_numeros
print(f"El promedio de los números es: {promedio}")

#Ejercicio 10
numero = int(input("Ingrese un número: "))
numero_reversa = []

for digito in str(numero):
    print(digito)
    numero_reversa.insert(0, int(digito))
print(f"El número al revés es: {''.join(map(str, numero_reversa))}")
    