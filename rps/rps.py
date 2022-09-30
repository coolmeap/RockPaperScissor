import turtle
import random

sc = turtle.Screen()
sc.bgcolor('black')
sc.setup(width=700, height=700)
#sad="sad.gif"
trophy="trophy.gif"
sc.addshape(trophy)
#sc.addshape(sad)
text = turtle.Turtle()
text.color('white')
text.penup()
text.setpos(0, 250)
cfont = ("Arial", 30)
wfont = ("Arial",20)
text.write("ROCK-PAPER-SCISSOR", align="center", font=cfont)
text.hideturtle()
#computer
computer = turtle.Turtle()
computer.color('white')
computer.penup()
computer.setpos(-150, -100)


computer.write("", align="center", font=cfont)
computer.hideturtle()

#player
text =0
player = turtle.Turtle()
player.color('white')
player.penup()
player.setpos(150, -100)

player.write("", align="center", font=cfont)
player.hideturtle()

#result
result = turtle.Turtle()
result.speed(0)
result.penup()
result.setpos(-50,-200)
result.write("", align="center", font=cfont)
result.hideturtle()


#fighter
fighter1=turtle.Turtle()
fighter1.setpos(-200,100)
fighter1.color('red')
fighter1.penup()
fighter1.shapesize(3)


fighter2=turtle.Turtle()
fighter2.setpos(-200,90)
fighter2.color('blue')
fighter2.penup()
fighter2.shapesize(3)

#finish line
finish=turtle.Turtle()
finish.speed(0)
finish.shape('square')
finish.shapesize(4)
finish.penup()
finish.setpos(200,95)
finish.write("",font=cfont)
finish.color('white')

win_text =turtle.Turtle()
win_text.speed(0)
win_text.color('yellow')
win_text.penup()
win_text.setpos(100,135)
win_text.hideturtle()

def check_win ():
    if fighter1.distance (finish) < 10:
        win_text.write("player win", font=wfont)
        win_shape()
    if fighter2.distance (finish) < 10:
        win_text.write("player lose", font=wfont)
        lose_shape()

#try again
def try_again(x,y):
    win_text.clear()
    result.clear()
    shape.hideturtle()
    fighter1.setpos(-200,100)
    fighter2.setpos(-200,90)
    computer.clear()
    player.clear()
    
tryagain=turtle.Turtle()
tryagain.shape('circle')
tryagain.shapesize(3)
tryagain.speed(0)
tryagain.color('green')
tryagain.onclick(try_again)
tryagain.penup()
tryagain.setpos(-196,-250)

trytext=turtle.Turtle()
trytext.color('white')
trytext.penup()
trytext.speed(0)
trytext.hideturtle()
trytext.setpos(-225,-260)
trytext.write('Try again',font=('Arial',10,'bold'))

#shape
shape=turtle.Turtle()
shape.speed(0)
shape.hideturtle()
shape.penup()
shape.setpos(-40,200)


def win_shape():
    shape.pendown()
    shape.showturtle()
    shape.shape(trophy)
def lose_shape():
    shape.pendown()
    shape.showturtle()
    shape.shape(sad)

#exit

exitb=turtle.Turtle()
exitb.shape('circle')
exitb.shapesize(3)
exitb.speed(0)
exitb.color('orange')
#exitb.onclick()
exitb.penup()
exitb.setpos(200,-250)


exittext=turtle.Turtle()
exittext.color('white')
exittext.penup()
exittext.speed(0)
exittext.hideturtle()
exittext.setpos(190,-260)
exittext.write('Exit',font=('Arial',10,'bold'))

####################################
        
#main
def cal():
    if (text=="rock" and computertext=="rock") or (text=="scissors" and computertext=="scissors") or(text=="paper" and computertext=="paper"):
        result.color('yellow')    
        result.write("DRAW",font=cfont)
        check_win ()
    elif (text=="rock" and computertext=="paper") or (text=="scissors" and computertext=="rock") or(text=="paper" and computertext=="scissors"):
        result.color('red')
        result.write("LOSE",font=cfont)
        fighter2.forward(100)
        check_win ()
    elif (text=="paper" and computertext=="rock") or (text=="scissors" and computertext=="paper") or(text=="rock" and computertext=="scissors"):
        result.color('blue')
        result.write("WIN",font=cfont)
        fighter1.forward(100)
        check_win ()
    else:
        result.color('white')
        result.write("Wrong input",font=cfont)

        
   

computertext =""
def randomChoose(x, y):
    global text
    global computertext
    computertext = random.choice(['rock','paper','scissors'])
    computer.clear()
    player.clear()
    result.clear()
    text = sc.textinput("player","Choice: \nrock, paper, scissors ")
    computer.write("COMPUTER\n{}".format(computertext), align="center", font=cfont)
    player.write("PLAYER\n{}".format(text), align="center", font=cfont)
    cal()
           

#play button
button = turtle.Turtle()
button.speed(0)
button.color('white')
button.shape('circle')
button.shapesize(3)
button.onclick(randomChoose)
button.penup()
button.setpos(0,-250)

playtext=turtle.Turtle()
playtext.color('black')
playtext.penup()
playtext.speed(0)
playtext.hideturtle()
playtext.setpos(-10,-260)
playtext.write('Play',font=('Arial',10,'bold'))

     

sc.mainloop()

