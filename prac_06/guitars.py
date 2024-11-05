from guitar import Guitar

print('My guitars!')
guitars = []
name = input('Name: ')
while name != '': 
    year = int(input('Year: '))
    cost = float(input('Cost: $'))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f'{guitar} added.\n')
    name = input('Name: ')


print('These are my guitars:')
for i, guitar in enumerate(guitars, 1):
    print(f'Guitar {i} {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:10,.2f} {'(vintage)' if guitar.is_vintage() else ''}')