import turtle
import time

turtle.speed(10)
turtle.screensize(canvheight=200,canvwidth=200,bg="cyan")
# width 与 height 为小数时表示占据屏幕的比例
# turtle.setup(width=0.5,height=0.5)

turtle.up()
turtle.goto(-200,200)
turtle.down()
turtle.fillcolor("red")
turtle.color("red")

turtle.begin_fill()
turtle.forward(480)
turtle.right(90)
turtle.forward(320)
turtle.left(90)
turtle.backward(480)
turtle.right(90)
turtle.backward(320)
turtle.end_fill()

turtle.up()
turtle.forward(64)
turtle.left(90)
turtle.forward(32)
turtle.down()

# 大五角星
a=96
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
turtle.begin_fill()
for i in range(1,6):
    turtle.forward(a)
    turtle.right(144)
    turtle.speed(2)
turtle.end_fill()

#无需使用移动指针 直接使用goto更方便
turtle.up()
# 移动到五角星右顶点
turtle.forward(96)
# 向左边转动°(度数)
turtle.left(53)
turtle.forward(36)
turtle.down()

# 第一个小五角星
a=32
turtle.begin_fill()
for i in range(1,6):
    turtle.forward(a)
    turtle.right(144)
    turtle.speed(5)
turtle.end_fill()

turtle.up()
turtle.right(80)
turtle.forward(42)
turtle.left(55)

# 第二个小五角星
a=32
turtle.begin_fill()
for i in range(1,6):
    turtle.forward(a)
    turtle.right(144)
    turtle.speed(5)
turtle.end_fill()

turtle.up()
turtle.right(96)
turtle.forward(32)

# 第三个小五角星
a=32
turtle.begin_fill()
for i in range(1,6):
    turtle.forward(a)
    turtle.right(144)
    turtle.speed(5)
turtle.end_fill()

turtle.up()
turtle.right(54)
turtle.forward(45)
turtle.right(30)

# 最后一个小五角星
a=32
turtle.begin_fill()
for i in range(1,6):
    turtle.forward(a)
    turtle.right(144)
    turtle.speed(2)
turtle.end_fill()
turtle.ht()
time.sleep(2)
