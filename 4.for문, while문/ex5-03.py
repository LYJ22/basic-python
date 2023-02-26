#1부터 입력받은 값 까지의 합
sum = 0
num = int(input("숫자를 입력하세요: "))
for x in range(1, num+1):
    sum += x
print("합계: ", sum)

# 1~100 사이의 3의 배수 합 구하기
sum2 = 0;
for x in range(0, 101, 3):
    sum2 += x
print("합계2 :", sum2)