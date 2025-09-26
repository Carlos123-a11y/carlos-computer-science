#1
'''
def abc_un(a):

    prefix_word = "un"+a
 
    return(prefix_word)

word=input('enter a word:')

print(abc_un(word))

#2

def abc_s(b):

    postfix_word=b+'s'

    return(postfix_word)

word=input('enter a word:')

print(abc_s(word))

#3
#math.pi
import math
diameter=int(input('enter the diameter:'))
def circle_dia(diameter):

    radius=diameter/2
    area=math.pi*radius**2
    return area
print(circle_dia(diameter))

#4
import math
height=int(input('enter the height:'))
lenght=int(input('enter the lenght:'))
def rectangle_area(lenght,height): 
    area=height*lenght
    return area


print(rectangle_area(lenght,height))

#5
import math
user_input=int(input('enter 1 for the circle and 2 for the perimeter of the circle:'))
diameter=int(input('enter the diameter:'))
def circle_dia(diameter):

    radius=diameter/2
    area=math.pi*radius**2
    return area
print(circle_dia(diameter))

import math
user_two=float(input('enter the radius of the circle:'))
def circle_radius(radius):
    radius=user_two
    perimeter=2*math.pi*radius
    return(perimeter)
print(circle_radius(user_two))

import math
user_lenght=float(input('enter the lenght of the rectangle:'))
user_height=float(input('enter the height of the rectangle:'))
def area(lenght,height):
    lenght=user_lenght
    height=user_height
    area2=lenght*height
    return area2
print(area(user_lenght,user_height))
'''
import math
user_2=float(input('enter the lenght:'))
user_3=float(input('enter the height:'))
def perimeter(lenght,height):
    lenght=user_2
    height=user_3
    perimeter=lenght+lenght+height+height
    return perimeter
print(perimeter(user_2,user_3))

    




