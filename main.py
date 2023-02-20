
#pencolor('white')
'''
pensize(3)
pencolor('red')
forward(100)
right(90)
pencolor('green')
forward(100)
right(90)
pencolor('yellow')
forward(100)
right(90)
pencolor('blue')
forward(100)
left(90)
forward(100)
backward(50)
right(90)
forward(100)
'''
#circulos
'''
circle(30)
circle(60)
circle(100)
'''
'''
fillcolor('blue')
begin_fill()
for i in range(4):
    forward(100)
    right(90)
end_fill()
'''
import random
from turtle import *
title('DESENHANDO COM PYTHON')
bgcolor('black')

speed(0)
x = 1
while x < 400:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colormode(255)
    pencolor(r, g, b)
    forward(5 + x)
    right(121)
    forward(5 + 1)

    x += 1

mainloop()