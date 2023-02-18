#리스트 sort() 오름차순 내림차순
l = [65, 40, 90, 100, 55, 60]

l.sort()
for i in l:
    print(i, end=" ")

print("\n"+"-"*20)
l.sort(reverse=True)
for i in l:
    print(i, end=" ")

print("\n"+"-"*20)    
#역인덱스 사용해서 출력
start = -len(l)
end = 0
for i in range(start, end):
    print(l[i] , "-", i)
