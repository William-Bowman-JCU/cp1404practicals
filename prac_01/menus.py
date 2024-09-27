name = input('Enter name: ')
MENU = '(H)ello\n(G)oodbye\n(Q)uit\n>>> '

choice = input(MENU).lower()
while choice != 'q':
    if choice == 'h':
        print(f'Hello {name}!')
    elif choice == 'g':
        print(f'Goodbye {name}')
    else:
        print('Invalid choice\n')
    choice = input(MENU).lower()
print('Finished.')
    