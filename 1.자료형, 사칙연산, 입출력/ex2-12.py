# try - except
try:
    i = int(input("숫자를 입력하세요: "))
    print("입력한 숫자는 ", i, "입니다.")
except ValueError:
    print("숫자가 아닙니다.")