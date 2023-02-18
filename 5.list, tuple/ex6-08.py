# 튜플 자료형(순서o, 중복o, 수정x, 삭제x)
a = ()
b = (1,2,3)
c = (4)
print(type(a), type(b), type(c))

# 원소가 하나일 때 ,를 찍어야 튜플로 인식된다(c 타입: int, d 타입: tuple)
d = (5,)
print(type(d))

# 괄호 생략가능
t = 1,2,3
print(type(t))

e = (1, 2, 'a', 'b', 'c')
f = (1, 2, ('a', 'b', 'c'))

# 인덱싱
print("b[1]: ", b[1])  # 2
print("b[0]+e[1]: ", b[0]+e[1]) # 3
print("e[-1]: ", e[-1]) # c
print("f[-1] :", f[-1]) # ('a', 'b', 'c')
print("f[-1] :", f[-1][0]) # a

# 슬라이싱
print("e의 0~2", e[0:3])
print("e 1번째 이후", e[1:])
print("f안의 튜플", f[2][0:2])