# Make a Program that asks how much you earn per hour and the number of hours worked in the month. Calculate and show your total salary in that month, knowing that 11% is deducted for Income Tax, 8% for INSS and 5% for the union, make a program that gives us:
# gross salary.
# how much did he pay to the INSS.
# How much did you pay the union?
# the net salary.
# calculate the discounts and the net salary, according to the table below:
# + Gross Salary: 
# - IR (11%): 
# - INSS (8%): ​​
# - Union (5%): 
# = Net Salary: 

hour = float(input('How much do you earn for hour? R$'))
hours = float(input('How much hours do you work per month? '))
salary = hour*hours

def values(salary):
    ir = salary-(salary*0.11)
    inss = salary-(salary*0.08)
    union = salary-(salary*0.05)
    net_salary = salary-(salary*0.24)
    print(f'Gross Salary: R${salary}')
    print(f'IR (11%): R${ir}')
    print(f'INSS (8%): R${inss}')
    print(f'Union (5%): R${union}')
    print(f'Net Salary (24%): R${net_salary}')
values(salary)