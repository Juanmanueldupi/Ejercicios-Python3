#Como hacer un menu

menu='''
1. Opcion 1 
2. Opcion 2
3. Opcion 3
4. Salir'''

print(menu)
opcion=int(input())
while opcion!=4:
    if opcion==1:
        print("Opcion 1")
    elif opcion==2:
        print("Opcion 2")
    print(menu)
    opcion=int(input())