#iteration 실습
for x in [0, 1, 2]:
    print("Hello World!")
print("--------------------")    
    
for x in range(3):
    print("Hi!")
print("--------------------")
    
for x in range(3):
    print("안녕!", end=" ")
    
print(type(range(5)))

#리스트 정방향 역방향
l = ['dog', 'cat', 'lion', 'tiger', 'bird']
for x in l:
    print(x, end=" ")
print("\n")    
for x in l[::-1]:
    print(x, end=" ")
print("\n" + "-"*20)


s = ["김연아", "손흥민", "손연재"]
for name in s:
    print("반갑습니다. "+ name+"님")