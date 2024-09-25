import numpy as np
from matplotlib import pyplot as plt
from cmath import pi, exp
from numpy import zeros


def num_coef(y_len):
    # Número de coeficientes a serem calculados devido ao tamanho de y, regra do conjugado -> c[N-r] = c[r]*
    if y_len % 2 == 0:
        return int(y_len/2 + 1)
    return int((y_len + 1)/2)

def dft(y):
    # transformada de fourier discreta
    N = len(y)
    c = zeros(num_coef(N), complex)
    for k in range(num_coef(N)):
        for n in range(N):
            c[k] += y[n]*exp(-2j*k*pi*n/N)

    return c

def square_wave(N, n):
    if n > N/2:
       return  -1
    return 1

def create_y(N):
    y = zeros(N)
    for n in range(N):
        # y[n] = square_wave(N, n) # exec. 7.1 a
        # y[n] = n # exec. 7.1 b
        y[n] = np.sin(pi*n/N)*np.sin(20*pi*n/N) # exec. 7.1 c
    return y

if __name__ == '__main__':
    N = 1000
    y = create_y(N)
    c = dft(y)
    fig, ax = plt.subplots()
    ax.grid()
    ax.scatter(range(N), y, marker='o', s=5)
    plt.show()
    fig, ax = plt.subplots()
    ax.scatter(range(num_coef(N)), abs(c), marker='o', s=5)
    plt.show()