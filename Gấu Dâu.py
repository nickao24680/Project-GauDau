#-*- coding: UTF-8 -*-

import turtle as t

 

"""

=================================================

@Project ->Adversity Awake Strawberry Bear Series

@category     : Strawberry Bear->Strawberry Bear 3

@Author  : Nguyễn Văn Đức

@Date    : 2007/02/01 0:00

@Desc    :0327463234

=================================================

"""

# Set background color, window position and size

 

t.colormode(255)# Color Mode

t.speed(0)

t.screensize(850,760,"white")#Canvas size background color

t.setup(width=850, height=760,startx=None, starty=None) #The size and starting coordinates of the drawing window

#t.bgpic("ditu3.gif")

t.title("Nguyễn Văn Đức (ADMIN)")#Sets the title of the drawing window

t.resizemode('noresize')  #Resizing Mode:auto,user,noresize

t.tracer(1)  

 

 

 

 

def mlingpen(x, y):

    t.penup()

    t.goto(x, y)

    t.pendown()

 

 

def rose(): #rose

    t.seth(90)

    mlingpen(-225, -60)

    t.pensize(10)

    t.pencolor("#035025")

    t.circle(300,30)

    mlingpen(-240, 70)

 

    t.pensize(2)

    t.color("#000000", "#22ac38")

    t.seth(12)

    mlingpen(-235,40)

    t.lt(40)

    t.fd(50)

    t.begin_fill()

    t.circle(-150,30)

    t.circle(-2,140)

    t.circle(-150,43)

    t.up()

    t.end_fill()

    mlingpen(-235,40)

    t.lt(330)

    t.fd(50)

    t.begin_fill()

    t.circle(-150,30)

    t.circle(-2,140)

    t.circle(-150,43)

    t.up()

    t.end_fill()

    mlingpen(-235,40)

    t.lt(260)

    t.fd(50)

    t.begin_fill()

    t.circle(-150,30)

    t.circle(-2,140)

    t.circle(-150,43)

    t.up()

    t.end_fill()

    t.pensize(2)

    t.seth(12)

    mlingpen(-210,60)  

    t.begin_fill()

    t.color("#000000", "#f8c0c8")

    t.circle(50,150)

    t.rt(20)

    t.fd(40)

    t.rt(40)

    t.circle(15,130)

    t.fd(50)

    t.circle(15,80)

    t.up()

    t.end_fill()

    t.pensize(2)

    t.seth(12)

    mlingpen(-210,65)  

    t.begin_fill()

    t.color("#f5aab5", "#f5aab5")

    t.circle(34,150)

    t.rt(20)

    t.fd(30)

    t.rt(40)

    t.circle(10,130)

    t.fd(50)

    t.circle(15,80)

    t.up()

    t.end_fill()

    t.pensize(2)

    t.seth(12)

    mlingpen(-210,65)  

    t.begin_fill()

    t.color("#f198a5", "#f198a5")

    t.circle(30,150)

    t.rt(20)

    t.fd(30)

    t.rt(40)

    t.circle(10,130)

    t.fd(50)

    t.circle(15,80)

    t.up()

    t.end_fill()

    t.pensize(2)

    t.seth(12)

    mlingpen(-210,65)  

    t.begin_fill()

    t.color("#ee8998", "#ee8998")

    t.circle(20,150)

    t.rt(20)

    t.fd(30)

    t.rt(40)

    t.circle(10,130)

    t.fd(50)

    t.circle(15,80)

    t.up()

    t.end_fill()

    mlingpen(-220,80)  

    t.begin_fill()

    t.color("#e56e7f", "#e56e7f")

    t.circle(15,200)

    t.rt(20)

    t.fd(30)

    t.rt(40)

    t.circle(10,130)

    t.fd(50)

    t.circle(15,80)

    t.up()

    t.end_fill()

    t.seth(35)

    mlingpen(-230,90)  

    t.begin_fill()

    t.color("#000000", "#fda7b5")

    t.circle(50,50)

    t.rt(40)

    t.circle(25,200)

    t.up()

    t.end_fill()

    t.seth(130)

    mlingpen(-294.51,142.14)  

    t.begin_fill()

    t.color("#000000", "#fdadb8")

    t.circle(20,100)

    t.rt(90)

    t.circle(10,180)

    t.rt(90)

    t.circle(15,130)

    t.rt(110)

    t.circle(30,130)

    t.rt(50)

    t.circle(50,80)

    t.up()

    t.end_fill()

    t.seth(80)

    mlingpen(-240,140)  

    t.begin_fill()

    t.color("#000000", "#fe8e9e")

    t.circle(10,100)

    t.rt(90)

    t.circle(12,150)

    t.rt(90)

    t.circle(15,130)

    t.rt(50)

    t.circle(50,80)

    t.rt(10)

    t.circle(50,80)

    t.goto(-240,140)

    t.up()

    t.end_fill()

    t.seth(80)

    mlingpen(-250,140)  

    t.begin_fill()

    t.color("#f9788b", "#f9788b")

    t.circle(5,130)

    t.rt(90)

    t.circle(10,170)

    t.rt(100)

    t.circle(10,130)

    t.rt(70)

    t.circle(40,80)

    t.rt(40)

    t.circle(30,30)

    t.goto(-250,140)

    t.up()

    t.end_fill()

    t.seth(10)

    mlingpen(-245, 80)

    t.begin_fill()  

    t.color("#000000", "#ef5f7a")

    t.seth(35)

    t.circle(30,80)

    t.rt(80)

    t.circle(10,150)

    t.rt(80)

    t.circle(17,200)

    t.rt(60)

    t.circle(29,120)

    t.goto(-245, 80)

    t.up()

    t.end_fill()

    t.seth(10)

    mlingpen(-250, 85)

    t.begin_fill()  

    t.color("#ef758c", "#ef758c")

    t.seth(35)

    t.circle(25,80)

    t.rt(80)

    t.circle(6,150)

    t.rt(80)

    t.circle(12,210)

    t.rt(60)

    t.circle(23,120)

    t.goto(-250, 85)

    t.up()

    t.end_fill()

    t.seth(0)  

    mlingpen(-250,125)

    t.pensize(5)

    t.dot("#ff4969")

    t.pensize(2)

    mlingpen(-266.97,121.26)

    t.pencolor("#321320")

    t.fillcolor("#f04969")

    t.begin_fill()

    t.rt(80)

    t.circle(12,150)

    t.rt(80)

    t.circle(6,270)

    t.rt(150)

    t.circle(10,180)

    t.up()

    t.end_fill()

    #t.color("#000000", "#f04969")

    t.seth(-70)

    mlingpen(-210,100)  

    t.begin_fill()

    t.color("#000000", "#f04969")

    t.rt(20)

    t.fd(30)

    t.circle(-40,170)

    t.lt(20)

    t.fd(20)

    t.goto(-210,100)

    t.up()

    t.end_fill()

    t.seth(-70)

    mlingpen(-215,90)  

    t.begin_fill()

    t.color("#ee627d", "#ee627d")

    t.rt(20)

    t.fd(20)

    t.circle(-35,170)

    t.lt(20)

    t.fd(15)

    t.goto(-220,90)

    t.up()

    t.end_fill()

    t.seth(-70)

    mlingpen(-220,80)  

    t.begin_fill()

    t.color("#f47a91", "#f47a91")

    t.rt(20)

    t.fd(10)

    t.circle(-28,170)

    t.lt(20)

    t.fd(10)

    t.goto(-220,90)

    t.up()

    t.end_fill()

    t.seth(150)

    mlingpen(-220,100)  

    t.begin_fill()

    t.color("#000000", "#f7cad1")

    t.circle(20,80)

    t.rt(10)

    t.circle(-40,70)

    t.rt(10)

    t.circle(20,80)

    t.rt(5)

    t.circle(5,180)

    t.rt(80)

    t.circle(20,70)

    t.rt(80)

    t.circle(40,60)

    t.rt(10)

    t.circle(40,110)

    t.goto(-220,100)

    t.up()

    t.end_fill()

    t.seth(150)

    mlingpen(-220,98)  

    t.begin_fill()

    t.color("#ffe9f2", "#ffe9f2")

    t.circle(15,80)

    t.rt(7)

    t.circle(-45,75)

    t.rt(8)

    t.circle(20,50)

    t.rt(5)

    t.circle(2,200)

    t.rt(80)

    t.circle(15,85)

    t.rt(80)

    t.circle(40,60)

    t.rt(20)

    t.circle(30,70)

    t.goto(-220,98)

    t.up()

    t.end_fill()

    t.seth(150)

    mlingpen(-180,55)  

    t.begin_fill()

    t.color("#000000", "#f7cad1")

    t.circle(30,80)

    t.rt(10)

    t.circle(-60,70)

    t.rt(5)

    t.circle(30,80)

    t.rt(5)

    t.circle(5,180)

    t.rt(90)

    t.circle(30,80)

    t.rt(80)

    t.circle(40,70)

    t.circle(20,50)

    t.rt(90)

    t.circle(20,95)

    t.goto(-180,55)

    t.up()

    t.end_fill()

    t.seth(150)

    mlingpen(-190,50)  

    t.begin_fill()

    t.color("#f7e0e3", "#f7e0e3")

    t.circle(25,80)

    t.rt(8)

    t.circle(-55,75)

    t.rt(3)

    t.circle(25,60)

    t.rt(6)

    t.circle(5,200)

    t.rt(90)

    t.circle(30,80)

    t.rt(80)

    t.circle(22,80)

    t.circle(20,40)

    t.rt(80)

    t.circle(15,90)

    t.goto(-190,50)

    t.up()

    t.end_fill()

 

 

 

