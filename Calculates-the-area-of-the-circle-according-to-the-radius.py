# Write a program that asks for the radius of a circle, calculates and displays its area.

radius = float(input('What is the radius of the circle? '))

def calc(radius):
    answer = (radius * radius)*3.14
    print(f'The area of the circle is {answer}')
calc(radius)

