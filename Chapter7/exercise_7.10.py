prompt = 'If you could visit one place in the world, where would you go?'
visit_dict = {}
active = True

while active:
    name = input('What is your name? ')
    place = input(prompt)
    visit_dict[name] = place

    question = input('Do you have other destination? yes or no' )
    if question == 'no':
        active = False

for name , place in visit_dict.item():
    print(f'{name} want to visit {place}')