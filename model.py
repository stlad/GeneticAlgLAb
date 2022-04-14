import random
import math_lib as ml
import copy

class Model:
    def __init__(self, pop_count, grid_count, func, interval):
        self.population_count = pop_count
        self.grid_count = grid_count
        self.function = func
        self.current_population = []
        self.grey_nums = ml.get_grey_codes(grid_count)
        self.interval = (interval[0], interval[1])
        self.grid_step = (interval[1] - interval[0])/(2**grid_count)
        self.PR_CROSSOVER = 0.5
        self.PR_MUTATION = 0.1
        self.generation_number = 0

    def get_start_population(self):
        #self.current_population = [Individ(i,self.function(i)) for i in range(self.population_count)] # предварительно
        for i in range(self.population_count):
            x = random.randint(0,2**self.grid_count-1)
            '''global_x = ml.grid_index_to_global(self, x)

            ind_x = self.grey_nums[x]
            ind_y = self.function(global_x)

            self.current_population.append(Individ(ind_x, ind_y))'''
            ind_gene = self.grey_nums[x]
            ind = Individ(ind_gene)
            ind.make_func(self)

            self.current_population.append(ind)

    def next(self):
        if self.generation_number ==0:
            self.get_start_population()
            self.generation_number = 1
            return
        next_generation = []
        next_generation = self.selection(3)
        next_generation = self.crossover(next_generation)
        self.mutation(next_generation)

        for i in next_generation:
            i.make_func(self)

        self.generation_number += 1

        self.current_population = next_generation
        return

    def selection(self, t=2): # турнирный отбор
        winners = []
        for i in range(self.population_count):
            rand_indexies = []
            for j in range(t):
                rand_indexies.append(random.randint(0,self.population_count-1))

            tour = [self.current_population[g] for g in rand_indexies]
            winners.append(copy.copy(get_best_fit_individ(tour)))

        return winners

    def crossover(self, pop):
        for child1, child2 in list(zip(pop[::2], pop[1::2])):
            if random.random() < self.PR_CROSSOVER:
                child1, child2 = ml.cross_individs(self, child1, child2)

        return pop

    def mutation(self, pop):
        for mutant in pop:
            if random.random() < self.PR_MUTATION:
                ml.mutate(self, mutant)
        return







class Individ:
    def __init__(self, gene):
        self.gene = gene
        #self.fitness = y


    def make_func(self, model):
        global_x = ml.gene_to_global_coords(model, self.gene)
        self.fitness = model.function(global_x)




def get_best_fit_individ(population):
    best = (population[0], population[0].fitness)
    for ind in population:
        if ind.fitness <= best[1]:
            best = (ind, ind.fitness)

    return best[0]

