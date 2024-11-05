from project import Project
from datetime import datetime
MENU = '\nMenu:\n(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit\n>> '

def main():
    choice = get_choice()
    while choice != 'q':
        if choice == 'l':
            projects = []
            in_filename = input('Filename: ')
            try:
                with open(f'prac_07/{in_filename}', 'r') as in_file:
                    in_file.readline()
                    for line in in_file:
                        data = line.strip().split('\t')
                        # Use datetime here
                        project = Project(data[0], data[1], int(data[2]), float(data[3]), float(data[4]))
                        projects.append(project)
            except:
                print('Invalid filename')
        elif choice == 's':
            try:
                out_filename = input('Filename: ')
                with open(f'prac_07/{out_filename}', 'w') as out_file:
                    pass
            except:
                print('Invalid filename')
        elif choice == 'd':
            try:
                for project in projects:
                    print(project)
            except:
                print('No projects found')
        choice = get_choice()


def get_choice():
    choice = input(MENU).lower()
    while choice not in ['l', 's', 'd', 'f', 'a', 'u', 'q']:
        print('Invalid choice')
        choice = input(MENU).lower()
    return choice

main()