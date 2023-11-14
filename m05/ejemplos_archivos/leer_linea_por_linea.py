file = open('datos.txt', 'r')

while True:
    line = file.readline() 
    if not line: # if not data in file END
        break
    print('File line ==>', end=' ')
    print(line)