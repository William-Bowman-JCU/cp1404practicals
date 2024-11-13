from guitar import Guitar

def main():
    with open('prac_07/guitars.csv', 'r') as in_file:
        guitars = []
        for line in in_file:
            data = line.strip().split(',')
            guitar = Guitar(data[0], int(data[1]), float(data[2]))
            guitars.append(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    print('\nEnter new guitar details (blank to quit)')
    name = input('Name: ')
    while name != '':
        year = int(input('Year: '))
        cost = float(input('Cost: $'))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        name = input('Name: ')
    
    guitars.sort()
    print('\nNew guitars list:')
    for guitar in guitars:
        print(guitar)
    with open('prac_07/guitars.csv', 'w') as out_file:
        for guitar in guitars:
            print(f'{guitar.name},{guitar.year},{guitar.cost}', file=out_file)
main()




