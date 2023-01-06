<<<<<<< HEAD
# 사용자의 연도를 입력받아 초, 중, 고, 대학생으로 분류
# 나이 8~13(초등학생), 14~16(중학생), 17~19(고등학생), 20~27(대학생), 이외 일반인
year = int(input("태어난 년도를 입력해주세요:" ))
age = 2023-year
if(age >= 8) and (age < 14):
    print("초등학생입니다.")
elif(age >= 14) and (age < 17):
    print("중학생입니다.")
elif(age >= 17) and (age < 20):
    print("고등학생입니다.")
elif(age >= 20) and (age < 28):
    print("대학생입니다.")
else:
=======
# 사용자의 연도를 입력받아 초, 중, 고, 대학생으로 분류
# 나이 8~13(초등학생), 14~16(중학생), 17~19(고등학생), 20~27(대학생), 이외 일반인
year = int(input("태어난 년도를 입력해주세요:" ))
age = 2023-year
if(age >= 8) and (age < 14):
    print("초등학생입니다.")
elif(age >= 14) and (age < 17):
    print("중학생입니다.")
elif(age >= 17) and (age < 20):
    print("고등학생입니다.")
elif(age >= 20) and (age < 28):
    print("대학생입니다.")
else:
>>>>>>> 17108c910fc3e57d0f45d8b91272f53eeee3fcb6
    print("일반인입니다.")