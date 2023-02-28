# 대문자로 변환
s  = "comPutEr"
for x in s:
    if x.isupper():
        print(x)
    else:
        print(x.upper())
        
# dictionary에서 특정 숫자 찾기(ex. 20)
d = [42, 46, 789, 123, 56, 94, 20, 13, 32, 67, 85]
for x in d:
    if x == 20:
        print("x의 위치는 ", d.index(20))
        break
    else:
        print("no 20")

# for else : break없이 for문을 다 돌면 else문 실행, 자주 사용하지는 않음
for x in d:
    if x == 1000:
        print("x의 위치는 ", d.index(1000))
        break
else:
    print("no 1000")
        
# 특정 타입 찾기
d1 = ['a', 82, 3.14, 'banana', (1,2,3), False]
for x in d1:
    if type(x) is float:
        print(x, "is float")
    else:
        print("type:", type(x))