set_countries = {'Argentina', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Peru', 'Uruguay'}

print(set_countries)

set_countries.add('Venezuela')

print(set_countries)

set_countries.add('Venezuela')

print(set_countries)

hello = "hoola"

print(set(hello))


set_from_tuples = set(('abc', 'def', 'ghi','abc'))

print(set_from_tuples)

array_of_repeated_numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

not_repeted_numbers = set(array_of_repeated_numbers)

print(not_repeted_numbers)

array_of_numbers_not_repeted = list(not_repeted_numbers)

print(array_of_numbers_not_repeted)


print("#"*30)

set_countries2 = {'Argentina', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Peru', 'Uruguay'}

print(len(set_countries2))

print('Japon' in set_countries2)

print('Brasil' in set_countries2)

set_countries2.add("Japon")

print(set_countries2)

set_countries2.update({'Japon', 'China','Rusia'})

print(set_countries2)

set_countries2.discard('España')

#set_countries2.remove('España')

set_countries2.clear()

print(set_countries2)

print("#"*30)

# opetations with sets
# union
a = {'a', 'b', 'c', 'd'}
b = {'a', 'b', 'c', 'e'}

c = a.union(b)
print(c) # {'a', 'b', 'd', 'e', 'c'}

# intersection
c = a.intersection(b)
print(c) # {'b', 'a', 'c'}

# difference
c = a.difference(b)
print(c) # {'d'}

c = b.difference(a)
print(c) # {'e'}

# symmetric difference
c = a.symmetric_difference(b)
print(c) # {'d', 'e'}
c = b.symmetric_difference(a)
print(c) # {'d', 'e'}