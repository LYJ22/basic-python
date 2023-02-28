# while else 문도 가능하다
a = [1,2,3,4,5,6,7,8]
b = 20
i = 0
while i < len(a):
    if a[i] == b:
        print("found")
        break
    i += 1
else:
    print("not found")