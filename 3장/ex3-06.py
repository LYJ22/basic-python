<<<<<<< HEAD
#문자열 인덱싱(문자 추출)
word = "Python"
print(len(word))
print(word[0], word[5])

print(word[len(word) - 1])

#한번 작성된 문자열 변경 불가능
# word[2] = a  안됨

item1 = input("첫번째 단어 입력 : ")
item2 = input("두번째 단어 입력 : ")
item3 = input("세번째 단어 입력 : ")

word = item1[0] + item2[0] + item3[0]
=======
#문자열 인덱싱(문자 추출)
word = "Python"
print(len(word))
print(word[0], word[5])

print(word[len(word) - 1])

#한번 작성된 문자열 변경 불가능
# word[2] = a  안됨

item1 = input("첫번째 단어 입력 : ")
item2 = input("두번째 단어 입력 : ")
item3 = input("세번째 단어 입력 : ")

word = item1[0] + item2[0] + item3[0]
>>>>>>> 17108c910fc3e57d0f45d8b91272f53eeee3fcb6
print("새로 만든 문자: ", word)