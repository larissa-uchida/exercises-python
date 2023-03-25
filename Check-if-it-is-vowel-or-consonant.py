# Write a program that checks whether a typed letter is a vowel or a consonant.

letter = input('Type a letter: ')
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def verify_letter(letter, vowels):
    if letter in vowels:
        print(f'The letter {letter} is a vowel.')
    else:
        print(f'The letter {letter} is a consonant.')

verify_letter(letter, vowels)