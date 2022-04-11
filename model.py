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

    def get_start_population(self):
        #self.current_population = [Individ(i,self.function(i)) for i in range(self.population_count)] # предварительно
        for i in range(self.population_count):
            ind_x = random.randint(0, 2**self.grid_count)
            ind_y = self.function(ind_x)

            self.current_population.append(Individ(ind_x, ind_y))




class Individ:
    def __init__(self, x, y):
        self.x = x
        self.y = y




def fitness(Individ, function):
    return  function(Individ.x)  # предварительно