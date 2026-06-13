prompt = 'Please enter your age: '
prompt = prompt + ('\n(Enter "quit" if you do not have other '
'questions) ')
active = True

while active :
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print('Free')
        elif age < 12 :
            print('10 dollar')
        else :
            print('15 dollar')