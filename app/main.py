import utils 

data = [
    {
        'name': 'jesus',
        'age': 30,
        'country': 'arg',
    },
    {
        'name': 'vergara',
        'age': 40,
        'country': 'bra',
    },
    {
        'name': 'juan',
        'age': 50,
        'country': 'uru',
    }
]

def run():

    keys, values = utils.get_population()

    print(keys, values)

    result = utils.get_population_by_country('usa')

    print(result)


if __name__ == '__main__':
    run()