from guitar import Guitar

def main():
    with open('prac_07/guitars.csv', 'r') as in_file:
        guitars = []
        in_file.readline()
        for line in in_file:
            data = line.strip().split(',')
            guitar = Guitar(data[0], int(data[1]), float(data[2]))
            guitars.append(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
main()




