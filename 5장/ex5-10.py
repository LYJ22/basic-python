# 사각형 3개 그리기(단, 갈수록 20도씩 기울어짐)
import turtle
t = turtle
t.pen()

for x in range(3):
    for y in range(4):
        t.forward(70)
        t.left(90)
    t.left(20)
    
t.exitonclick()