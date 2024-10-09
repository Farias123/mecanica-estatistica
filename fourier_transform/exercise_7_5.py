import numpy as np
from matplotlib import pyplot as plt
from numpy import zeros
from cmath import pi, exp

from fourier_transform.filtering_and_smoothing_7_4 import make_new_c
from fourier_transform.simple_fuctions_7_1 import num_coef

def dft(y):
    # transformada de fourier discreta
    N = len(y)
    c = zeros(num_coef(N), complex)
    for k in range(num_coef(N)):
        for n in range(N):
            c[k] += y[n]*exp(-2j*k*pi*n/N)

    return c

def idft(c, N):
    y = zeros(N, complex)

    for n in range(N):
        for k in range(num_coef(N)):
            y[n] += c[k]*exp(2j*k*pi*n/N)
        y[n] = y[n]/N

    return y

def f(t):
    if round(2*t) % 2 == 0:
        return 1
    return -1

def create_f(N):
    f_array = zeros(N)
    interval = np.linspace(0, 1/2, N)
    # intervalo de 1000 pontos entre 0 e 1/2 (um ciclo)
    for i in range(N):
        f_array[i] = f(interval[i])
    return f_array


if __name__ == '__main__':
    N = 1000
    y = create_f(N)
    c = dft(y)
    new_c = make_new_c(c)
    new_y = idft(new_c, N)
    fig, ax = plt.subplots()
    # ax.set_yscale('log')
    ax.scatter(range(N), y, marker='o', s=5, label='original_y')
    # Problema com plotagem de complexos
    ax.scatter(range(N), new_y, marker='o', s=5, label='smoothed_y')
    plt.show()