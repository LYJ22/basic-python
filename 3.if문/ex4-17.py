#숫자 추측 게임
from random import *
rand_num = randint(1,100)

user_num = int(input("숫자를 맞춰보세요(1~100): "))
cnt = 0
while True:
    if user_num == rand_num:
        print("정답입니다. %s번만에 맞췄습니다." % cnt)
        break
    elif user_num > rand_num:
        print("입력한 숫자보다 작습니다.")
        cnt += 1
    else:
        print("입력한 숫자보다 큽니다.")
        cnt += 1
    user_num = int(input("숫자를 맞춰보세요(1~100): "))