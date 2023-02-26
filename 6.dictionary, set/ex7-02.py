a = dict(
    Name = 'Lee', 
    City = 'Seoul',
    Age = 20,
    Grade = 'B',
    Status = True
)

# keys, values, items
print("a의 키:",a.keys())
print("a키의 리스트:",list(a.keys()))

print("a의 값:",a.values())
print("a값의 리스트:",list(a.values()))

print("a의 아이템(키와 값):",a.items())
print("a아이템의 리스트:",list(a.items()))

# 제거
print("Name pop: ", a.pop('Name'))
print("a: ",a)

print("무작위 pop: ", a.popitem())
print("a: ",a)
print("무작위 pop: ", a.popitem())
print("a: ",a)
print("무작위 pop: ", a.popitem())
print("a: ",a)
print("무작위 pop: ", a.popitem())
print("a: ",a)