a = {1, 2, 3, 4, 5, 6}
b = {5, 6, 7, 8, 9}
c = {10, 11, 12}
d = {2, 3, 4}

# 교집합
print(a&b)
print(a.intersection(b))

# 합집합
print(a|b)
print(a.union(b))

# 차집합
print(a-b)
print(a.difference(b))

# 교집합 존재하는지 확인, 존재하면 false
print(a.isdisjoint(b))
print(a.isdisjoint(c))

# 부분집합인지 확인
print(a.issubset(b))
print(d.issubset(a))
print(a.issuperset(d)) # 위의 함수와 반대