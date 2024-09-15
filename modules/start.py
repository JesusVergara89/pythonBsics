import sys
import re
import time
import collections

print(sys.path)

text = " my celphone number is (123) 456-7890 "

pattern = r'\((\d+)\) (\d+)-(\d+)'

matches = re.findall(pattern, text)

for match in matches:
    print(match)

timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(result)
print(timestamp)

# TODO: create an array with repeated numbers
repeated_numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

counter = collections.Counter(repeated_numbers)
print(counter) # Counter({1: 3, 2: 3, 3: 3, 4: 3, 5: 3})