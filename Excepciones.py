try:
    print(0/0)
except ZeroDivisionError:
    print('No se puede dividir por cero')


print('#'*30)

try:
    assert 1 / 0, 'No se puede dividir por cero'
except ZeroDivisionError as e:
    print(e)

print('#'*30)


def add(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError as e:
        result = f'No se puede dividir por cero: {e}'
    return result

result = add(1, 0)
print(result)