# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name' : 'Kim', 'phone' : '010-1234-5678', 'birthday':'2023-02-18'}
b = {1 : 'apple', 2 : ' banana'}
c = {'arr':[1,2,3]}
d = {
    'Name' : 'Lee',
    'City' : 'Seoul',
    'Age' : 20,
    'Grade' : 'B',
    'Status' : True
}
e = dict([
    ('Name', 'Lee'),
    ('City', 'Seoul'),
    ('Age', 20),
    ('Grade', 'B'),
    ('Status', True)
])
f = dict(
    Name = 'Lee', 
    City = 'Seoul',
    Age = 20,
    Grade = 'B',
    Status = True
)

print( a,"\n",b,"\n",c,"\n",d,"\n",e,"\n",f)

# 출력
print('a의 이름: ', a['name'])
print('a의 번호: ', a.get('phone'))
# get은 키 값이 잘못 입력되면 에러 대신 none을 출력한다.
print('a의 번호2: ', a.get('phone2'))
print('b의 1번: ', b[1])
print('c의 배열: ', c.get('arr'))
print('f의 나이와 성적', f.get('Age'), f.get('Grade'))

# 추가
a['address'] = 'seoul'
print(a)
a['rank'] = [1,2,3]
print(a)

# 길이
print("a의 길이", len(a))