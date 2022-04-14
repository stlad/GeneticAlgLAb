import math

def func_0(x):
    return x**8 - 0.5*x**7 - 3*x**6 + 2*x**5 + 2*x**4 - 3*x**2 - 2*x

def func_1(x):
    return x**2

def func_2(x):
    return math.sin(x)

def func_3(x):
    return math.cos(x)

def func_4(x):
    return x

def func_5(x):
    return math.sin(x**2)

def func_6(x):
    return (x**4)/4 - x**3

func_dict ={
    0: (func_0,[-2,2]),
    1: (func_1,[-10,10]),
    2: (func_2,[0,7]),
    3: (func_3,[0,7]),
    4: (func_4,[0,100]),
    5: (func_5,[-3,3]),
    6: (func_6,[-1,4])
}