import random
import model as md

def num_to_grey_code(num):
    return num ^ (num >> 1)


def get_grey_codes(n, res =[]):
    res = []
    for i in range(2**n):
        res.append(num_to_grey_code(i))
    return  res



def grey_to_num(gr):
    bin =0
    while gr>0:
        bin = bin^gr
        gr =gr >>1
    return bin


def grid_index_to_global(model, index):
    a = model.interval[0]
    global_pos = a + (model.grid_step * index + (model.grid_step / 2))
    return global_pos

def gene_to_global_coords(model, gene):
    index_x = grey_to_num(gene)
    return grid_index_to_global(model, index_x)


def cross_individs(model, first, sec):
    gap_point = gap = random.randint(1, model.grid_count-1)

    a = format(first.gene, 'b')
    b = format(sec.gene, 'b')

    a1 = a[:gap] + b[gap:]
    b1 = b[:gap] + a[gap:]

    new_a_ind = md.Individ(int(a1,2))
    #new_a_ind.make_func(model)

    new_b_ind = md.Individ(int(b1, 2))
    #new_b_ind.make_func(int(b1,2))

    return (new_a_ind, new_b_ind)


def mutate(model, ind):
    gene = a = list(format(ind.gene,'b'))

    for i in range(len(gene)):
        if random.random() < 1.0/len(gene):
            if gene[i] == '1':
                gene[i] = '0'
            else:
                gene[i] = '1'

    mutated_gene = int(''.join(gene),2)
    ind.gene = mutated_gene
    return


