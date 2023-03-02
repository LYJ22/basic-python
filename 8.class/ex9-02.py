# self
class selfTest:
    def func1():
        print("func1 called")
        
    def func2(self):
        print("func2 called")
        
f = selfTest()

# f.func1()을 사용하면 에러 발생, class method로 취급
selfTest.func1()
# 인스턴스 f가 func2의 self로 넘어간다고 볼 수 있다, instance method
f.func2()
selfTest.func2(f)