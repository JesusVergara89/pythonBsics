my_iter = range(1, 10)

print(my_iter) #range(1, 10)

my_iter = iter(range(1, 10))

print(my_iter) #<range_iterator object at 0x102f56430>

my_iter = iter(range(1, 11))

start = 1

while start < 11:
    print(next(my_iter))
    start += 1
