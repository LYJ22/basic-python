# __init__ : 생성자, __del__ : 소멸자
class Warehouse:
    stock_num = 0
    
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1
    
    def __del__(self):
        Warehouse.stock_num -= 1
        
user1 = Warehouse('Lee')
user2 = Warehouse('Kim')

print(Warehouse.stock_num)
print(user1.name)
print(user2.name)
# user의 namespace에 stock number가 없다
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
# 이럴 경우 파이썬은 Warehouse의 stock number을 찾아서 출력해준다.
print(user1.stock_num)

del user1
print(user2.stock_num)