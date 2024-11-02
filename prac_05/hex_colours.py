HEX_COLOURS = {
    'Absolute Zero': '#0048ba',
    'Acid Green': '#b0bf1a',
    'Alice Blue': 'f0f8ff',
    'Alizarin Crimson': '#e32636',
    'Amaranth': '#e52b50',
    'Amber': '#ffbf00',
    'Amethyst': '#9966cc',
    'Antique White': '#faebd7',
    'Apricot': '#fbceb1',
    'Aqua': '#00ffff'
}
for colour in HEX_COLOURS:
    print(f'{colour:16} - {HEX_COLOURS[colour]}') 
print()
user_colour = input('Enter colour name: ').title()

while user_colour != '':
    try:
        print(HEX_COLOURS[user_colour])
    except KeyError:
        print('Invalid colour name')
    user_colour = input('Enter colour name: ').title()
    