mling_circle_list = iter([  # Each arc segment (radius, arc angle)

    (18, 360), (14, 360), (10, 360), (6, 360),

    (18, 360), (14, 360), (10, 360), (6, 360),

])

 

 

def mling_draw_eyeball(zb1,zb2,zb3,zb4):  

    for zb, color_ in zip([zb1,zb2,zb3,zb4], ['#ffffff', '#482d08', '#000000', '#ffffff']):

        t.penup()

        t.goto(*zb)

        t.pendown()

        t.begin_fill()

        t.setheading(0)

        t.color(color_)

        t.pencolor('#000000')

        t.pensize(2)

        t.circle(*next(mling_circle_list))

        t.end_fill()

 

t.penup()

p = t.home()

t.pencolor("#321320")

t.fillcolor("#cb3263")

t.pensize(4)

t.goto(120,110)

t.pendown()

t.begin_fill()

t.goto(200,0)

t.left(-40)

t.circle(-110,105)

t.left(75)

t.goto(170,-110)

t.left(-80)

t.circle(30,40)

t.left(60)

t.circle(-80,70)

t.left(83)

t.circle(-35,95)

t.goto(60,-270)

t.left(-80)

t.circle(-65,70)

t.left(63)

t.circle(35,30)

t.left(130)

t.circle(-65,70)

