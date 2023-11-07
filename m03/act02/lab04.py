
continuar = True
while continuar == True:
    valor1 = int(input('Ingrese el primer valor: '))
    valor2 = int(input('Ingrese el segundo valor: '))
    if (valor1 > valor2):
        print(f'{valor1} es mayor {valor2}')
    elif (valor2 > valor1):
        print(f'{valor2} es mayor {valor1}')
    else:
        print(f'{valor1} es igual a {valor2}')
        continuar = False