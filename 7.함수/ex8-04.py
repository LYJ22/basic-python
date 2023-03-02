# 람다식 lambda, 메모리 절약, 코드 간결
# 함수 : 객체 생성 -> 메모리 할당
# 람다 : 즉시 실행 함수, heap 영역에 저장 -> 메모리 초기화

# 함수
def func(x, y):
    return x*y

print(func(5, 7))
# 이런 식으로 사용 가능
tmp_func = func
print(tmp_func(4, 5))


# 람다
# 위 함수와 같은 의미를 지님
a = lambda x, y:x*y
print(a(5, 7))

# 람다식의 유용한 쓰임 예제
def func_final(x,y,func):
    print(x*y*func(10,20))
    
func_final(5, 6, lambda x,y:x*y)