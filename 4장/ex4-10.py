#if와 elif와 else
score = int(input("성적을 입력하세요(0~100점): "))
if score >= 90:
    print("학점 A")
elif score >= 80:
    print("학점 B")
elif score >= 70:
    print("학점 C")
elif score >= 60:
    print("학점 D")
else:
    print("학점 F")
    
    
#중첩 if else
appleQuality = input("사과의 상태를 입력하시오(좋음, 나쁨): ")
applePrice = int(input("사과의 가격: "))

if appleQuality == "좋음":
    if applePrice < 1000:
        print("10개를 산다.")
    else:
        print("5개를 산다.")
else:
    print("사과를 사지 않는다.")