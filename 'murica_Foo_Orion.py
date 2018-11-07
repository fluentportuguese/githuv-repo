'''
Orion Foo
'murica_Foo_Orion.py
10/28/2018
This program asks the user for input for the height of the American Flag and uses Turtle to draw an accurately proportioned flag.
'''
import turtle
import math
turtle.speed(0)

a=int(input("Enter the sacred number: "))
b=a/1.9
screen = turtle.Screen()
screen.screensize(5000 ,5000)

def draw_rectangle(x,y,turtle,length,height,color):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
        
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
def draw_star(x,y,turtle,size,color):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()
def write(x,y,word,color):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.color(color)
    turtle.write(word,align="center", font=("Arial",20,"normal"))

def main():

    def draw_flag(a):
    
        draw_rectangle(-a/2,b/2,turtle,a,b,"Black")
        x=0
        y=0
        z=1
        theta=1
        alpha=2
        beta=2
        for i in range(7):
            draw_rectangle(-a/2,b/2-x,turtle,a,b/13,"#B22234")
            x+=2*b/13
        for i in range(6):
            draw_rectangle(-a/2,(b/2-b/13)-y,turtle,a,b/13,"White")
            y+=2*b/13
        draw_rectangle(-a/2,b/2,turtle,2/5*a,b*7/13,"#3C3B6E")
        for i in range(5):
            for i in range(6):
                draw_star(-a/2+z*((2/5*a)/12)-(4/5*b/13)/2,b/2-(theta*(b*7/13)/10)+(1/2*(2/5*b/13)**2*math.sin(math.degrees(144)))/(4/5*b/13*math.sin(math.degrees(144))/math.sin(math.degrees(18))/2),turtle,4/5*b/13,"White")
                z+=2
            z=1
            theta+=2
        for i in range(4):
            for i in range(5):
                draw_star(-a/2+alpha*((2/5*a)/12)-(4/5*b/13)/2,b/2-(beta*(b*7/13)/10)+(1/2*(2/5*b/13)**2*math.sin(math.degrees(144)))/(4/5*b/13*math.sin(math.degrees(144))/math.sin(math.degrees(18))/2),turtle,4/5*b/13,"White")
                alpha+=2
            alpha=2
            beta+=2
        write(0,-b/2-100,"'murica(The American Flag)","Black")
        write(0,-b/2-135,"Orion Foo, 10/30/2018","Black")
        turtle.hideturtle()
    draw_flag(a)
if __name__=='__main__':
    main()
