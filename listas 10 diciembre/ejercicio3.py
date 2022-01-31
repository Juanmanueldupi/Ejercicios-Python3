#Ejercicios de listas

#Ejercicio 3

#Tenemos la siguiente variable definida en nuestro programa (esta variable puede tener cualquier valor,
#es decir, le podemos añadir nuevas ciudades con temperaturas):

#temperaturas='''Utrera,29,12
#Dos Hermanas,32,14
#Sevilla,30,15
#Alcalá de Guadaíra,31,14
#'''

#En esa cadena se definen nombres de poblaciones y las temperaturas máximas y mínimas de dichas poblaciones durante un día.

#Realiza un programa que muestre el nombre de las poblaciones y la temperatura media. Además el programa te debe pedir el nombre de una población y nos debe dar la temperatura máxima y mínima (si la población no existe se debe dar une error.)

#Ayuda: Puede venir muy bien utilizar los métodos splitlines y split de cadenas.

temperatura='''Utrera,29,12
Dos Hermanas,32,14
Sevilla,30,15
Alcalá de Guadaíra,31,14
'''

lista=[]
lista1=[]

lista=temperatura.splitlines()
    
for i in lista:
    datos=i.split(",")
    lista1.append(datos)

for var in lista1:
    med=(int(var[1])+int(var[2]))/2
    nombre=var[0]
    print(f"\n-Nombre: {nombre}")
    print(f"-Media de temperaturas: {med}")
print()

poblacion=input("-Introduce el nombre de una población: ")
falso=False
for variable in lista1:
    if poblacion==variable[0]:
        print(f"\n-Temperatura máxima: {variable[1]}\n-Temperatura mínima: {variable[2]}")
        falso=True
        
if not falso:
    print("\n~ La población introducida no existe")