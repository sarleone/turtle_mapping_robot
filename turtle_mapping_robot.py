from turtle import *

robot = Turtle()

moves = [('l',2), ('l',5), ('l', 5), ('r',5), ('l', 2)]
#moves = [('r',3), ('r',3), ('r', 3), ('l', 2)]

robot.seth(180)

for move in moves:
    if move[0] == 'l':
        robot.left(90)
    else:
        robot.right(90)
    robot.fd(move[1]*10)

heading = 180
x, y = 0, 0
for move in moves:
    if move[0] == 'l':
        heading = (heading + 90) % 360
    else:
        heading = (heading - 90) % 360
    if heading == 0:
        x += move[1]
    elif heading == 90:
        y += move[1]
    elif heading == 180:
        x -= move[1]
    elif heading == 270:
        y -= move[1]
        
print("x=", x, "y=", y)

##x = robot.xcor()
##y = robot.ycor()
robot.penup()
robot.setpos(0,0)
robot.seth(180)
robot.pencolor("red")
robot.pendown()

if y >= 0:
    print('R' + str(y), end=' ') 
    robot.right(90)
    robot.fd(y*10)
    if x >= 0:
        print('R' + str(x), end=' ') 
        robot.right(90)
        robot.fd(x*10)
    else:
        print('L' + str(-x), end=' ') 
        robot.left(90)
        robot.fd(-x*10)
else:
    print('L' + str(-y), end=' ') 
    robot.left(90)
    robot.fd(-y*10)
    if x >= 0:
        print('L' + str(-x), end=' ') 
        robot.left(90)
        robot.fd(-x*10)
    else:
        print('R' + str(x), end=' ') 
        robot.right(90)
        robot.fd(x*10)
print()