import matplotlib.pyplot as plt

N = 2
D = 2

r = [[1.0, 1.0], [0.5, 0.5]]
v = [[0.5, 1.0], [-0.1, -0.9]]
a = [[1.0, 0.0], [-2.0, 2.0]]

t = 0.0
dt = 0.1

x1_list = []
y1_list = []
x2_list = []
y2_list = []


def forca():
    a = [[0.0, 0.0], [0.0, 0.0]]
    for i in range(N-1):
        for j in range(i+1, N):
            r2 = 0
            for m in range(D):
                dr = r[i][m] - r[j][m]
                r2 += dr*dr
            r2 = 1/r2
            r6 = r2*r2*r2
            f = 48*r2*r6*(r6-0.5)
            for m in range(D):
                a[i][m] += f*dr
                a[j][m] -= f*dr


while t < 10:
    forca()
    
    for i in range(N):
        for m in range(D):
            r[i][m] += dt*v[i][m] + 1/2*a[i][m]*dt**2
            v[i][m] += dt*a[i][m]

    forca()

    for i in range(N):
        for m in range(D):
            v[i][m] += dt*a[i][m]/2
    
    x1_list.append(r[0][0])
    y1_list.append(r[0][1])

    x2_list.append(r[1][0])
    y2_list.append(r[1][1])

    t += dt

fig, ax = plt.subplots()
ax.plot(y1_list, x1_list, label='N = 0')
ax.plot(y2_list, x2_list, label='N = 1')
ax.legend()
plt.show()
