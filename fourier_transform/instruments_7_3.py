import numpy as np
import matplotlib.pyplot as plt

def import_data(filename):
    with open(filename, 'r') as file:
        content = file.read()

    return np.array(content.split('\n'), int)

if __name__ == '__main__':
    files = ['data_files/trumpet.txt', 'data_files/piano.txt']

    for datafile in files:
        y = import_data(datafile)
        c = np.fft.rfft(y)
        c = c[:10000]

        fig, ax = plt.subplots()
        # ax.scatter(range(len(y)), y, s=2)
        ax.set_title(datafile)
        ax.scatter(range(len(c)), abs(c), s=2)
        plt.show()