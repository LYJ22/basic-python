<<<<<<< HEAD
# 윤년 계산하기
# 조건1. 4로 나누어 떨어지면 윤년, 조건2. 100으로 나누어 떨어지면 제외
# 조3. 400으로 나누어 떨어지면 윤년

year = int(input("년도를 입력하세요: "))
if year % 4 == 0:
    if year % 100 == 0:
        
        if year % 400 == 0:
            print("윤년입니다.")
        else:
            print("윤년이 이닙니다.")
            
    else:
        print("윤년입니다.")

else:
    print("윤년이 아닙니다.")
    
#또다른 답
=======
# 윤년 계산하기
# 조건1. 4로 나누어 떨어지면 윤년, 조건2. 100으로 나누어 떨어지면 제외
# 조3. 400으로 나누어 떨어지면 윤년

year = int(input("년도를 입력하세요: "))
if year % 4 == 0:
    if year % 100 == 0:
        
        if year % 400 == 0:
            print("윤년입니다.")
        else:
            print("윤년이 이닙니다.")
            
    else:
        print("윤년입니다.")

else:
    print("윤년이 아닙니다.")
    
#또다른 답
>>>>>>> 17108c910fc3e57d0f45d8b91272f53eeee3fcb6
#if ((year%4 == 0) and (year%100 != 0)) or (year % 400 == 0)