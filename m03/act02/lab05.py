operacion = ""
while operacion.upper() != "S":
    valor1 = int(input('Ingrese el primer valor: '))
    valor2 = int(input('Ingrese el segundo valor: '))

    operacion = input('Indique la operación (*/+-): ')
    if (operacion == '+'):
        print(f'{valor1 + valor2}')
    elif (operacion == '-'):
        print(f'{valor1 - valor2}')
    elif (operacion == '*'):
        print(f'{valor1 * valor2}')
    elif (operacion == '/'):
        print(f'{valor1 / valor2}')
    else:
        print(f'No es una operación válida')