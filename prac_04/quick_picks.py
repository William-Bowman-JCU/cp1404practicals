import random

NUMBER_OF_COLUMNS = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
number_of_rows = int(input('How many quick picks? '))

for i in range(number_of_rows):
    numbers = []
    for i in range(NUMBER_OF_COLUMNS):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in numbers:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        numbers.append(number)
    numbers_string = ' '.join([f'{number:2}' for number in sorted(numbers)])
    print(numbers_string)