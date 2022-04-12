import model
import model as md
import math_lib as ml
import matplotlib.pyplot as plt
import math

def func(x):
    return x**5+6*x**4+3*x**3+x**2-10*x+5


m = md.Model(10, 6, func, [-5,5])
m.get_start_population()

for gen in range(10):

    x=[]
    y=[]

    for i in m.current_population:
        y.append(i.fitness)
        x_index =ml.grey_to_num(i.gene)
        x_global = ml.grid_index_to_global(m, x_index)
        x.append(x_global)


    func_x = [a for a in range(-5,5)]
    func_y = [func(a) for a in func_x]

    plt.scatter(x,y)
    plt.plot(func_x, func_y)
    plt.grid()
    plt.show()

    print(f'номер поколения:{m.generation_number}')
    for ind in m.current_population:
        print(f'ген: {ind.gene}| индекс: {ml.grey_to_num(ind.gene)}| глобальная X: {ml.gene_to_global_coords(m,ind.gene)}| фенотип: {ind.fitness}')

    m.next()




print('------------')
'''ind = (model.get_best_fit_individ(m.current_population))
print('-----------------')
print(f'ген: {ind.gene}| индекс: {ml.grey_to_num(ind.gene)}| глобальная X: {ml.gene_to_global_coords(m,ind.gene)}| фенотип: {ind.fitness}')'''