# 사용자로부터 점수를 입력받아 성적 출력
# 95~100 : A+, 90~94 : A0, 85~89 : B+, ... D0까지. 그 아래는 F
score = int(input("점수를 입력하시오: "))
if score >= 90:
    if score >= 95:
        print("학점 A+")
    else:
        print("학점 A0")
elif score >= 80:
    if score >= 85:
        print("학점 B+")
    else:
        print("학점 B0")
elif score >= 70:
    if score >= 75:
        print("학점 C+")
    else:
        print("학점 C0")
elif score >= 60:
    if score >= 65:
        print("학점 D+")
    else:
        print("학점 D0")
else:
    print("학점 F")