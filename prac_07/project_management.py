from project import Project
from datetime import datetime
from operator import attrgetter

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
                        project = Project(data[0], convert_string_to_date(data[1]), data[2], data[3], data[4])
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
                incomplete_projects = sorted([project for project in projects if project.completion_percentage != 100], key=attrgetter('priority'))
                completed_projects = sorted([project for project in projects if project.completion_percentage == 100], key=attrgetter('priority'))
                print('Incomplete projects:')
                for project in incomplete_projects:
                    print(project)
                print('\nCompleted projects:')
                for project in completed_projects:
                    print(project)
            except:
                print('No projects found')
        elif choice == 'f':
            date = convert_string_to_date(input('Date: '))
            future_projects = sorted([project for project in projects if project.start_date > date], key=attrgetter('start_date'))
            for project in future_projects:
                print(project)
        elif choice == 'a':
            print('Enter project details:')
            name = input('Name: ')
            start_date = convert_string_to_date(input('Start date: '))
            priority = int(input('Priority: '))
            cost_estimate = float(input('Cost estimate: $'))
            completion_percentage = float(input('Completetion percentage: '))
            print(f'{name} has been added')
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        choice = get_choice()


def get_choice():
    choice = input(MENU).lower()
    while choice not in ['l', 's', 'd', 'f', 'a', 'u', 'q']:
        print('Invalid choice')
        choice = input(MENU).lower()
    return choice

def convert_string_to_date(date):
    return datetime.strptime(date, '%d/%m/%Y')

main()
