# Ejercicio 1
multiplo_4 = range(4, 101, 4)
lista = []
for i in multiplo_4:
    lista.append(i)
print("Los multiplos de 4 son: ", lista)

# Ejercicio 2 
mi_lista = [1, 2, 3, 4, 5]
print("El penulimo elemento de la lista es: ", mi_lista[-2])

# Ejercicio 3
lista_vacia = []
lista_vacia.append('5')
lista_vacia.append('10')
lista_vacia.append('15')
print(lista_vacia)

# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

# Ejercicio 5
numeros = [8, 15, 3, 22, 7] # Se crea una lista con numeros
numeros.remove(max(numeros)) # La funcion max devuelve el maximo valor dentro de una lista, y la funcion remove remueve el valor indicado en la lista, resultando en el valor 22 borrando de la lista
print(numeros) # Se imprime la lista sin el numero 22

#Ejercicio 6
multiplo_5 = range(10, 31, 5)
lista_5 = []
for i in multiplo_5:
    lista_5.append(i)
print("El primer resultado de la lista es: ", lista_5[0])
print("El segundo resultado de la lista es: ", lista_5[1])

# Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "golf"
autos[2] = "punto"
print(autos)

# Ejercicio 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

# Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)

