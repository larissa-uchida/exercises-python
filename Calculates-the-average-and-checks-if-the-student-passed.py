# Write a program to read two partial grades from a student. The program must calculate the average achieved per student and present:
# The message "Approved", if the average achieved is greater than or equal to seven;
# The message "Failed", if the average is less than seven;
# The message "Approved with Distinctions", if the average is equal to ten.

grade1, grade2 = map(int, input('What were the students two grades? ').split())

def calculates_average(grade1, grade2):
    average = (grade1+grade2)/2
    if average == 10:
        print('Approved without distinction!')
    elif average >= 7:
        print('Approved!')
    else:
        print('Failed :(')

calculates_average(grade1, grade2)