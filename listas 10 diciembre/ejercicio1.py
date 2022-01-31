#Ejercicios de listas
#Ejercicio 1

#Pedir cadenas de caracteres y guardarlas en una lista (el programa pedirá al principio cuantas cadenas se van a introducir).
#A continuación se pide otra cadena, y hay que eliminar de la lista todas las apariciones de esta segunda cadena.
#Si se ha quitado algún elemento se muestra la lista, sino se informa que la segunda cadena no estaba en la lista.

lista =[]

valor=False

cantidad=int(input("¿Cuantas cadenas introducirás?"))

for i in range(0,cantidad):
    cadena=input("Introduce una cadena: ")
    lista.append(cadena)

cadena2=(input("Introduce otra cadena: "))

while cadena2 in lista: 
    if valor == False:
        valor=True
        lista.remove(cadena2)
        for valor in lista:
            print(valor, end=" ")
if valor ==False:
    print("La segunda cadena no esta en la primera.")

