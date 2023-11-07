letra = 'z'
while letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
    letra = input('Ingrese una letra (vocal para salir): ')
        
print(f'La última letra entrada es una vocal: {letra}')


letra = 'z'
while letra not in 'aeiou':
    letra = input('Ingrese una letra (vocal para salir): ')

print(f'La última letra entrada es una vocal: {letra}')