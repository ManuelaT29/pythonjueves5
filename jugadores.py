from pickletools import OpcodeInfo
from pydoc import cli

opcion=100

print("Empandas inteligentes")
print("1. Agregar clientes: ")
print("2. Busque un Clinte po cedula: ")
print("3. Mostar cedulas: ")

print("0. Salir")



#Lista
clientes=[]


while(opcion != 0):

    #Diccionario
    cliente={}

    #pedimmos la opcion deseada
    opcion=int(input("Digite la opcion preferida. *"))
    
    #Caminos del menu
    if(opcion==1):
       
        cliente['cedula']=input("Didite su cedula: ")
        cliente['nombre']=input("Digite su nombre: ")
        clientes.append(cliente)

    if(opcion==2):
        print(cliente)  
    if (opcion==3):
        cedulaBuscar=input("digite su cedula: ")
        for cliente in clientes:
            if(cliente["cedula"]==cedulaBuscar):
                print(f"Cliente encontrado: {cliente['cedula']}")
            else:
                print("Usuario no encontrado ")

        print(cliente['cedula'])


    elif(opcion==0):
        break

    else:
        print("Digite una opcion valida ")

else:
        print("Adios")