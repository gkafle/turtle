from turtle import *

color("WhiteSmoke")
bgcolor("MidnightBlue")

def drawStar():
	pendown()
	begin_fill()

	for side in range(5):
		left(144)
		forward(100)
		
	end_fill()
	penup()

drawStar()
forward(200)
drawStar()
left(250)
forward(300)
drawStar()
left(300)
done()
