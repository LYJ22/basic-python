# 함수 기본 틀
# def fucntion_name(parameter):
#   code

def first_func(x):
    print("Hello", x)
    
w = "python"
first_func(w)
first_func("world")


def second_func(x2):
    value = "Hello " + str(x2)
    return value

w2 = second_func('world')
print(w2)

# 다중 return, 튜플 형식으로 리턴됨
def third_func(x3):
    y1 = x3*5
    y2 = x3*10
    y3 = x3*15
    return y1, y2, y3

z1, z2, z3 = third_func(2)
print(z1, z2, z3)
print(third_func(10))

# dictionary 형태 return 가능
def thirdOne_func(x4):
    y1 = x4*5
    y2 = x4*10
    y3 = x4*15
    return {'one':y1, 'two':y2, 'three':y3}

w4 = thirdOne_func(5)
print(w4, w4.keys(), w4.values())