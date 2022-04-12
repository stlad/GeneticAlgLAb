import model as md
import math_lib as ml
import matplotlib.pyplot as plt
import math

def func(x):
    return x**2


m = md.Model(10, 5, func, [-32,32])
x=[]
y=[]
m.get_start_population()
for i in m.current_population:
    y.append(i.y)
    x_index =ml.grey_to_num(i.gene)
    x_global = ml.grid_index_to_global(m, x_index)
    x.append(x_global)


func_x = [a for a in range(0,32)]
func_y = [func(a) for a in func_x]


plt.scatter(x,y)
plt.plot(func_x, func_y)
plt.grid()
plt.show()
