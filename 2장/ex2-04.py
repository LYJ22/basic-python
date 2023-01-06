#5000원이 있고 사탕이 120원일 때 최대 살 수 있는 사탕 수
money = 5000
candy = 120

# /는 정확한 나누기 , //는 정수형 결과
# 추가로 **는 지수 계산, 3**3 == 27
print("최대 구입 가능한 수:", money/candy)
print("최대 구입 가능한 수(정수):", money//candy)
print("잔돈: ", money%candy)