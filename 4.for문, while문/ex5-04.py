#1~100까지 누적값을 구하는데 2000이 넘어가면 for문 탈출
sum = 0
for x in range(101):
    sum += x
    if sum > 2000:
        print("%s까지의 합계: %s" % (x, sum))
        break