temperaturas='''Utrera,29,12
Dos Hermanas,32,14
Sevilla,30,15
Alcalá de Guadaíra,31,14
'''
lista=temperaturas.splitlines()
lista_final=[]

for elem in lista:
    datos=elem.split(",")
    lista_final.append(datos)

for elem in lista_final:
    print(elem[0])