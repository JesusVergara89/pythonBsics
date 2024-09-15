import csv
import matplotlib.pyplot as plt

def read_csv(path):
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dic = {key: value for (key, value) in iterable}
            data.append(country_dic)
        name = [country['Country/Territory'] for country in data]
        population = [country['World Population Percentage'] for country in data]
        return name, population


def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()          


if __name__ == '__main__':
    name, population = read_csv('./world_population.csv')
    generate_bar_chart(name,population)
