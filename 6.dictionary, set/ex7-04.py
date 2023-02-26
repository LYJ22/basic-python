# set 집합(순서x, 중복x, 수정o, 삭제o)

# 선언
a = set([1,2,3,4])
b = set([1,2,'apple','banana', 2, 2])
c = set()
d = {'apple', 'banana', 'cherry', 'pear'} #dictionary와 차이점 : 키가 없다.
e = {1, 2, 'apple', (3,4,5), 7.89}

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)

# 추가 삭제
a.add(5)
print(a)
a.remove(2)
print(a)
a.discard(8) # 없는 값을 제거하려 해도 error발생 X
print(a)
a.pop()
print(a)
a.clear() # 전부 삭제
print(a)

# set -> tuple
t = tuple(d)
print(type(t), t)

# set -> list
l = list(d)
print(type(l), l)