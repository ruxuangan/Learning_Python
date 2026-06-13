sandwich_orders = ['veggie', 'pastrami', 'pastrami', 'grilled cheese', 'turkey', 'pastrami', 'roast beef']
finished_sandwiches = []

print('pastrami is sold out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    making = sandwich_orders.pop()
    print(f'I made your {making}')
    finished_sandwiches.append(making)

print('The following sandwiched are ready')
for sandwich in finished_sandwiches:
    print(sandwich)