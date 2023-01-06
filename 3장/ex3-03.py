# 자동 판매기 시뮬레이션 1000원, 500원, 100원 사용
# 물건값 1000원 500원 100원 입력하면 거스름값 동전으로 출력
#(단, 입력한 돈의 합이 물건값을 초과하지 않음, 거스름돈 단위는 500원, 100원, 10원)

item_Price = int(input("물건값 :"))
thousand = int(input("1000원 :"))
fiveHundred = int(input("500원 :"))
oneHundred = int(input("100원 :"))

nod_money = (thousand*1000 + fiveHundred*500 + oneHundred*100) - item_Price
nFiveHundred = nod_money // 500
nod_money = nod_money % 500

nOneHundred = nod_money // 100
nod_money = nod_money % 100

nTen = nod_money // 10

print("거스름돈은 500원 : %s, 100원 : %s, 10원 : %s" % (nFiveHundred, nOneHundred, nTen))