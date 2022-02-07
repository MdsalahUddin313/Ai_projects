#calculate area of circle
import math
print('Practice Problem 01:-')
radius = input("Enter the area of a circle please-")
radius = float(radius)
area = (3.1416*pow(radius,2))
print('The area of circle is:: ',area,';;;')

#find country in SAARC organization
print('###################################')
print('Practice Problem 02:-')
country=input("please enter your Country:")
saarc =['Bangladesh','Nepal','Bhutan','India','Afganistan','Pakistan','Srilanka']
if country in saarc :
    print('your country',country,'is a member of SAARC')
else:
    print('your country',country,'is not a member of saarc')
print('program terminated')

#Grade point
marks=input("Enter your marks::")
marks=int(marks)
if marks<40:
    print('F')
elif marks>40 & marks<=59:
    print('C')
elif marks<=75 & marks>60:
    print('B')
elif marks>=76 & marks <80:
    print('A-')
elif marks>=80:
    print('A+')
else:
    print('Invalid grade numver')
#leap year

year=input('Enter A year:')
year=int(year)
if(year%4==0):
    print('The year ',year,'is leap year')
else:
    print('The year ',year,'is not leap year ')

#Turtle identification making a square
import turtle
turtle.shape("turtle")
turtle.speed(2)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.exitonclick()

