# list 실습
person_name = "홍길동"
person_age = "20"
person_address = "서울특별시"
person_tel = "010-1234-5678"
print(person_name, person_age, person_address, person_tel)

person = ["홍길동", "20", "서울특별시", "010-1234-5678"]
print(person)

# 정수+리스트
a = [1,2,3,['a','b']]
print(a, type(a))
# 정수+리스트+튜플
b = [1,2,3,[1,2,3],(1,2,3)]
print(b, type(b))

c = [{1,2,3,3}, {'a':100, 'b':200}]
print(c, type(c))
print(c[1])

# list 길이
d = [1,2,3,4,5,[1,2,3,3]]
print(len(d), len(d[5]))