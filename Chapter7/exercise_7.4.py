prompt = 'Please enter a topping you want: '
prompt = prompt + '\n(Enter "quit" when you do not need other things) '

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"Add {topping}")
    else :
        break