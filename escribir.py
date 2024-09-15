with open('./text.txt', 'r+') as file: # r+ para abrir el archivo en modo lectura y escritura
    lines = file.readlines()
    for line in lines:
        print(line)


with open('./text.txt', 'a') as file:
    file.write('hola\n')

with open('./text.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)