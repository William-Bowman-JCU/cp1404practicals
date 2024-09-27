MINIMUM_LENGTH = 8

def main():
    password = get_password()
    print_hidden_password(password)

def get_password():
    password = input('Password: ')
    while len(password) < MINIMUM_LENGTH:
        print(f'Password too short, minimum password length is {MINIMUM_LENGTH}')
        password = input('Password: ')
    return password


def print_hidden_password(password):
    print('*' * len(password))

main()