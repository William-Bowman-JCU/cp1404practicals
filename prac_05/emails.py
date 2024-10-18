"""
Emails
Estimate: 5 minutes
Actual:   5 minutes
"""

email = input('Email: ')
name_to_email = {}
while email != '':
    name = email.split('@')[0].replace('.', ' ').title()
    edit_name = input(f'Is your name {name}? (Y/n) ').lower()
    if edit_name not in ['', 'y']:
        name = input('Name: ')
    name_to_email[name] = email
    email = input('Email: ')

print()
for name, email in name_to_email.items():
    print(f'{name} ({email})')