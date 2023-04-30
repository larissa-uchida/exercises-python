# Python Exercises

Here are some basic codes in python I made to put into practice what I learned only in theory, like this code that calculates the factorial:

```
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
```
