def sum_with_range(start, end):
    sum = 0
    for i in range(start, end):
        sum += i
    return sum

print(sum_with_range(1, 10))

print(sum_with_range(1,100))

print('#'*30)


def find_volume(length=1, width=1, height=1):
    return length * width * height, f'the variables are {length}, {width}, {height}', 'hello'

result = find_volume(10, 20, 30)
result1 = find_volume()

print(result)
print(result1)

print('#'*30)

price = 100

def calculate_price():
    price = 200
    price += 100
    return price

print(f'the price inside the function is {calculate_price()}')

print(f'the price outside the function is {price}')


print('#'*30)

price1 = 100

def calculate_price():
    price2 = 200
    result_ = price2 + 100
    return result_

print(f'the price inside the function is {calculate_price()}')

print(f'the price outside the function is {price}')

#print(f'this is an error: {result_}')

