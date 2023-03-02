# 중첩 함수
def nested_func(num):
    def in_func(num):
        print(num)
        
    print("In function")
    in_func(num + 1)
    
nested_func(10)

# 함수 안에서 선언된 함수는 외부에서 사용할 시 에러 발생
