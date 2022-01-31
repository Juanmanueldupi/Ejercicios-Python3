#Ejercicios de listas

#Ejercicio 4

#Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:

#   Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
#   Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
#   Eliminar: Me pide una cadena, y la elimina de la lista.

#El programa te muestra el menú, hasta que introduzcamos la opción 0 de salir.

#Dígame cuántas palabras tiene la lista: 4
#Dígame la palabra 1: Carmen
#Dígame la palabra 2: Alberto
#Dígame la palabra 3: Benito
#Dígame la palabra 4: Carmen
#La lista creada es: Carmen, Alberto, Benito, Carmen
#Elige opción:
#1. Contar
#2. Modificar
#3. Eliminar	
#0. Salir	

#1
#Dígame la palabra a buscar: Carmen
#La palabra 'Carmen' aparece 2 veces en la lista.		

#2
#Sustituir la palabra: Carmen
#por la palabra: David
#La lista es ahora: Alberto, David, Benito, David

#3
#Palabra a eliminar: David
#La lista es ahora: Alberto, Benito	
#0
#Adiós!!!

lista=[]
cadena =int(input("Dígame cuántas palabras tiene la lista:"))
for i in range(cadena):
    cadena = input("Dígame la palabra:")
    lista.append(cadena)
print(f"La lista creada es: {lista}")
print("Elige opción:")
print("1. Contar")
print("2. Modificar ")
print("3. Eliminar")
print("0. Salir")
opcion = int(input("Elige opción:"))
if opcion == 1:
        cadena = input("Dígame la palabra a buscar:")
        print("La palabra aparece %d veces en la lista" % lista.count(cadena))
elif opcion == 2:
        buscar = input("Sustituir la palabra: ")
        sustituir = input("por la palabra: ")
        for i in range(len(lista)):
          if lista[i] == buscar:
              lista[i] = sustituir
        print(f"La lista es ahora: {lista}")  
        
elif opcion == 3:
        cadena = input("Palabra a eliminar:")
        for i in range(len(lista) - 1, -1, -1):
          if lista[i] == cadena:
              del lista[i]
        print(f"La lista es ahora: {lista}")
elif opcion == 0:
    print("Salir del programa")