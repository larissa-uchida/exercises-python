print('---------------------------------------------------- \n              To finish, digit 0. \n----------------------------------------------------')

def verify_value():
    value = 1
    values = []
    while value != 0:
        value = float(input('Product value: R$'))
        values.append(value)
    print('----------------------------------------------------')
    total = sum(values)
    print('                 Lojas Tabajara')
    soma = 0
    for x in range(len(values)):
        soma = soma + 1
        print(f'Product {soma}: R$ {values[x]}')
    print(f'Total: {total}')
    print('----------------------------------------------------')
    payment = float(input('What is the value of the money received? R$'))
    print('----------------------------------------------------')
    change = payment - total
    print(f'Change: R$ {change}' )
verify_value()