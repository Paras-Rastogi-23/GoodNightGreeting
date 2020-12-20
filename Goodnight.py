import turtle
import random
scr = turtle.Screen()
scr.setup(width=1600,height=800)
scr.bgcolor('black')

moon = turtle.Turtle()
moon.hideturtle()
moon.speed(5)

star = turtle.Turtle()
star.hideturtle()
star.speed(5)

text = turtle.Turtle()
text.hideturtle()
text.speed(0)
colors = ['blue','orange','red','pink','cyan','white','magenta','brown','ivory','grey']

def draw_moon(pos,color):
    x,y=pos
    moon.color(color)
    moon.penup()
    moon.goto(x,y)
    moon.pendown()
    moon.begin_fill()
    moon.circle(100)
    moon.end_fill()
draw_moon((-300+250,170),'white')
draw_moon((-270+250,180),'black')
def draw_star(pos,color,length):
    x,y = pos
    star.color(color)
    star.penup()
    star.goto(x,y)
    star.pendown()
    star.begin_fill()
    for i in range(5):
        star.forward(length)
        star.right(144)
        star.forward(length)
    star.end_fill()
          
draw_star((-240+250,320),'red',80)   
star.speed(0)          
def write_text(color):
    text.color(color)
    text.penup()
    text.goto(-180,-270)
    text.pendown
    style = ('Stencil Std Bold',50,'normal')
    text.write('Good Night Python\n\n  from: Paras.py', font=style,move=True)
    text.speed(6)
write_text('green')    
def random_pos():
    return (random.randint(-800,800),random.randint(-400,400))
def random_length():
    return random.randint(5,25)

while True:
    color = random.choice(colors)
    pos = random_pos()
    length = random_length()
    
    draw_star(pos,color,length)
    write_text(color)
turtle.done()