from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = 'q)uit, c)hoose taxi, d)rive\n>>> '

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    print("Let's drive!")
    choice = get_choice()
    while choice != 'q':
        taxi_choice = None
        if choice == 'c':
            taxi_choice = choose_taxi(taxis)
        if choice == 'd':
            if taxi_choice == None:
                print('You need to choose a taxi before you can drive')
            else:
                taxi_choice.start_fare()
                distance = get_valid_number('Drive how far? ')
                taxi_choice.drive(distance)
                fare = taxi_choice.get_fare()
                print(f'Your {taxi_choice.name} cost you ${fare:.2f}')
                total_bill += fare
        print(f'Bill to date: ${total_bill:.2f}')
        choice = get_choice()
    print(f'Total trip cost: ${total_bill:.2f}')
    print('Taxis are now:')
    list_taxis(taxis)


def list_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi}')

def choose_taxi(taxis):
    list_taxis(taxis)
    index = get_valid_number('Choose taxi: ')
    if index > len(taxis) - 1 or index < 0:
        print('Invalid taxi choice')
    else:
        return taxis[index]

def get_choice():
    """Get a valid menu choice"""
    choice = input(MENU).lower()
    while choice not in ('q', 'c', 'd'):
        print('Invalid choice')
        choice = input(MENU).lower()
    return choice

def get_valid_number(prompt, blank=False):
    """Get a non negative number, and optionally a blank string"""
    value = input(prompt)
    while isinstance(value, str):
        try:
            if int(value) >= 0:
                return int(value)
            else:
                print('Invalid input; enter a valid number')
                value = input(prompt)
        except:
            if blank and value == '':
                return value
            print('Invalid input; enter a valid number')
            value = input(prompt)

main()