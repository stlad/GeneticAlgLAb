


def num_to_grey_code(num):
    return num ^ (num >> 1)

def get_grey_codes(n, res =[]):
    res = []
    for i in range(2**n):
        res.append(num_to_grey_code(i))
    return  res




