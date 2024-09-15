increment = lambda x: x + 1

print(increment(1))


def even(x):
    return x % 2 == 0

even_numbers = list(filter(even, range(1, 10)))

multipple_of_3 = list(map(lambda x: x * 3, range(1, 10)))

print(multipple_of_3)

print(even_numbers)