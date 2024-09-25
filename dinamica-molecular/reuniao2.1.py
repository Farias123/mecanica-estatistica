import matplotlib.pyplot as plt

r = [1.0, 1.0]
v = [0.5, 0.0]
a = [0.0, 0.0]

t = 0.0
dt = 0.1

x_list = []
y_list = []

def phi(r):
    x, y = r
    return [-x, -y]

while(t<10):
    f = phi(r)
    
    for i in range(len(r)):
        r[i] += dt*v[i] + 1/2*f[i]*dt**2
    
    f_ = phi(r)
    
    for i in range(len(r)):
        v[i] += dt*(f[i]+f_[i])/2
    
    x_list.append(r[0])
    y_list.append(r[1])
    
    t+=dt
    

fig, ax = plt.subplots()
ax.plot(y_list, x_list)
plt.show()