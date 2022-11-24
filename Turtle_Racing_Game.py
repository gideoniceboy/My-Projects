import turtle
import time
import random


name1 = input("Enter the name of racer 1: ")
name2 = input("Enter the name of racer 2: ")
name3 = input("Enter the name of racer 3: ")

#Constant variables
HEIGHT = 600
WIDTH = 800
TITLE = "Turtle Racing"

#Creating screen
def create_screen():
	sc = turtle.Screen()
	sc.title(TITLE)
	sc.bgcolor("black")
	
def create_racers():
		
	writer = turtle.Turtle()
	writer.speed(10)
	writer.ht()
	writer.pu()
	writer.bk(85)
	writer.clear()
	writer.home()
	writer.color("cyan")
	writer.setposition(0,230)
	writer.write("Racing...",align="center", font=("Courier", 18, "bold"))

	#Starting_line
	Starting_line = turtle.Turtle()
	Starting_line.speed(0)
	Starting_line.color("green")
	Starting_line.shape("turtle")
	Starting_line.penup()
	Starting_line.setposition(-350,-HEIGHT/2+50)
	Starting_line.pendown()
	Starting_line.shapesize(0.5)
	Starting_line.forward(1000)
	#finishing_line.setheading(90)

	finishing_line = turtle.Turtle()
	finishing_line.speed(0)
	finishing_line.color("red")
	finishing_line.shape("turtle")
	finishing_line.penup()
	finishing_line.setposition(-350,200)
	finishing_line.pendown()
	finishing_line.shapesize(0.5)
	finishing_line.forward(1000)
	#finishing_line.setheading(90)

	posW = [WIDTH*1/4,-WIDTH*1/4,0]
	random.shuffle(posW)
	Col = ["white","pink","coral","green","yellow","brown","cyan","magenta"]
	random.shuffle(Col)

	
	race1 = turtle.Turtle()
	race1.speed(1)
	race1.color(Col[0])
	race1.shape("turtle")
	race1.setheading(90)


	
	race1.penup()
	race1.setposition(posW[0],-HEIGHT/2+50)
	race1.write(str(name1),align="center", font=("Courier", 14, "bold"))
	#race1.forward(100)

	race2 = turtle.Turtle()
	race2.speed(1)
	race2.color(Col[1])
	race2.shape("turtle")
	race2.setheading(90)
	
	race2.penup()
	race2.setposition(posW[1],-HEIGHT/2+50)
	race2.write(str(name2),align="center", font=("Courier", 14, "bold"))


	race3 = turtle.Turtle()
	race3.speed(1)
	race3.color(Col[2])
	race3.shape("turtle")
	race3.setheading(90)
	
	race3.penup()
	race3.setposition(posW[2],-HEIGHT/2+50)
	race3.write(str(name3),align="center", font=("Courier", 14, "bold"))

	race1.clear()
	race2.clear()
	race3.clear()

	#Racing
	running = True
	moving = True
	while running:

		if moving :
			speed1 = random.randrange(1,30)
			race1.forward(speed1)
			race1.write(name1,align="center", font=("Courier", 14, "bold"))

			speed2 = random.randrange(1,30)
			race2.forward(speed2)
			race2.write(name2,align="center", font=("Courier", 14, "bold"))

			speed3 = random.randrange(1,30)
			race3.write(name3,align="center", font=("Courier", 14, "bold"))
			race3.forward(speed3)
		race1.clear()
		race2.clear()
		race3.clear()
		x,y = race1.pos()
		x2,y2 = race2.pos()
		x3,y3 = race3.pos()
		if y >= 200 or 200 <= y2 or y3 >= 200:
			moving = False
			writer.clear()
			if y < y2 and y2 > y3:
				if moving == False:
					print("Blue Got: ",int(y2))
					print("White Got: ",int(y))
					print("Orange Got: ",int(y3))
					print("Blue Won!!!")
					Writer = turtle.Turtle()
					Writer.speed(10)
					Writer.ht()
					Writer.pu()
					Writer.bk(85)
					Writer.clear()
					Writer.home()
					Writer.color("cyan")
					Writer.setposition(0,230)
					Writer.write(str(name2)+" Won!!!",align="center", font=("Courier", 14, "bold"))
					running = False
			elif y > y2 and y > y3:
				if moving == False:
					print("White Got: ",int(y))
					print("Blue Got: ",int(y2))
					print("Orange Got: ",int(y3))
					print("White Won!!!")
					Writer = turtle.Turtle()
					Writer.speed(10)
					Writer.ht()
					Writer.pu()
					Writer.bk(85)
					Writer.clear()
					Writer.home()
					Writer.color("white")
					Writer.setposition(0,230)
					Writer.write(str(name1)+" Won!!!",align="center", font=("Courier", 14, "bold"))
					running = False
			elif y3 > y2 and y3 > y:
				if moving == False:
					print("Orange Got: ",int(y3))
					print("White Got: ",int(y))
					print("Blue Got: ",int(y2))
					print("Orange Won!!!")
					Writer = turtle.Turtle()
					Writer.speed(10)
					Writer.ht()
					Writer.pu()
					Writer.bk(85)
					Writer.clear()
					Writer.home()
					Writer.color("orange")
					Writer.setposition(0,230)
					Writer.write(str(name3)+" Won!!!",align="center", font=("Courier", 14, "bold"))
					running = False


#Main Game
create_screen()
create_racers()
time.sleep(5)