# list comprehension
lst = [1,2,3,4,5,6,7,8,9]
print(type(lst), lst)

lst2 = []
for i in range(1, 10):
    lst2.append(i)
print(type(lst2), lst2)

lst3 = [i for i in range(1, 10)]
print(type(lst3), lst3)

# 연습
a = list(i for i in range(1, 10))
print("a =", a)

b = [i*i for i in range(1, 10)]
print("b =", b)

c = [i*i for i in range(1, 10) if i != 5]
print("c =", c)

d = [i for i in range(51) if i%2 == 0]
e = [i for i in range(51) if i%2 != 0]
        
print("d =", d)
print("e =", e)


# 이중 for 문 사용
a = [ (i,j) for i in range(3) for j in range(3)]
print(a)