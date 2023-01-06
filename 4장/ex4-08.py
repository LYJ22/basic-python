#블록의 들여쓰기가 중요하다. 반드시 공간을 동일하게 주어야 한다.
#아래와 같은 경우 error 발생
#score = 50
#if score >= 95:
#    print("축하합니다.")
#   print("합격입니다.")


#구입한 가격이 5만원 이상이면 5% 할인. 입력받은 금액의 최종금액 출력
total_price = int(input("구입한 금액: "))
if total_price >= 50000:
    discount = total_price * 0.05
    sales_price = total_price - discount
    print("할인 금액: %s, 총 금액: %s" % (discount, sales_price))
else:
    print("할인 금액 대상이 아닙니다. 총 금액: %s" % total_price)
    
    
#문자열 중앙에 있는 문자 추출
# 예시로 문자열 weekend의 경우 k를 출력, monday의 경우 nd
word = input("문자열을 입력하세요: ")
length = len(word)
if length % 2 == 0:
    middle = length//2
    print(word[middle-1]+word[middle])
else:
    middle = length//2
    print(word[middle])