# 리스트 추가, 수정, 삭제, 병합
l = [65, 40, 90, 100, 55, 60]
print(l)

# 추가
l.append(70)
print(l)

# 수정
l[-1] = 85
print(l)

# 삭제
l.pop()
print(l)

del l[-1]
print(l)

l.remove(40)
print(l)

print("-"*30)
# 병합 (tuple로도 가능, set은 불가)
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]

ab = a + b
print(ab)

a4 = a*4
print(a4)

a.extend(b)
print(a)
