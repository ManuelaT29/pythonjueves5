from operator import truediv
from this import d


diccionario={
    'nombre':'Manuela',
    'apellido':'Taborda',
    'edad': 22,
    'estatura': 1.47,
    'cumpleaños':'29 de Septiembre 1999',
    'colorfavorito':'Rosado',
    'AnimalFavorito':'Mariposa',
    'nombreMascota':'Niño'
}

#Accediendo de forma individual a los atributos 
# y valores del diccionario
print(diccionario)
print(diccionario['nombre'])
print(diccionario.get('AnimalFavorito'))

#acceder a Todos los atributos y valores
#de un diccionario 
#recorrer todos los valores

#.items()
for clave,valor in diccionario.items():
    print(valor)
    
#agregar desde el codigo una propiedad
diccionario['Apellido2'] = 'true'
print(diccionario)

