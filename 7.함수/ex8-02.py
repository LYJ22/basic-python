# * 언팩킹 / 가변 매개변수 사용. 1~n개의 매개변수가 넘어와도 됨
# 튜플 형태로 받는다.
def args_func(*args):
    for i, v in enumerate(args):    # 튜플 형태를 i와 v로 언팩킹
        print('{}'.format(i), v)
    print('-----------')

def args_func2(*args):
    for i in enumerate(args):
        print('{}'.format(i))
    print('-----------')

args_func('a', 'b', 'c', 'd', 'e')
args_func2('a', 'b', 'c', 'd', 'e')

# ** 언팩킹 / key와 value를 매개변수로 사용
# 딕셔너리 형태로 받는다.
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v])
    print('------------')
    
kwargs_func(name1='a', name2='b', name3='c', name4='d', name5='e')

def ex(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)
    
ex(1, 2, 'a', 'b', 'c', name4='d', name5='e')