import turtle

turtle.Screen().bgcolor("Red")
turtle.Screen().setup(300,300)
polygon = turtle.Turtle()

numsides = 4
sidelength = 70
angle = 360.0 / numsides

for i in range(numsides):
    polygon.forward(sidelength)
    polygon.right(angle)

turtle.done()