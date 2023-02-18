#range 실습
sum = 0
for x in range(10):
    sum += x
print("0~9의 합:", sum)

#range(start, stop)
sum = 0
for x in range(1, 11):
    sum += x
print("0~9의 합:", sum)

#range(start, stop, step)
sum = 0
for x in range(0, 11, 2):
    sum += x
print("0~9의 합:", sum)

#문자열
s = "Hello World"
for x in s:
    print(x, end=" ")