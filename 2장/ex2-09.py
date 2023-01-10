# id 함수
# 메모리 값을 출력
a = "hello"
b = a
c = "hi"

print(id(a), id(b) , id(c))

# is 함수
# 메모리 값 비교(결과: True, False)
print("a is b :", a is b)
print("a is c :", a is c)
print("b is c :", b is c)

print("---------------")
# is와 ==의 비교
# 숫자나 문자열은 이미 존재하는 값이면 같은 메모리 주소지만
# 리스트는 메모리 주소가 다르다
a = 2
b = 1+1
print("a is b :", a is b)
print("a == b :", a==b)

a = "hello"
b = "hello"
print("a is b :", a is b)
print("a == b :", a==b)

a = [1, 2, 3]
b = [1, 2, 3]
print("a is b :", a is b)
print("a == b :", a==b)
