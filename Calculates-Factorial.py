from math import prod
num = int(input('Enter a number: '))

def factorial():
    lista = []
    for i in range(1, num+1):
        lista.append(i)
    result = prod(lista)
    lista.reverse()
    print(f'{num}! =', end=' ')
    print(" . ".join(map(str, lista)), end=' = ')
    print(f'{result}')
factorial()