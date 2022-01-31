f=open("nombrefichero.txt")
lista=f.readlines()
f.close()
print(lista)
#quitar el /n 
for elem in lista:
    datos=elem[:-1].split(",")