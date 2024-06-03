import math
import turtle
def polygon(t,length,n):
    t=turtle.Turtle()
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


bob=turtle.Turtle()
polygon(bob,100,5)

def circle(t,r):
    circumference=2*math.pi*r
    n=int(circumference/3)+1
    length=circumference/n
    polygon(t,length,n)

circle(bob,100)
    
turtle.mainloop()
    
