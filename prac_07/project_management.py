from project import Project
from datetime import datetime
MENU = '\nMenu:\n(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit\n>> '

def main():
    choice = get_choice()
    while choice != 'q':
        if choice == 'l':
            projects = []
            # in_filename = input('Filename: ')
            in_filename = 'projects.txt'
            try:
                with open(f'prac_07/{in_filename}', 'r') as in_file:
                    in_file.readline()
                    for line in in_file:
                        data = line.strip().split('\t')
                        # Use datetime here
                        project = Project(data[0], data[1], int(data[2]), float(data[3]), float(data[4]))
                        projects.append(project)
                print(f'{in_filename} loaded successfully')
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
                incomplete_projects = sorted([project for project in projects if project.completion_percentage != 100])
                completed_projects = sorted([project for project in projects if project.completion_percentage == 100])
                print('Incomplete projects:')
                for project in incomplete_projects:
                    print(project)
                print('\nCompleted projects:')
                for project in completed_projects:
                    print(project)
            except:
                print('No projects found')
        elif choice == 'f':
            date = input('Date: ')
            date = datetime.strptime(date, '%d/%m/%Y')
            # Sort this by date instead of priority
            future_projects = sorted([project for project in projects if project.start_date > date])
            for project in future_projects:
                print(project)
        choice = get_choice()


def get_choice():
    choice = input(MENU).lower()
    while choice not in ['l', 's', 'd', 'f', 'a', 'u', 'q']:
        print('Invalid choice')
        choice = input(MENU).lower()
    return choice

main()
