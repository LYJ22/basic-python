#사용자에게 명령어를 입력받아서 터틀그래픽 제어해보자
# "left" 입력하면 왼쪽 회전, "right" 입력하면 오른쪽 회전

import turtle
t = turtle.pen()
#반복문으로 if 구문 이용하여 방향 제어
while(True):
    direction = input("왼쪽=left, 오른쪽=right, 종료=quit")
    if direction == "quit":
        break
    if direction == "left":
        t.left(60)
        t.forward(50)
    if direction == "right":
        t.right(60)
        t.forward(50)
        
# 그래픽 창이 클릭이 되어야 사라지는 코드
turtle.exitonclick()