#list
city = ["서울", "부산", "대구", "광주", "인천"]
print(len(city), city)
print(city[1])

city[1] = "전주"
print(city)

#data type 상관없이 하나의 리스트 작성 가능
temp = ["서울", "부산", 100, 235.7546]
print(temp)
print(type(temp), type(temp[0]), type(temp[2]))

name = input("이름 : ")
age = input("나이 : ")
address = input("주소 : ")
tall = input("키 : ")
weight = input("몸무게 : ")
person = [name, age, address, tall, weight]
print(person)