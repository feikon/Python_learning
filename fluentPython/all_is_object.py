from icecream import ic


def print_name(name='Ya'):
    print(name)


my_func1 = print_name()  # 函数返回值
my_func2 = print_name    # 函数对象，类似于对函数重命名

ic(my_func1)    # None
ic(my_func2)    # <function print_name at 0x7f32e91abd90>


# ic(id(my_func1))
# ic(id(print_name))
# ic(id(my_func2))