t.goto(-120,-270)

t.left(-110)

t.circle(-35,80)

t.left(83)

t.circle(-80,50)

t.left(60)

t.circle(-80,60)

t.left(60)

t.circle(30,30)

t.left(20)

t.circle(80,80)

t.left(-105)

t.circle(-70,150)

t.left(50)

t.circle(-170,50)

t.goto(120,110)

#Author:Adversity Awake

t.end_fill()

t.penup()

p = t.home()

t.pencolor("#321320")

t.fillcolor("#ffffff")

t.pensize(4)

t.goto(90,60)

t.pendown()

t.begin_fill()

t.right(30)

t.circle(-130,360)

t.end_fill()

t.penup()

p = t.home()

t.pencolor("#321320")

#t.fillcolor("#f3d2ad")

t.fillcolor("#015426")

t.pensize(4)

t.goto(-250,-55)

t.dot("blue")

t.seth(0)

t.pendown()

t.begin_fill()

t.right(-55)

#t.circle(-45,270)

t.circle(-35,70)

t.goto(-200,-165)

t.goto(-250,-165)

t.goto(-220,-75)

t.goto(-250,-55)

t.end_fill()

 

rose()

 

t.penup()

p = t.home()

t.pencolor("#321320")

#t.fillcolor("#f3d2ad")

t.fillcolor("#f3d2ad")

t.pensize(4)

t.goto(185,-90)

t.pendown()

t.begin_fill()

t.right(140)

t.circle(43,95)

t.goto(185,-90)

t.end_fill()

t.penup()

t.seth(0)

t.pencolor('#321320')

t.fillcolor('#cb3263')

t.pensize(4)

t.begin_fill()

t.goto(21,0)

t.pendown()

t.circle(123,134)

t.left(-90)

t.circle(40,185)

t.left(-60)

t.circle(120,60)

t.left(-90)

t.circle(50,200)

