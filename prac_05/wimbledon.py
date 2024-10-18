"""
Word Occurrences
Estimate: 30 minutes
Actual:   30 minutes
"""
FILENAME = 'wimbledon.csv'

def main():
    """Read CSV and print the details about the Wimbledon champions"""
    records = get_data()
    champ_to_wins, countries = filter_records(records)
    display_data(champ_to_wins, countries)

def filter_records(records):
    """Make a set containing each country, and a dictionary of the winners"""
    champ_to_wins = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        champ = record[2]
        champ_to_wins[champ] = champ_to_wins.get(champ, 0) + 1
    return champ_to_wins,countries

def get_data():
    """Get data from the CSV and append it to a list of lists"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        return [line.strip().split(',') for line in in_file]

def display_data(champ_to_wins, countries):
    """Print champions & countries"""
    print('Wimbledon Champions:')
    for champ in champ_to_wins:
        print(f'{champ} {champ_to_wins[champ]}')
    print(f'\nThese 12 countries have won Wimbledon:\n{', '.join(sorted(countries))}')

main()