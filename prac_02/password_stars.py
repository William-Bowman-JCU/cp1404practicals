MINIMUM_LENGTH = 8

def main():
    """Perform functions"""
    password = get_password()
    print_hidden_password(password)

def get_password():
    """Get valid password"""
    password = input('Password: ')
    while len(password) < MINIMUM_LENGTH:
        print(f'Password too short, minimum password length is {MINIMUM_LENGTH}')
        password = input('Password: ')
    return password

def print_hidden_password(password):
    """Print stars amounting to the users password length"""
    print('*' * len(password))

main()