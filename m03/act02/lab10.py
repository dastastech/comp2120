secreto = 7
for n in range(1,3): # if n < 3 iterar; if n == 3 exit
    numero = int(input('Ingrese un número del 1 al 10: '))
    if (numero == secreto):
        print(f'Número acertado :-D')
        break
    else:
        print('No es el valor secreto')


