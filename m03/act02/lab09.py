numero = 1
while (numero % 2) != 0:
    numero = int(input('Ingrese un número: '))
    if (numero % 2) != 0:
        print(f'El número {numero} no es par')

print(f'El número {numero} es par')
