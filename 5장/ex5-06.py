#fibonacci

n1 = 1
n2 = 1
n3 = 1

num = int(input("정수를 입력하세요: "))
for x in range(num):
    if x < 2:
        n3 = 1
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    print(n3, end=" ")