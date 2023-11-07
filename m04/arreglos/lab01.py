# Desarrolle un programa que defina un arreglo con cuatro elementos que sean nombres de Ciudades favoritas. El programa debe solicitar una posición del arreglo y cambiar el nombre del elemento de la posición indicada.

myFavoritePlaces = ['Italia','Hatillo','New York', 'Camuy']

print(myFavoritePlaces)
posicion = int(input('Ingrese la posición a cambiar: '))

myFavoritePlaces[posicion] = input('Indique el nuevo nombre: ')
print(myFavoritePlaces)