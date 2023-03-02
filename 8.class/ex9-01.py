# 클래스
class Dog:
    species = 'firstDog'
    
    # 초기화/인스턴스 속성 , init: 생성자
    def __init__(self, name, age):
        self.n = name
        self.a = age

print(Dog)

# 클래스 사용
# 인스턴스 생성, a와 b는 인스턴스다.
a = Dog("bob", 2)
b = Dog("mike", 1)

print("Dog a:",a.__dict__)
print("Dog b:",b.__dict__)
print("Dogs name is {}, {} and age is {}, {}".format(a.n, b.n, a.a, b.a))

print(Dog.species)
print(a.species)
print(b.species)