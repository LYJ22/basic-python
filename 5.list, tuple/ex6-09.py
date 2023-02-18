# 튜플 packing, unpacking

# packing
t = ('apple', 'banana', 'cherry', 'grape', 1, 2, 3)

print(t[0])
print(t[-1])

# unpacking -> 튜플의 원소를 각각 변수로 해체
# 괄호가 필수는 아니나 보통 묶어서 unpacking 임을 표시
(a, b, c, d, e, f, g) = t
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g))
print(a, b, c, d, e, f, g)