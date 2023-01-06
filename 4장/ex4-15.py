# 사용자로부터 달을 입력받아 그 달의 일 수를 출력
month = int(input("월을 입력하세요: "))

if month == 2:
    print("%s월의 일수는 28일입니다." % month)
elif month < 8:
    if month % 2 == 0:
        print("%s월의 일수는 30일입니다." % month)
    else:
        print("%s월의 일수는 31일입니다." % month)
else:
    if month % 2 == 0:
        print("%s월의 일수는 31일입니다." % month)
    else:
        print("%s월의 일수는 30일입니다." % month)