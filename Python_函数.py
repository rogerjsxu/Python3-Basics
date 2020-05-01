
# 参数
# 局部变量
# 全局变量


m = 8 # 全局变量
n = 9 # 全局变量


def add(a,b): # 参数
    return a+b

def func():
    m = 3  # 局部变量 作用域
    n = 4
    print(m)

def func2():
    print(n)

def print_root(root_name):
    print(root_name)

def return_root(root_name):
    
    return root_name

def f(x):
    a = x+1
    print(a)



def non_return(num):
    num = num+1
    print(num)


def return_0():
    return 123

def multiply(a,b):
    result = a*b
    print(result)
72
multiply(8,9)


