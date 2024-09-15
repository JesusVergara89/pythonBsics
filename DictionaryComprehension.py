dictionary_of_people_information = {'Jesus': {'height': 1.80, 'weight': 70},
                                    'Vergara': {'height': 1.75, 'weight': 60},
                                    'Juan': {'height': 1.70, 'weight': 50},
                                    'Luis': {'height': 1.65, 'weight': 40}}

for name, information in dictionary_of_people_information.items():
    print(name, information['height'])


heights = [information['height'] for name, information in dictionary_of_people_information.items()]
print(heights)

names = ['jesus', 'vergara', 'juan', 'luis']
ages = ['70', '60', '50', '40']

person_data = {name: age for (name,age) in zip(names, ages)}
print(person_data)

print('#'*30)


population = [40,30,20,130]
countries = ['Argentina', 'Brasil', 'Chile', 'Colombia']

population_by_country = {country: population for (country, population) in zip(countries, population)}
print(population_by_country)

countries = ['Argentina', 'Brasil', 'Chile', 'Colombia']
population = [40,30,20,130]

population_by_country = {country: population for (country, population) in zip(countries, population)}
print(population_by_country)
print("#"*30)

countries = ['Argentina', 'Brasil', 'Chile', 'Colombia']
ages = [40,30,20,130]

people_by_country = {country: age for (country, age) in zip(countries, ages)}
print(people_by_country)

countries = ['Argentina', 'Brasil', 'Chile', 'Colombia']
population = [40,30,20,130]

people_by_country = {country: population for (country, population) in zip(countries, population)}

print(people_by_country.items(), "hhhh")

more_population = { country:population for (country,population) in people_by_country.items() if population >= 130}

print(more_population)

text = "hi, i'm jesus vergara"

unique = { c: c.upper() for c in text if c in 'aeiou'}
print(unique)