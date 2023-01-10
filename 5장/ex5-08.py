#구구단 출력
num = int(input("출력할 구구단을 입력하세요(2~9): "))
for x in range(1,10):
    if (num < 2) or (num > 9):
        print("잘못된 범위입니다.")
        break
    print("%s * %s = %s" %(num, x, num*x))
    
    
# 사용자로부터 2개의 정수값 입력받아 두 수 사이의 3의 배수이면서 4의 배수인
# 수를 제외하고 출력
num1 = int(input("첫번째 수: "))
num2 = int(input("두번째 수: "))

for x in range(num1, num2+1):
    if(x % 3) == 0 and (x % 4) == 0:
        continue
    print(x, end=" ")