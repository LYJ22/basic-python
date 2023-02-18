# slice 실습
t = "hello"
print(t, id(t))
print(t[:1], id(t[:1]))
print(t[:2], id(t[:2]))
print(t[:3], id(t[:3]))
print(t[:4], id(t[:4]))
print(t[:5], id(t[:5]), t is t[:5])
print(t[:-1], id(t[-1]))
print(t[:-2], id(t[-2]))
print(t[:-3], id(t[-3]))
print(t[:-4], id(t[-4]))
print(t[:], id(t[:]), t is t[:])

print("--------------------")
# 문자를 더한 뒤 slice한 문자열은 따로 할당 받는다.
a = "hello"
print("a id : %s"% id(a))
b = "hello"
print("b id : %s, a is b : %s"% (id(b), a is b))
b = b + "!"
print("b id : %s, a is b : %s"% (id(b), a is b))
b = b[:-1]
print("b id : %s, a is b : %s"% (id(b), a is b))