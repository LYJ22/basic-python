class Dog:
    species = 'firstDog'
    
    # 초기화/인스턴스 속성 , init: 생성자
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def info(self):
        return '{} is {} years old.'.format(self.n, self.a)
    
    def bark(self, sound):
        return '{} says {}.'.format(self.n, sound)
    
    
a = Dog('bingo', 5)
b = Dog('john', 4)
print(a.info())
print(b.info())
print(a.bark('woof woof'))
