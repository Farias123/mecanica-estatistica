import numpy as np
from matplotlib import pyplot as plt
from simple_fuctions import dft, num_coef


def main():
    with open('data_files/sunspots.txt', 'r') as file:
        content = file.read()

    data = [x.split('\t') for x in content.split('\n')]
    months = [float(x[0]) for x in data]
    spots = [float(x[1]) for x in data]


    fig, ax = plt.subplots()
    ax.scatter(months, spots, s=1, marker='o')
    ax.set_yticks(np.arange(min(spots), max(spots), 10))
    plt.show()

    c = dft(spots)
    fig, ax = plt.subplots()
    ax.scatter(range(num_coef(len(months))), abs(c)**2, marker='o', s=1) # todo apenas um pico
    # ax.set_yscale('log')
    plt.show()

if __name__ == '__main__':
    main()