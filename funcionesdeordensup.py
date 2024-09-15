def increment(x):
    return x + 1

def high_order(func, x):
    return x + func(x)

result = high_order(increment, 5)

print(result)

increment_v2 = lambda x: x + 1

high_order_v2 = lambda func, x: x + func(x)

result_v2 = high_order_v2(increment_v2, 2)

print(result_v2)