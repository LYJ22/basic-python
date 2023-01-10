#python에서의 자료형
print(type(17))
print(type(121.432))
print(type("hello"))
print("-"*20)
print(type((1, 2, 3, 4, 5)))
print(type({1, 2, 3, 4, 5}))
print(type([1, 2, 3, 4, 5]))
print(type({'a':97, 'b':98}))

#반지름 r인 구의 부피 (4/3)*PI*r^3
from math import *
r = 5.0
print("구의 부피 :", 4/3*3.14*(r**3))
volume = 4/3*pi*pow(r,3)
print("구의 부피 :" + str(volume))

#구의 겉넓이 4*PI*r^2
outer_area = 4*pi*pow(r,2)
print("구의 겉넓이 :", str(outer_area))

# 문자열 + 는 문자열 2개가 합쳐지기 때문에 사이에 공백없이 이어서 나옴
# 구의 부피 :523.59~
# 문자열을 , 로 연속해서 적은 경우 공백을 두고 나옴
# 구의 겉넓이 : 314.159~