t.left(-90)

t.circle(100,100)

t.left(-12)

t.circle(100,40)

t.goto(21,0)

t.penup()

#Author:Adversity Awake

t.end_fill()

t.penup()

t.goto(0, 0)

t.seth(0)

t.pencolor('#321320')

t.fillcolor('#ffffff')

t.pensize(4)

t.begin_fill()

t.goto(-70,210)

t.left(140)

t.pendown()

t.circle(30,200)

t.goto(-70,210)

t.penup()

t.end_fill()

t.penup()

t.goto(0, 0)

t.seth(0)

t.pencolor('#321320')

t.fillcolor('#ffffff')

t.pensize(4)

t.begin_fill()

t.goto(90,220)

t.left(45)

t.pendown()

t.circle(22,200)

t.goto(90,220)

t.penup()

t.end_fill()

t.penup()

t.goto(0, 0)

t.seth(0)

t.pencolor('#321320')

t.fillcolor('#ffffff')

t.pensize(4)

t.begin_fill()

t.left(-98)

t.left(90)

t.goto(18,10)

t.pendown()

t.circle(100,134)

t.left(10)

t.circle(110,30)

t.left(10)

t.circle(160,40)

t.circle(85,40)

t.left(2)

t.circle(95,40)

t.left(5)

t.circle(95,60)

t.goto(18,10)

t.penup()

t.end_fill()

t.penup()

p = t.home()

t.pencolor("#321320")

t.fillcolor("#8f3a52")

t.pensize(2)

t.goto(25,240)

t.pendown()

t.begin_fill()

t.goto(60,235)

t.left(30)

t.fd(8)

t.left(90)

t.fd(22)

t.circle(90, 8)

t.left(20)

t.circle(90, 8)

t.left(20)

t.circle(90, 20)

t.left(40)

t.circle(50, 20)

t.end_fill()

t.penup()

t.pensize(12)

t.goto(-2,250)

t.pencolor("#4D1F00")

t.fillcolor("#4D1F00")

t.pendown()

t.goto(60,240)

t.end_fill()

t.penup()

p = t.home()

t.pencolor("#321320")

t.fillcolor("#8f3a52")

t.pensize(2)

t.goto(-55,193)

t.pendown()

t.begin_fill()

t.left(65)

t.circle(-90, 25)

t.goto(-10,230)

t.left(30)

t.fd(8)

t.left(90)

t.fd(18)

t.circle(90, 8)

t.left(20)

t.circle(90, 10)

t.left(40)

t.circle(90, 30)

t.left(30)

t.circle(40, 20)

t.penup()

t.end_fill()

t.pensize(12)

t.goto(-63,195)

t.pencolor("#4D1F00")

t.fillcolor("#4D1F00")

t.pendown()

t.left(100)

t.circle(-85,45)

t.end_fill()

 

mling_draw_eyeball((-20,180), (-23,185), (-25,188), (-30,200))

mling_draw_eyeball((30, 193), (27, 200), (25,203), (20,213))

 

t.penup()

p = t.home()

t.pencolor("#321320")

t.fillcolor("#8f3a52")

t.pensize(3)

t.goto(25,105)

p = t.pos()

t.pendown()

t.begin_fill()

t.circle(85, 65)

t.left(16)

t.circle(30, 55)

t.left(20)

t.circle(145, 58)

t.left(8)

t.circle(20, 55)

t.left(8)

t.circle(50, 65)

t.left(-5)

t.circle(310, 8)

t.end_fill()

t.penup()

t.goto(0, 0)

t.seth(0)

t.pencolor('#321320')

t.fillcolor('#a93e54')

t.pensize(3)

t.begin_fill()

t.left(-20)

t.goto(9,66)

t.pendown()

t.circle(68,40)

t.left(10)

t.circle(65,40)

t.left(160)

t.circle(-75,85)

t.left(158)

t.circle(48,37)

t.goto(9,66)

t.penup()

t.end_fill()

t.color('#987824')

t.penup()

t.goto(260,60)

t.pendown()

t.write("  我\n  爱\n  你\n    I\nLOVE\n YOU\n",align="center",font=("Bold",20,"normal"))

t.penup()

t.goto(290,183)

t.pendown()

t.write("阮\n文\n德\n 。\n",align="center",font=("Bold",10,"normal"))

t.hideturtle()

t.done()