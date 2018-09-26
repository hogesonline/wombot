#draw wombot

import turtle

def polyDodec (t, x, y, length):
  t.goto(x, y)
  t.setheading(0)

  t.begin_poly()
  
  for count in range(12):
    t.forward(length)
    t.left(360/12)

  t.end_poly()
  

  return t.get_poly()

def polyHalfDodec (t, x, y, length):
  t.goto(x, y)
  t.setheading(180)
  t.begin_poly()

  for count in range(6):
    t.forward(length)
    t.right(360/12)
  t.forward(length)
  t.goto(x,y)
  t.end_poly()
  

  return t.get_poly()

def polyTwoHalfDodec (t, x, y, length):
  t.goto(x, y)
  t.setheading(0)
  t.begin_poly()

  for count in range(6):
    t.forward(length)
    t.left(360/12)
  t.forward(length)
  for count in range(6):
    t.forward(length)
    t.left(360/12)
  t.forward(length)

  t.end_poly()
  

  return t.get_poly()

def polyRoundishTri (t, x, y, length):
  t.goto(x, y)
  t.setheading(90)
  t.begin_poly()

  for count in range(3):
    t.forward(length)
    t.left(60)
    t.forward(length//4)
    t.left(60)
  
  t.end_poly()
  

  return t.get_poly()

def wombotCursor():

    temporary = turtle.Turtle()

    screen = turtle.getscreen()

    delay = screen.delay()

    screen.delay(0)

    temporary.hideturtle()
    temporary.penup()

    wombot = turtle.Shape("compound")
    
    #legs
    leg1 = polyDodec (temporary, 0, 0, 4)
    wombot.addcomponent(leg1, "#a05024", "black")
    leg2 = polyDodec (temporary, 0, 36, 4)
    wombot.addcomponent(leg2, "#a05024", "black")
    leg3 = polyDodec (temporary, 36, 0, 4)
    wombot.addcomponent(leg3, "#a05024", "black")
    leg4 = polyDodec (temporary, 36, 36, 4)
    wombot.addcomponent(leg4, "#a05024", "black")
    #body
    body = polyTwoHalfDodec (temporary, 22, 4, 12)
    wombot.addcomponent(body, "#a05024", "black")
    #eyes
    eye1 = polyDodec (temporary, 30, 30,3)
    wombot.addcomponent(eye1, "white", "black")
    pupil1 = polyDodec (temporary, 32, 32,1)
    wombot.addcomponent(pupil1, "black", "black")
    eye2 = polyDodec (temporary, 30, 10,3)
    wombot.addcomponent(eye2, "white", "black")
    pupil2 = polyDodec (temporary, 32, 12,1)
    wombot.addcomponent(pupil2, "black", "black")
    eyelid1 = polyHalfDodec(temporary, 29, 29,3.5)
    wombot.addcomponent(eyelid1, "#a05024", "black")
    eyelid2 = polyHalfDodec(temporary, 29, 9,3.5)
    wombot.addcomponent(eyelid2, "#a05024", "black")
    #nose
    nose = polyRoundishTri(temporary, 44, 21, 8)
    wombot.addcomponent(nose, "black", "black")
    turtle.addshape("wombot", shape=wombot)
    del temporary

wombotCursor()  # creates and registers the "tank" cursor shape

turtle.shape("wombot")

turtle.up()  # get rid of the ink

# show our tank in motion

turtle.setheading(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)

turtle.done()
                 
