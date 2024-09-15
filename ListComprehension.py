numbers = []

for i in range(1, 10):
    numbers.append(i)

print(numbers)

numbers2 = [i for i in range(1, 10)]

print(numbers2)

for value, index in enumerate(numbers):
    print(value, index)

names = ['Jesus', 'Vergara', 'Juan', 'Luis']

heights = [1.80, 1.75, 1.70, 1.65]


information_person = zip(names, heights)

for name, height in information_person:
    print(name, height)



for number in range(1, 10):
    if number % 2 == 0:
        print(number)

even_numbers = [number for number in range(1,10) if number % 2 == 0]

print(even_numbers)