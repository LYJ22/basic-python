#for문으로 factorial 계산
sum = 1
num = int(input("정수를 입력하세요: "))

for n in range(1, num+1):
    sum *= n
    
print("값:", sum)