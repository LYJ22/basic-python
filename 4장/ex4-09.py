#논리 연산자
name = "홍길동"
age = 14
height = 160
#and 연산자
if (age >= 15) and (height >= 160):
    print("놀이기구를 탈 수 있습니다.")
else:
    print("놀이기구를 탈 수 없습니다.")
    
#or 연산자    
if (age >= 15) or (height >= 160):
    print("놀이기구를 탈 수 있습니다.")
else:
    print("놀이기구를 탈 수 없습니다.")
    
#not 연산자
if not(1==1):
    print("참입니다.")
else:
    print("거짓입니다.")
    
    
#졸업요건이 140학점 이상 이수, 평점 2.0 이상일 때 졸업가능여부 출력
total = int(input("전체 들은 학점: "))
average_score = float(input("평점: "))
if (total >= 140) and (average_score >= 2.0):
    print("졸업할 수 있습니다.")
else:
    print("졸업할 수 없습니다.")
    
#BMI가 20.0이상 25.0미만인 경우 표준입니다, 그 외 체중관리가 필요합니다 출력
#키를 입력받아서 100으로 나눈 뒤, BMI = 몸무게 / (키 * 키)
height = float(input("키: "))
weight = float(input("몸무게: "))
height /= 100
BMI = weight / (height*height)
if(BMI >= 20.0) and (BMI < 25.0):
    print("표준입니다.")
else:
    print("체중 관리가 필요합니다.")