#while문 실습
i = 0
while i < 3:
    print("반갑습니다.")
    i += 1
print("종료합니다.")

i = 0
sum = 0
while i < 10:
    print(i, end=" ")
    sum += i
    i += 1
print("합계:", sum)

#factorial 출력
i = 1
factorial = 1
while i <= 5:
    factorial *= i
    i += 1
print("5!의 값은 %s입니다." % factorial)

#구구단 3단 출력
i = 1
while i < 10:
    print("3 * %s = %s"%(i, i*3))
    i += 1
    
#1~100 사이 3의 배수만 합한 값 출력
i = 1
sum = 0

while i <= 100:
    if i % 3 == 0:
        sum += i
    i += 1
print("합계:", sum)

#정수 안의 각 자리수 합 계산 (예시: 1234 -> 1+2+3+4)
num = 1234
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print("합계:",sum)