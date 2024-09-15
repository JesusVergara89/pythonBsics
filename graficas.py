import matplotlib.pyplot as plt

def generate_bar_chart():
    labels = ['A', 'B', 'C']
    values = [10, 20, 30]
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

generate_bar_chart()