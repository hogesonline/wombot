#draw wombot

import turtle

#const
ORIGIN = 0
LENGTH_SHORT = 1
LENGTH_MED = 3
LENGTH_MED1 = 3.5
LENGTH_LONG = 4
LENGTH_TRI = 8
LENGTH_BODY = 12
FOOT = 36
BODY_X = 22
BODY_Y = 4
EYE_X = 30
EYE_Y1 = 30
EYE_Y2 = 10
PUP_X = 32
PUP_Y1 = 32
PUP_Y2 = 12
LID_X = 29
LID_Y1 = 29
LID_Y2 = 9
NOSE_X = 44
NOSE_Y = 21
BROWN = "#a05024"

def polyDodec (t, x, y, length):
  t.goto(x, y)
  t.setheading(0)

  t.begin_poly()
  
  for _ in range(12):
    t.forward(length)
    t.left(360/12)

  t.end_poly()
  

  return t.get_poly()

def polyHalfDodec (t, x, y, length):
  t.goto(x, y)
  t.setheading(180)
  t.begin_poly()

  for _ in range(6):
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

  for _ in range(6):
    t.forward(length)
    t.left(360/12)
  t.forward(length)
  for _ in range(6):
    t.forward(length)
    t.left(360/12)
  t.forward(length)

  t.end_poly()
  

  return t.get_poly()

def polyRoundishTri (t, x, y, length):
  t.goto(x, y)
  t.setheading(90)
  t.begin_poly()

  for _ in range(3):
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
    leg1 = polyDodec (temporary, ORIGIN, ORIGIN, LENGTH_LONG)
    wombot.addcomponent(leg1, BROWN, "black")
    leg2 = polyDodec (temporary, ORIGIN, FOOT, LENGTH_LONG)
    wombot.addcomponent(leg2, BROWN, "black")
    leg3 = polyDodec (temporary, FOOT, ORIGIN, LENGTH_LONG)
    wombot.addcomponent(leg3, BROWN, "black")
    leg4 = polyDodec (temporary, FOOT, FOOT, LENGTH_LONG)
    wombot.addcomponent(leg4, BROWN, "black")
    #body
    body = polyTwoHalfDodec (temporary, BODY_X, BODY_Y, LENGTH_BODY)
    wombot.addcomponent(body, BROWN, "black")
    #eyes
    eye1 = polyDodec (temporary, EYE_X, EYE_Y1,LENGTH_MED)
    wombot.addcomponent(eye1, "white", "black")
    pupil1 = polyDodec (temporary, PUP_X, PUP_Y1,LENGTH_SHORT)
    wombot.addcomponent(pupil1, "black", "black")
    eye2 = polyDodec (temporary, EYE_X, EYE_Y2,LENGTH_MED)
    wombot.addcomponent(eye2, "white", "black")
    pupil2 = polyDodec (temporary, PUP_X, PUP_Y2,LENGTH_SHORT)
    wombot.addcomponent(pupil2, "black", "black")
    eyelid1 = polyHalfDodec(temporary, LID_X, LID_Y1,LENGTH_MED1)
    wombot.addcomponent(eyelid1, BROWN, "black")
    eyelid2 = polyHalfDodec(temporary, LID_X, LID_Y2,LENGTH_MED1)
    wombot.addcomponent(eyelid2, BROWN, "black")
    #nose
    nose = polyRoundishTri(temporary, NOSE_X, NOSE_Y, LENGTH_TRI)
    wombot.addcomponent(nose, "black", "black")
    turtle.addshape("wombot", shape=wombot)
    del temporary

wombotCursor()  # creates and registers the "wombot" cursor shape

turtle.shape("wombot")
turtle.up()  # get rid of the ink

# show our wombot in motion
turtle.speed(1)
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
turtle.left(90)
turtle.forward(100)

turtle.done()
                 
