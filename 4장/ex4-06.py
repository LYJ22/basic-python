# 20kg이 넘어가면 추가비용을 내야한다고 한다. 20kg 미만은 수수료가 없다
# 사용자로부터 짐 무게 입력받아 지불해야 하는 금액 계산

price = float(input("짐의 무게 : "))
if price >= 20.0:
    print("수수료 가격은 %s입니다."% 20000)
else:
    print("수수료 가격은 %s입니다."% 0)