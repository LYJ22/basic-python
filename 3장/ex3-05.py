#문자열 연결
first_name = " Gil Dong"
last_name = "Hong"
name = last_name + first_name
print(name)

#data type에 따른 계산
temp = "Person" + str(100)
print(temp)

temp = int("100") + 100
print(temp)

#문자열 반복
arrow = "->" * 10
print(arrow)

# %s 형식 지정자
price = 1000
print("가격 : %s" % "1000")
print("가격 : %s" % price)

temp = "현재 시간은 %s시 %s분 %s초 입니다."
print(temp % (22, 24, 18))

#특수 문자와 같이 r 사용 가능
temp = r"현재 시간은 %s시 %s분 %s초 입니다."
print(temp)