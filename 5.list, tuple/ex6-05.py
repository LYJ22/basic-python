# 리스트에서 검색
# 학생의 성적을 검색
l = [65, 40, 90, 100, 55, 60]
num = int(input("원하는 학생의 번호를 입력하세요: "))

print("%s번 학생의 성적은 %s점입니다."%(num, l[num-1]))

score = int(input("몇점인 학생을 찾겠습니까?: "))
for i in range(0, len(l)):
    if l[i] == score:
        print("%s점인 학생은 %s번 학생입니다."%(score, i+1))
        break
    
student = l.index(score)
print("%s점인 학생은 %s번 학생입니다."%(score, student+1))