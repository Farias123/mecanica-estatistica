import matplotlib.pyplot as plt
import numpy as np
from cmath import pi, exp


def import_data(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return np.array(content.split('\n'), float)

def num_coef(y_len):
    # Número de coeficientes a serem calculados devido ao tamanho de y, regra do conjugado -> c[N-r] = c[r]*
    if y_len % 2 == 0:
        return int(y_len/2 + 1)
    return int((y_len + 1)/2)

def make_new_c(c, not_zero_percentage=0.10):
    index_to_zero = len(c) * not_zero_percentage
    new_c = np.zeros(len(c), complex)
    for i in range(len(c)):
        if i < index_to_zero:
            new_c[i] = c[i]
    return new_c

def dft(y):
    # transformada de fourier discreta
    N = len(y)
    K = num_coef(N)
    c = np.zeros(K, complex)

    for k in range(K):
        for n in range(N):
            c[k] += y[n] * exp(-2j * k * pi * n / N)

    return c


def idft(c, N):
    # transformada inversa de fourier discreta
    y = np.zeros(N)
    K = num_coef(N)

    for n in range(N):
        for k in range(K):
            y[n] += c[k] * exp(2j * k * pi * n / N)
        y[n] = y[n] / K

    return y

if __name__ == '__main__':
    y = import_data('data_files/dow2.txt')
    N = len(y)
    c = dft(y)
    new_c = make_new_c(c, not_zero_percentage=0.02)
    # TODO idft estranha
    new_y = idft(new_c, N)
    new_y_np = np.fft.irfft(new_c)
    fig, ax = plt.subplots()
    ax.scatter(range(len(y)), y, s=2, label='original data')
    ax.scatter(range(len(new_y)), new_y, s=2, label='modified data')
    ax.scatter(range(len(new_y_np)), new_y_np, s=2, label='modified data numpy')

    fig.legend()
    ax.set_title('dow2')
    plt.show()
