<<<<<<< HEAD
# 지구에서 가장 가까운 별은 40 * 10^12 km 거리
# 빛의 속도로 가는데 걸리는 시간, 빛의 속도는 300,000
from math import *
light_speed = 300000
distance = 40 * pow(10, 12)
second = distance / light_speed
print("걸리는 시간(초) :", second)
light_year = second / (60*60*24*365)
print("걸리는 시간(년) :", light_year)

#정수 10과 실수 10은 같다. 단, 문자열 "10"과는 다르다
print(10 == 10.0)
=======
# 지구에서 가장 가까운 별은 40 * 10^12 km 거리
# 빛의 속도로 가는데 걸리는 시간, 빛의 속도는 300,000
from math import *
light_speed = 300000
distance = 40 * pow(10, 12)
second = distance / light_speed
print("걸리는 시간(초) :", second)
light_year = second / (60*60*24*365)
print("걸리는 시간(년) :", light_year)

#정수 10과 실수 10은 같다. 단, 문자열 "10"과는 다르다
print(10 == 10.0)
>>>>>>> 17108c910fc3e57d0f45d8b91272f53eeee3fcb6
print("10" == 10)