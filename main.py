

import turtle


screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor('cornflower blue')

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t2 = turtle.Turtle()
t2.hideturtle()
t3 = turtle.Turtle()
t3.hideturtle()

t5=turtle.Turtle()
t5.penup()





t.penup()
t.goto(0, 50)
t.pendown()
t.write("Turtle Presentation Assignment", font=("Chela one", 24, "bold"), align="center")

t.penup()
t.goto(0, -50)
t.pendown()
t.write("Sriya Kharel", font=("Satisfy", 18, "bold"), align="center")


#circle
t.penup()
t.goto(150,-100)
t.pendown()
t.fillcolor('pale violet red')
t.pencolor('pale violet red')

t.begin_fill()
t.circle(30)
t.end_fill()

t.setheading(90)

t.begin_fill()
t.circle(30)
t.end_fill()

t.setheading(180)

t.begin_fill()
t.circle(30)
t.end_fill()

t.setheading(270)

t.begin_fill()
t.circle(30)
t.end_fill()

t.setheading(0)

t.penup()
t.goto(150,-110)
t.pendown()
t.fillcolor('orange')
t.pencolor('orange')
t.begin_fill()
t.circle(10)
t.end_fill()


#2nd circle

t.penup()
t.goto(-150,150)
t.pendown()
t.fillcolor('pale violet red')
t.pencolor('pale violet red')

t.begin_fill()
t.circle(30)
t.end_fill()

t.setheading(90)

t.begin_fill()
t.circle(30)
t.end_fill()

t.setheading(180)

t.begin_fill()
t.circle(30)
t.end_fill()

t.setheading(270)

t.begin_fill()
t.circle(30)
t.end_fill()

t.setheading(0)

t.penup()
t.goto(-150,140)
t.pendown()
t.fillcolor('orange')
t.pencolor('orange')
t.begin_fill()
t.circle(10)
t.end_fill()

enter = input("Press Enter to Start")
t.clear()

#2nd page
screen.bgcolor('hot pink')
t2.penup()
t2.goto(0, 50)
t2.pendown()
t2.write("Favorite Foods", font=("Chela one", 24, "bold"), align="center")

#triangle
t.penup()
t.goto(-50,100)
t.pendown()
t.fillcolor('purple')
t.begin_fill()

t.goto(50,100)
t.goto(0,200)
t.goto(-50,100)
t.end_fill()


turtle.addshape("mac.gif")
t5.shape("mac.gif")
t5.goto(-150,150)
a = t5.stamp()

t3.penup()
t3.goto(-160, 160)
t3.pendown()
t3.write("Mac and Cheese", font=("Chela one", 14, "bold"), align="center")


turtle.addshape("pasta.gif")
t5.shape("pasta.gif")
t5.goto(150,-150)
b = t5.stamp()

t3.penup()
t3.goto(160, -160)
t3.pendown()
t3.write("pasta  ", font=("Chela one", 18, "bold"), align="center")


turtle.addshape("tacos.gif")
t5.shape("tacos.gif")
t5.goto(-150,-150)
c = t5.stamp()

t3.penup()
t3.goto(-150, -150)
t3.pendown()
t3.write("tacos  ", font=("Chela one", 18, "bold"), align="center")

t3.penup()
t3.goto(0,0)
t3.pendown()
t3.write("hit enter for next page!", font=("Chela one", 24, "bold"), align="center")

# #add pictures

enter = input("Press Enter to Start")
t2.clear()
t.clear()
t3.clear()

t5.clearstamps()
t5.hideturtle()



#page3
screen.bgcolor('orchid')
t3.penup()
t3.goto(0, 50)
t3.pendown()
t3.write("Hobbies", font=("Chela one", 24, "bold"), align="center")

t3.penup()
t3.goto(0,0)
t3.pendown()
t3.write("hit enter for next page!", font=("Chela one", 20, "bold"), align="center")

turtle.addshape("travel.gif")
t5.shape("travel.gif")
t5.goto(-150,150)
d = t5.stamp()

t3.penup()
t3.goto(-150,150)
t3.pendown()
t3.write("I like to travel!", font=("Chela one", 15, "bold"), align="center")

turtle.addshape("movies.gif")
t5.shape("movies.gif")
t5.goto(150,-150)
e = t5.stamp()

t3.penup()
t3.goto(150,-150)
t3.pendown()
t3.write("I like to watch", font=("Chela one", 15, "bold"), align="center")


t3.penup()
t3.goto(150,-165)
t3.pendown()
t3.write("movies and shows!", font=("Chela one", 15, "bold"), align="center")

turtle.addshape("ccok.gif")
t5.shape("ccok.gif")
t5.goto(-150,-150)
f = t5.stamp()

t3.penup()
t3.goto(-150,-150)
t3.pendown()
t3.write("I like to cook!", font=("Chela one", 15, "bold"), align="center")

turtle.addshape("run.gif")
t5.shape("run.gif")
t5.goto(150,150)
g = t5.stamp()

t3.penup()
t3.goto(150,150)
t3.pendown()
t3.write("I like to go on", font=("Chela one", 15, "bold"), align="center")

t3.penup()
t3.goto(150,165)
t3.pendown()
t3.write("runs and walks!", font=("Chela one", 15, "bold"), align="center")

t.penup()
t.goto(-50,0)
t.pendown()
t.fillcolor('plum1')
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()


enter = input("Press Enter to Start")
t.clear()
t3.clear()
t5.clear()

#page4
screen.bgcolor('light salmon')
t3.penup()
t3.goto(0, 50)
t3.pendown()
t3.write("Favorite Movie", font=("Chela one", 24, "bold"), align="center")

turtle.addshape("movie1.gif")
t5.shape("movie1.gif")
t5.goto(-150,150)
g = t5.stamp()

t3.penup()
t3.goto(0,-60)
t3.pendown()
t3.write("My favorite movie is Tangled!", font=("Chela one", 15, "bold"), align="center")

turtle.addshape("tangled.gif")
t5.shape("tangled.gif")
t5.goto(-150,-150)
g = t5.stamp()

t3.penup()
t3.goto(0,0)
t3.pendown()
t3.write("hit enter for next page!", font=("Chela one", 20, "bold"), align="center")



t.setheading(45)
t.penup()
t.forward(250)
t.pendown()
t.fillcolor('cornsilk')
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()


t.setheading(0)


enter = input("Press Enter to Start")
t.clear()
t3.clear()
t5.clear()



#page5
screen.bgcolor('powder blue')
t3.penup()
t3.goto(0, 50)
t3.pendown()
t3.write("Favorite Sport", font=("Chela one", 24, "bold"), align="center")

turtle.addshape("track.gif")
t5.shape("track.gif")
t5.goto(-160,160)
h = t5.stamp()

turtle.addshape("track1.gif")
t5.shape("track1.gif")
t5.goto(-150,-150)
i = t5.stamp()

t.penup()
t.goto(75,100)
t.pendown()

t.fillcolor('purple')
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

t3.penup()
t3.goto(0,0)
t3.pendown()
t3.write("My favorite sport is track!", font=("Chela one", 20, "bold"), align="center")













turtle.done()


