"""
Emails
Estimate: 5 minutes
Actual:   5 minutes
"""

email = input('Email: ')
names = {}
while email != '':
    name = email.split('@')[0].replace('.', ' ').title()
    edit_name = input(f'Is your name {name}? (Y/n) ').lower()
    if edit_name not in ['', 'y']:
        name = input('Name: ')
    names[name] = email
    email = input('Email: ')

print()
for name, email in names.items():
    print(f'{name} ({email})')