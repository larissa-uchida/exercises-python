# Make a program that asks a person 5 questions abort a crime. The questions are:
# "Did yor call the victim?"
# "Were yor at the crime scene?"
# "Do yor live near the victim?"
# "Owed to the victim?"
# "Have yor ever worked with the victim?" The program shorld ultimatelyue a rating on the person's participation in the crime. If the person responds positively to 2 questions, he must be cified as "Suspect", between 3 and 4 as "Accomplice" and 5 as "Murderer". Otherwise, he will be cified as "Innocent"

print('---------------------------------------------------- \n             Responda com yes or no: \n----------------------------------------------------')

def verify_suspect():
    amount = 0
    call = input('Did yor call the victim?? ')
    while call not in "yes, Yes, no, No": 
        call = input('Answer just with yes or no: ')
    if call in 'yes, Yes, YES':
        amount += 1

    local = input('Were you at the crime scene?? ')
    while local not in "yes, Yes, no, No":
        local = input('Answer just with yes or no: ')
    if local in 'yes, Yes, YES':
        amount += 1

    home = input('Do you live near the victim? ')
    while home not in "yes, Yes, no, No":
        home = input('Answer just with yes or no: ')
    if home in 'yes, Yes, YES':
        amount += 1

    moneylender = input('Do you owe something to the victim?? ')
    while moneylender not in "yes, Yes, no, No":
        moneylender = input('Answer just with yes or no: ')
    if moneylender in 'yes, Yes, YES':
        amount += 1

    work = input('Have you ever worked with the victim?? ')
    while work not in "yes, Yes, no, No": 
        work = input('Answer just with yes or no: ')
    if work in 'yes, Yes, YES':
        amount += 1

    if amount == 2:
        print('Classification: Suspect')
    elif amount in range(3,4):
        print('Classification: Accomplice')
    elif amount == 5:
        print('Classification: Murderer')
    else: 
        print('Classification: Innocent')
verify_suspect()