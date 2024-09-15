def get_population():
    keys = ['arg', 'bra', 'chl', 'col', 'ecu', 'per', 'uru']
    values = [45, 30, 20, 130, 200, 150, 100]
    return keys, values

keys, values = get_population()

iterable_ = {key: value for key, value in zip(keys, values)}

def get_population_by_country(country):
     return {key: value for (key,value) in iterable_.items() if key == country}

