"""
file = open('./text.txt', 'r')

#print(file.read())

print(file.readlines(1))

file.close()
"""
with open('./text.txt', 'r') as file:
    print(file.readlines(1))