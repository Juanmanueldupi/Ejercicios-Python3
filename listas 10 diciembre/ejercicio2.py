#Ejercicio de listas
#Ejercicio 2

#Crear una lista con 10 número aleatorios (del 1 al 100).
#A continuación se muestra la lista. 
#El programa seguirá mostrando el siguiente menú:

#1. Sumar
#2. Máximo
#3. Media
#4. Salir
#Opción:

#crear lista con 10 numeros aleatorios
from random import randint

lista=[]
for i in range(10):
    numero=randint(1,100)
    lista.append(numero)
#mostrar la lista
for i in lista:
    print(i, " ",end="")
#contador
opcion = 0
condicion = False
#mostrar el menu
while opcion != 4:
    print("")
    print("1. Sumar")
    print("2. Máximo")
    print("3. Media")
    print("4. Salir")
    opcion= int(input("Dime la opción: "))
    if opcion ==1:
        sum=0
        for i in lista:
            sum= sum + i
        print(f"La suma es: {sum} ")
        condicion=True
    if opcion ==2:
        max=0
        for i in lista:
            if i > max:
                max = i
        print(f"El numero maximo es: {max}")
    if opcion == 3:
        if condicion:
            med= sum / len(lista)
            print(f"La media es: {med}")
        else:
            sum=0
            for i in lista:
                sum=sum + 1
            med= sum / len(lista)
            print(f"la media es: {med}")
    if opcion ==4:
        print()