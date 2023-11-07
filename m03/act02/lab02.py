# Suma de los primeros N Números: Dado un número entero positivo N entrado por el usuario, calcula la suma de todos los números desde 1 hasta N.

suma = 0
numero = int(input('Ingrese un número: '))
for n in range(1, numero + 1): # 1 ... 4 (if n == 4 exit)
    suma = suma + n

print(f'La suma de los enteros del 1 al {numero}')
print(f'es {suma}')
