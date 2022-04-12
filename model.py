import random
import math_lib as ml


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

    def next(self):
        pass

    def selection(self, t = 2): # турнирный отбор
        winners = []
        for i in range(self.population_count):
            rand_indexies = []
            for j in range(t):
                rand_indexies.append(random.randint(0,self.population_count-1))

            tour = [self.current_population[g] for g in rand_indexies]
            winners.append(get_best_fit_individ(tour))

        return winners

    def crossing(self):
        pass

    def mutation(self):
        pass







class Individ:
    def __init__(self, gene, y):
        self.gene = gene
        self.fitness = y


def get_best_fit_individ(population):
    best = (population[0], population[0].fitness)
    for ind in population:
        if ind.fitness <= best[1]:
            best = (ind, ind.fitness)

    return best[0]

