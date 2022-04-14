import model
import model as md
import math_lib as ml
import matplotlib.pyplot as plt
import math
import functions
import csv_module as csvm



def create_model():
    print('Введите параметры модели:')
    print('Размер популяции = ',end = '')
    pop_count = int(input())
    print('количество узлов сетки = 2^', end = '')
    gr_count = int(input())
    print('номер функции = ', end = '')
    func_num = int(input())
    func = functions.func_dict[func_num]

    model = md.Model(pop_count, gr_count, func[0], func[1])

    print('Изменить доп. параметры? [y/n] ', end='')
    if input()=='y':
        print(f'Вероятность скрещивания (по умолчанию {model.PR_CROSSOVER}) = ', end = '')
        model.PR_CROSSOVER = float(input())
        print(f'Вероятность мутации (по умолчанию {model.PR_MUTATION}) = ', end = '')
        model.PR_MUTATION = float(input())

    print(f'Изменить интервал (по умолчанию {model.interval}) ? [y/n] ', end='')
    if input() == 'y':
        print('Начало = ', end = '')
        a = float(input())
        print('Конец = ', end = '')
        b = float(input())
        model.interval = (a,b)

    return model

def draw_graph(model):
    dots_x = []
    dots_y = []

    for ind in m.current_population:
        dots_y.append(ind.fitness)
        dots_x.append(ml.gene_to_global_coords(model, ind.gene))

    plt.scatter(dots_x, dots_y, edgecolors='red')

    x = []
    for index in range(-2,2**model.grid_count+2):
        x.append(model.interval[0] + index*model.grid_step)
    y = [model.function(fx) for fx in x]

    plt.plot(x,y)
    plt.grid()
    plt.title(f'Поколение № {model.generation_number}')
    plt.show()



def print_model_generaiton(model):
    print('-----------------------------')
    print(f'номер поколения:{m.generation_number}')
    for ind in model.current_population:
        print(f'ген: {ind.gene}| индекс: {ml.grey_to_num(ind.gene)}| глобальная X: {ml.gene_to_global_coords(m, ind.gene)}| фенотип: {ind.fitness}')

    print('-----------------------------')


def save_model_generation(model):
    for ind in model.current_population:
        csvm.history.append({
            'gene': ind.gene,
            'index': ml.grey_to_num(ind.gene),
            'global_X': ml.gene_to_global_coords(m, ind.gene),
            'phenotype': ind.fitness,
            'generation': model.generation_number
        })


m = create_model()
#m.get_start_population()
#draw_graph(m)
#print_model_generaiton(m)

for i in range(5):
    m.next()
    draw_graph(m)
    print_model_generaiton(m)
    save_model_generation(m)

print('Название файла:', end='')
fn = input()
csvm.save_csv(fn)


print('------------')