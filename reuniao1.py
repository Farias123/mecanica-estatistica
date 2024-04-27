import matplotlib.pyplot as plt

x = 1.0
v = 0.0
t = 0.0
dt = 0.1

x_list = []
t_list = []


def phi(x):
    return -x


while t < 50:
    f = phi(x)
    
    x = x + dt*v + 1/2*f*dt**2
    f_ = phi(x)
    v = v + dt*(f+f_)/2
    
    x_list.append(x)
    t_list.append(t)
    
    t += dt
    

fig, ax = plt.subplots()
ax.plot(t_list, x_list)
plt.show()
