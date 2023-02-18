#boolean

flag = True
print(type(flag))
print(flag)

if flag:
    print("참입니다.")
else:
    print("거짓입니다.")


# not은 타 언어에서의 ! 같은 의미
flag = not flag
print(flag)

if flag:
    print("참입니다.")
else:
    print("거짓입니다.")
    
print("-"*20)
# None
print(bool(None))