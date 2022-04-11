import model as md
import matplotlib.pyplot as plt

def func(x):
    return x**2


m = md.Model(5, 5, func, [0,5])

x = []
y=[]
m.get_start_population()
for i in m.current_population:
    x.append(i.x)
    y.append(i.y)


plt.scatter(x,y)
plt.show()
