# Ejercicio 1
edad = int(input("Escriba su edad: "))
MAYORIA_EDAD = 18
if (edad > MAYORIA_EDAD):
  print ('Es mayor de edad')

# Ejercicio 2
nota = int(input("Ingrese la nota: "))
APROBADO = 6
if (nota >= APROBADO):
  print('Aprobado')
else:
  print('Desaprobado')

# Ejercicio 3
numero = int(input("Escriba un numero par: "))
if (numero % 2 == 0):
  print('Ha ingresado un número par')
else:
  print('Por favor, ingrese un número par')

# Ejercicio 4
edad = int(input("Escriba su edad: "))
if (edad < 12):
  print('Su categoria es niño')
elif (edad >= 12 and edad < 18):
  print('Su categoria es adolescente')
elif (edad >= 18 and edad < 30):
  print('Su categoria es adulto joven')
elif (edad >= 30):
  print('Su categoria es adulto')

# Ejercicio 5
password = input('Por favor, ingrese su contraseña: ')
passwordLength = len(password)
if (passwordLength >= 8 and passwordLength <= 14):
  print("Ha ingresado una contraseña correcta")
else:
  print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if (moda == mediana and moda == media):
  print('Sin sesgo')
elif (media > mediana and mediana > moda):
  print('Sesgo positivo o a la derecha')
elif (media < mediana and mediana < moda):
  print('Sesgo negativo o a la izquierda')

# Ejercicio 7
frase = input('Ingrese una frase: ')
ultima_letra = frase[len(frase) - 1]
vocales = 'AEIOU'

if (ultima_letra.upper() in vocales):
  frase = frase + '!'
print(frase)

# Ejercicio 8
nombre = input('Ingresa tu nombre: ')
numero = int(input('Ingresa un numero'))

if (numero == 1):
  print(nombre.upper())
elif (numero == 2):
  print(nombre.lower())
elif (numero == 3):
  print(nombre.title())
else:
  print(nombre)

# Ejercicio 9
magnitud = int(input('Ingrese la magnitud del terremoto: '))

if (magnitud < 3):
  print("Muy leve")
elif (magnitud >= 3 and magnitud < 4):
  print("Leve")
elif (magnitud >= 4 and magnitud < 5):
  print("Moderado")
elif (magnitud >= 5 and magnitud < 6):
  print("Fuerte")
elif (magnitud >= 6 and magnitud < 7):
  print("Muy fuerte")
else:
  print("Extremo")

# Ejercicio 10
hemisferio = input('Ingrese el hemisferio: ')
mes = input('Ingrese el mes: ')
dia = input('Ingrese el dia: ')
estacion_norte = ''
estacion_sur = ''

if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

print(estacion_norte if hemisferio == "N" else estacion_sur) 