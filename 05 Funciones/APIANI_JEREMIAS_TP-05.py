# #Ejercicio 1
def imprimir_hola_mundo():
  print("Hola Mundo!")

imprimir_hola_mundo()

# #Ejercicio 2
def saludar_usuario(nombre):
  return f'Hola {nombre}'

nombre = input('Ingresa tu nombre ')
saludo = saludar_usuario(nombre)
print(saludo)

# #Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
  return f"Soy {nombre} {apellido}, tengo  {edad} años y vivo en {residencia}"

nombre = input('Ingresa tu nombre ')
apellido = input('Ingresa tu apellido ')
edad = input('Ingresa tu edad ')
residencia = input('Ingresa tu residencia ')

info = informacion_personal(nombre, apellido, edad, residencia)
print(info)

#Ejercicio 4
def calcular_area_circulo(radio):
  return 3.14 * (radio * radio)

def calcular_perimetro_circulo(radio):
  return 3.14 * (radio * 2)

def calcular_circulo():
  radio = int(input('Ingresa el radio '))
  area = calcular_area_circulo(radio)
  perimetro = calcular_perimetro_circulo(radio)
  print((f'El area del circulo es {area} y su permietro es de {perimetro}'))

calcular_circulo()

#Ejercicio 5
def segundos_a_horas(segundos):
  return segundos // 3600

segundos = int(input('Ingresa la cantidad de segundos '))
horas = segundos_a_horas(segundos)
print((f'En {segundos} segundos hay {horas} horas'))

#Ejercicio 6
def tabla_multiplicar(numero):
  for i in range(11):
    print((f'Tabla del {i} resultad: {i * numero}'))

numero = int(input('Ingresa un numero '))
tabla_multiplicar(numero)

#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a // b
    return (suma, resta, multiplicacion, division)

a = int(input('Ingresa un numero '))
b = int(input('Ingresa otro numero '))
resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#Ejercicio 8
def calcular_imc(peso, altura):
  return peso / (altura ** 2)

peso = float(input('Ingresa tu peso '))
altura = float(input('Ingresa tu altura '))

imc = calcular_imc(peso, altura)
print((f'Tu IMC es de {imc}'))

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
  return (celsius * 9/5) + 32

celsius = float(input('Ingrese la temperatura en grados celsius '))
fahrenheit = celsius_a_fahrenheit(celsius)
print((f'La temperatura en celsius {celsius} es de {fahrenheit} fahrenheit'))

#Ejercicio 10
def calcular_promedio(a, b, c):
  return (a + b + c) / 3

numero1 = float(input('Ingrese el primer numero '))
numero2 = float(input('Ingrese el segundo numero '))
numero3 = float(input('Ingrese el tercer numero '))

promedio = calcular_promedio(numero1, numero2, numero3)
print((f'El promedio es de {promedio}'))


  


