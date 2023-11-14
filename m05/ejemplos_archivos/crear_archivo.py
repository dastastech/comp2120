print('Crear archivo ...')
archivo = open('datos.txt','a')

print('Crear datos en el archivo ...')
archivo.write('Esto es un ejemplo de un archivo\n')
for i in range(1,11):
    archivo.write(f'Line #{i}\n')

print('Fin de los comandos con archivo.')
archivo.close()