


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
