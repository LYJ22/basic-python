#사용자로부터 정수를 입력받아 양수, 0, 음수인지 출력
num = int(input("정수를 입력하시오: "))
if num > 0:
    print("양수입니다.")
elif num == 0:
    print("0입니다.")
else:
    print("음수입니다.")
    

#주사위 눈을 랜덤으로 출력
from random import *
num = randint(1, 6)
print("주사위: ", num)

#random()은 0.0에서 1.0사이 실수 반환
num = random()
print(num)
#randrange(start, stop, step)는 start와 stop 사이 step 값에 따라 랜덤 값 반환
#만약 값을 n 하나만 넣는 경우 0에서 n미만 사이 랜덤한 정수 반환
num = randrange(0, 101, 2)
print(num)
num = randrange(10)
print(num)

##궁금해서 시도해본 것. 이런 식으로도 된다.
#import random
#num = random.randint(1,10)
#print(num)