# Tabajara Organizations decided to give their collaborators a salary increase and hired you to develop the program that will calculate the readjustments.
# Make a program that receives the salary of an employee and adjusts it according to the following criteria, based on the current salary:
# salaries up to BRL 280.00 (including): 20% increase
# salaries between BRL 280.00 and BRL 700.00: 15% increase
# salaries between BRL 700.00 and BRL 1500.00: 10% increase
# salaries from R$ 1500.00 onwards: 5% increase After the increase is carried out, inform on the screen:
# salary before readjustment;
# the percentage increase applied;
# the amount of the raise;
# the new salary, after the increase.

wage = float(input('What is your salary? R$'))

def calculate_readjustment(wage):
    if wage <= 280:
        wage1 = wage*1.20
        novo1 = wage1-wage
        print(f'Salary before adjustment: {wage} \nThe percentage applied was 20% \nThe amount of the increase was R${novo1} \nThe new salary is R${wage1}')
    elif wage <= 700:
        wage2 = wage*1.15
        novo2 = wage2-wage
        print(f'Salary before adjustment: {wage} \nThe percentage applied was 15% \nThe amount of the increase was R${novo2} \nThe new salary is R${wage2}')
    elif wage <= 1500:
        wage3 = wage*1.10
        novo3 = wage3-wage
        print(f'Salary before adjustment: {wage} \nThe percentage applied was 10% \nThe amount of the increase was R${novo3} \nThe new salary is R${wage3}')
    else:
        wage4 = wage*1.5
        novo4 = wage4-wage
        print(f'Salary before adjustment: {wage} \nThe percentage applied was 5% \nThe amount of the increase was R${novo4} \nThe new salary is R${wage4}')
calculate_readjustment(wage)