a = dict(
    Name = 'Lee', 
    City = 'Seoul',
    Age = 20,
    Grade = 'B',
    Status = True
)

# 조회(in)
print("a City: ", 'City' in a)
print("a Status: ", 'Status' in a)

# 수정
a.update(Age=25)
print(a)

#잘 쓰는 방법은 아니지만 이렇게 사용할 수 있다.
temp = {'Name' : 'Kim'}
a.update(temp)
print(a)