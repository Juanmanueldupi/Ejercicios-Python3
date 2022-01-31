#Ejercicios de listas

#Ejercicio 5

#Vamos a crear un programa que tenga el siguiente menú:

#    Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
#    Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
#    Longitud de la lista: te muestra el número de elementos de la lista.
#    Eliminar el último número: Muestra el último número de la lista y lo borra.
#    Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
#    Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
#    Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
#    Mostrar números: Muestra los números de la lista
#    Salir

#Nota: Utilizar todos los métodos de las listas que sean necesarios.


lista=[]

opcion = 0

while opcion != 9:
    print("")
    print("1. Añadir un numero a la lista")
    print("2. Añadir un numero a la lista en la posicion deseada ")
    print("3. Longitud de la lista")
    print("4. Elimina el ultimo numero")
    print("5. Elimina el numero que tu quieras ")
    print("6. Numeros de veces que aparece un numero")
    print("7. Posicion del numero elegido")
    print("8. Muestra la lista")
    print("9. Salir")

    opcion = int(input("Dime la opcion: "))

    if opcion == 1:
        num = int(input("Dime el numero que quieres introducir: "))
        lista.append(num)

    if opcion == 2:
        num = int(input("Dime el numero que quieres introducir: "))
        pos = int(input("Dime la posicion donde lo quieres poner: "))
        if pos >= 1 and pos <= len(lista):
            lista.insert(pos-1,num)
            print("Se ha introducido el numero en la casilla asignada: ")
    
    if opcion == 3:
        print("La longitud de la lista es: ", len(lista))

    if opcion == 4:
        lista.pop()
        print("Se ha eleminado el ultimo numero")

    if opcion == 5:
        pos = int(input("Dime la posicion del numero que quieres eliminar: "))
        if pos >= 1 and pos <= len(lista):
            lista.pop(pos-1)  
            print("Se ha eliminado el numero en la casilla asignada")  

    if opcion == 6:
        num = int(input("Indica el numero que quieres contar: "))
        print("El numero sale: ", lista.count(num), " veces")

    if opcion == 7:
        num = int(input("Indica el numero del quieres saber la posicion: "))
        if lista.count(num) == 1:
            lista.index(num)
        elif lista.count(num) > 1:
            print("Las posiciones son: ")
            cont = 0
            for i in lista:
                cont = cont + 1
                if i == num:
                    print(cont, "", end= "")
                
    if opcion == 8:
        for i in lista:
            print(i," " ,end="")