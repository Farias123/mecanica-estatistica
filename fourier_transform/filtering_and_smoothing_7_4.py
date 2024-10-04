import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend


def import_data(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return np.array(content.split('\n'), float)

def make_new_c(c):
    index_to_zero = len(c) * 0.02
    new_c = np.zeros(len(c), complex)
    for i in range(len(c)):
        if i > index_to_zero:
            new_c[i] = 0
        else:
            new_c[i] = c[i]
    return new_c

def main():
    datafile = 'data_files/dow.txt'
    y = import_data(datafile)

    c = np.fft.rfft(y)
    new_c = make_new_c(c)
    new_y = np.fft.irfft(new_c)

    fig, ax = plt.subplots()
    ax.scatter(range(len(y)), y, s=2, label='original data')
    ax.scatter(range(len(new_y)), y, s=2, label='modified c')

    # ax.scatter(range(len(c)), abs(c), s=2, label='original data')
    # ax.scatter(range(len(new_c)), abs(new_c), s=2, label='modified c')

    fig.legend()
    ax.set_title(datafile)
    plt.show()



if __name__ == '__main__':
    main()