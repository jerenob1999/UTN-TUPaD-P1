#Ejercicio 1
def calcularFactorial(numero):
  if (numero == 0):
    return 1
  else:
    return numero * calcularFactorial(numero-1)
  
def mostrarFactorial():
  numero = int(input('Ingrese un numero: '))
  for i in range(1, numero + 1):
    print(calcularFactorial(i))

mostrarFactorial(); 

#Ejercicio 2
def calcularFibonacci(n):
  if n == 0:
      return 0
  elif n == 1:
      return 1
  else:
      return calcularFibonacci(n - 1) + calcularFibonacci(n - 2)

def mostrarFactorial():
  numero = int(input('Ingrese una posicion de fibonacci: '))
  serie = []
  for i in range(1, numero + 1):
    serie.append(calcularFibonacci(i))
  
  print(serie)

mostrarFactorial()

#Ejercicio 3
def calcularPotencia(base, exponente):
  if (exponente == 0):
    return 1
  else:
    return base * calcularPotencia(base, exponente - 1)
  
def mostrarPotencia():
  numero = int(input('Ingrese un numero: '))
  potencia = int(input('Ingrese la potencia: '))
  print(calcularPotencia(numero, potencia))

mostrarPotencia()

#Ejercicio 4
def calcularBinario(n):
    if n < 2:
        return str(n)
    return calcularBinario(n // 2) + str(n % 2)

def mostrarBinario():
    numero = int(input('Ingrese un numero para convertir a binario: '))
    binario = calcularBinario(numero)
    print(binario)

mostrarBinario()

#Ejercicio 5
def calcularPalindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return calcularPalindromo(palabra[1:-1])

def mostrarPalindromo():
   palabra = input("Ingresa una palabra: ")
   resultado = calcularPalindromo(palabra)
   if (resultado):
      print(f'La palabra {palabra} es palindromo')
   else:
      print(f'La palabra {palabra} no es palindromo')

mostrarPalindromo()

#Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

def mostrarSumaDigitos():
   numero = int(input("Ingresa un numero: "))
   suma = suma_digitos(numero)
   print(f'La suma de los digitos de {numero} es {suma}')

mostrarSumaDigitos()

#Ejercicio 7
def contar_bloques(n):
  if n == 1:
      return 1
  return n + contar_bloques(n - 1)

def mostrarBloques():
   numero = int(input("Ingresa el numero de bloques del nivel mas bajo: "))
   suma_bloques = contar_bloques(numero)
   print(f'La suma de los digitos de {numero} es {suma_bloques}')

mostrarBloques()

#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0  # Caso base

    ultimo = numero % 10

    if ultimo == digito:
        coincidencia = 1
    else:
        coincidencia = 0

    return coincidencia + contar_digito(numero // 10, digito)

def mostrarConteoDigito():
  numero = int(input("Ingresa un numero: "))
  digito = int(input("Ingresa un digito: "))
  conteo_digitos = contar_digito(numero, digito)
  print(f'En el numero {numero} el digito {digito} aparece {conteo_digitos} veces')

mostrarConteoDigito()