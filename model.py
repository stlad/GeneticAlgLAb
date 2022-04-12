import random

import math_lib as ml
import random as rnd


class Model:
    def __init__(self, pop_count, grid_count, func, interval):
        self.population_count = pop_count
        self.grid_count = grid_count
        self.function = func
        self.current_population = []
        self.grey_nums = ml.get_grey_codes(grid_count)
        self.interval = (interval[0], interval[1])
        self.grid_step = (interval[1] - interval[0])/(2**grid_count)


    def get_start_population(self):
        #self.current_population = [Individ(i,self.function(i)) for i in range(self.population_count)] # предварительно
        for i in range(self.population_count):
            x = random.randint(0,2**self.grid_count-1)
            global_x = ml.grid_index_to_global(self, x)

            ind_x = self.grey_nums[x]
            ind_y = self.function(global_x)

            self.current_population.append(Individ(ind_x, ind_y))








class Individ:
    def __init__(self, gene, y):
        self.gene = gene
        self.y = y




def fitness(Individ, function):
    return  function(Individ.x)  # предварительно