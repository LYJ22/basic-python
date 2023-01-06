<<<<<<< HEAD
#홀수 짝수 구분
num = int(input("정수를 입력하시오: "))

if (num%2) == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
    
#두 정수 중 큰 값 출력
x = int(input("첫번째 정수: "))
y = int(input("두번째 정수: "))
max = 0
if x > y:
    max = x
else:
    max = y
=======
#홀수 짝수 구분
num = int(input("정수를 입력하시오: "))

if (num%2) == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
    
#두 정수 중 큰 값 출력
x = int(input("첫번째 정수: "))
y = int(input("두번째 정수: "))
max = 0
if x > y:
    max = x
else:
    max = y
>>>>>>> 17108c910fc3e57d0f45d8b91272f53eeee3fcb6
print("더 큰 수는 %s입니다." % max)