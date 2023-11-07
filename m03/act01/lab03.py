# Permite que el usuario introduzca palabras hasta que decida detenerse (por ejemplo, escribiendo "STOP"). Luego, informa cuántas palabras tenían menos de 5 caracteres, cuántas tenían entre 5 y 10 caracteres y cuántas tenían más de 10 caracteres.

menor5 = 0 # palabras con menos de 5 letras
igual5_10 = 0 # palabras con 5 a 10 letras
mayor10 = 0 # palabras que tienen más de 10 letras

palabra = input('Ingrese una palabra (STOP para detener el programa): ')
while palabra.upper() != "STOP":
    cantidad_letras = len(palabra)
    if (cantidad_letras < 5):
        menor5 = menor5 + 1
    elif (cantidad_letras <= 10): # 5..10
        igual5_10 = igual5_10 + 1
    else:
        mayor10 = mayor10 + 1

    palabra = input('Ingrese una palabra: ')


print(f'Palabras con menos de 5 letras {menor5}')
print(f'Palabras con 5 a 10 letras {igual5_10}')
print(f'Palabras con más de 10 letras {mayor10}')