# Ejercicio 1
print("-"*125)
print("----------------------------------------------------Ejercicio #1-------------------------------------------------------------")
print("------------------------------------------------Primer cuatrimestre----------------------------------------------------------")

Asignaturas = ["Matematica Basica", "Español", "Fundamentos de Programacion","Orientacion Universitaria", "Introducion a la Ingenieria"]
print (Asignaturas)
print("-"*125)


#Ejercicio 2
print("-"*40)
print("-------------Ejercicio # 2--------------")
Asignaturas = ["Matematica Basica", "Español", "Fundamentos de Programacion", "Orientacion Universitaria", "Introducion a la Ingenieria"]


print(f"Yo estudio {Asignaturas[0]}")
print(f"Yo estudio {Asignaturas[1]}")
print(f"Yo estudio {Asignaturas[2]}")
print(f"Yo estudio {Asignaturas[3]}")
print(f"Yo estudio {Asignaturas[4]}")
print("-"*40)

#Ejercicio 3
print("-"*50)
print("------------------Ejercicio #3-------------------")
Asignaturas = ["Matematica Basica", "Español", "Fundamentos de Programacion", "Orientacion Universitaria", "Introducion a la Ingenieria"]

nota1 = input(f"¿Qué nota sacaste en {Asignaturas[0]}? ")
nota2 = input(f"¿Qué nota sacaste en {Asignaturas[1]}? ")
nota3 = input(f"¿Qué nota sacaste en {Asignaturas[2]}? ")
nota4 = input(f"¿Qué nota sacaste en {Asignaturas[3]}? ")
nota5 = input(f"¿Qué nota sacaste en {Asignaturas[4]}? ")

print("-------------Tus Calificaciones son--------------")
print(f"En {Asignaturas[0]}, has sacado {nota1}")
print(f"En {Asignaturas[1]}, has sacado {nota2}")
print(f"En {Asignaturas[2]}, has sacado {nota3}")
print(f"En {Asignaturas[3]}, has sacado {nota4}")
print(f"En {Asignaturas[4]}, has sacado {nota5}")
print("-"*50)

#Ejercicio 4
print("-"*40)
print("--------------Ejercicio #4--------------")
print("-----Numeros ganadores de la loteria-----")

numero1 = int(input("Ingresa el primer numero ganador: "))
numero2 = int(input("Ingresa el Segundo numero  ganador: "))
numero3 = int(input("Ingresa el tecer numero ganador: "))
numero4 = int(input("Ingresa el cuarto numero ganador: "))
numero5 = int(input("Ingresa el quinto numero ganador: "))

NumerosGanadores = [numero1, numero2, numero3, numero4, numero5]

NumerosGanadores.sort()

print(f"Los numeros ganadores son:{NumerosGanadores}.")
print("-"*42)

#Ejercicio 5
print("-"*35)
print("------------Ejercicio #5-----------")

Numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Numero.sort(reverse=True)

print(Numero)
print("-"*35)

#Ejercicio 6
print("-"*50)
print("-------------------Ejercicio #6-------------------")
print("-------------¿Repetiras asignaturas?--------------")
Asignaturas = ["Matematica Basica", "Español", "Fundamentos de Programacion", "Orientacion Universitaria", "Introduccion a la ingenieria"]


nota1 = int(input(f"¿Qué nota sacaste en {Asignaturas[0]}? "))
nota2 = int(input(f"¿Qué nota sacaste en {Asignaturas[1]}? "))
nota3 = int(input(f"¿Qué nota sacaste en {Asignaturas[2]}? "))
nota4 = int(input(f"¿Qué nota sacaste en {Asignaturas[3]}? "))
nota5 = int(input(f"¿Qué nota sacaste en {Asignaturas[4]}? "))


if nota1 >= 70:
    Asignaturas.remove("Matematica Basica")
if nota2 >= 70:
    Asignaturas.remove("Español")
if nota3 >= 70:
    Asignaturas.remove("Fundamentos de Programacion")
if nota4 >= 70:
    Asignaturas.remove("Orientacion Universitaria")
if nota5 >= 70:
    Asignaturas.remove("Introduccion a la ingenieria")

print("Debes repetir:", Asignaturas)
print("-"*50)


#Ejercicio 7
print("-"*90)
print("------------------------------------Ejercicio #7------------------------------------------")
print("-------------------------------------Abecedario-------------------------------------------")
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


del abecedario[2]   
del abecedario[4]   
del abecedario[6]   
del abecedario[8]  
del abecedario[10]  
del abecedario[12]  
del abecedario[14]  
del abecedario[16] 
print(abecedario)

print("-"*90)

#Ejercicio 8

print("-"*35)
print("-----------ejercicio #8------------")
print("---------es un palindromo----------")

palabra = input("Introduce una palabra: ")

palabra = palabra.lower()

invertida = palabra[::-1]


if palabra == invertida:
    print(f"'{palabra}' es un palindromo")
else:
    print(f"'{palabra}' no es un palindromo")

print("-"*35)

#Ejercicio 9
print("-"*29)
print("--------Ejercicio #9---------")
print("---¿Cuantas vocales tiene?---")
palabra = input("Introduce una palabra: ")

palabra = palabra.lower()

a = 0
e = 0
i = 0
o = 0
u = 0

for letra in palabra:
    if letra == 'a':
        a = a + 1
    elif letra == 'e':
        e = e + 1
    elif letra == 'i':
        i = i + 1
    elif letra == 'o':
        o = o + 1
    elif letra == 'u':
        u = u + 1

print(f"La vocal 'a' aparece {a} veces")
print(f"La vocal 'e' aparece {e} veces")
print(f"La vocal 'i' aparece {i} veces")
print(f"La vocal 'o' aparece {o} veces")
print(f"La vocal 'u' aparece {u} veces")
print("-"*29)

#Ejercicio 10
print("-"*35)
print("-----------Ejercicio #10-----------")
print("---¿Cual es el mayor y el menor?---")
precios = [50, 75, 46, 22, 80, 65, 8]

menor = min(precios)
mayor = max(precios)

print(f"El menor precio es: {menor}")
print(f"El mayor precio es: {mayor}")

print("-"*35)

#Ejercicio 11
print("-"*24)
print("-----Ejercicio #11------") 
print("---Producto a escalar---")

print("Vector1 = [1, 2, 3]")
print("Vector2 = [-1, 0, 3]")

vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]

producto_escalar = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]

print(f"El producto escalar es: {producto_escalar}")

#Ejercicio 12

print("-"*40)
print("-------------Ejercicio #12--------------")
entrada = input("Introduce números separados por comas: ")

numeros_texto = entrada.split(',')  
numeros = []
for num in numeros_texto:
    numeros.append(float(num))  

suma = 0
for num in numeros:
    suma += num
media = suma / len(numeros)


suma_diferencias = 0
for num in numeros:
    diferencia = num - media
    suma_diferencias += diferencia ** 2  

varianza = suma_diferencias / len(numeros)
desviacion = varianza ** 0.5  

print(f"Media: {media}")
print(f"Desviación típica: {desviacion}")

print("-"*40)
