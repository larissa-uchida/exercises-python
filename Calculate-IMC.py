# Having as input data the height (h) of a person, build an algorithm that calculates his ideal weight, using the following formulas:
# For men: (72.7*h) - 58
# For women: (62.1*h) - 44.7

height = float(input('What is your height (m)? '))
gender = input('What is your gender? (F ou M) ')

def verify_gender(gender):
    while gender != 'Feminine' and gender != 'Male' and gender != 'F' and gender != 'M' and gender != 'f' and gender != 'm' and gender != 'feminine' and gender != 'male':
        gender = input('Invalid gender. Enter again: ')
    print('Calculating...')
verify_gender(gender)
    
def calcula_peso(gender, height):
    if gender in ['Feminine','F', 'f','Feminine']:
        resultado_f = int((62.1*height) - 44.7)
        print(f'Your IMC is {resultado_f}kg')
    else:
        resultado_m = int((72.7*height) - 58)
        print(f'Your IMC is {resultado_m}kg')
calcula_peso(gender, height)