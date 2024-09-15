sum = lambda x, y: x + y

assert sum(1, 2) == 3


age = 18

if age < 18:
    raise Exception('no puede ser menor de 18')
else:
    print('puede ser menor de 18')