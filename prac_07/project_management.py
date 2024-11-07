from project import Project
from datetime import datetime
from operator import attrgetter

MENU = '\nMenu:\n(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit\n>> '

def main():
    print('Welcome to the Pythonic Project Management')
    projects, header = load_projects()
    choice = get_choice()
    while choice != 'q':
        if choice == 'l':
            projects, header = load_projects()
        elif choice == 's':
            try:
                out_filename = input('Filename: ')
                with open(f'prac_07/{out_filename}', 'w') as out_file:
                    print(header, file=out_file)
                    for project in projects:
                        print(project.save_format(), file=out_file)
            except FileNotFoundError:
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
            date = convert_string_to_date(input('Show projects that start after date (dd/mm/yyyy): '))
            future_projects = sorted([project for project in projects if project.start_date >= date], key=attrgetter('start_date'))
            for project in future_projects:
                print(project)
        elif choice == 'a':
            print('Enter project details:')
            name = input('Name: ')
            start_date = convert_string_to_date(input('Start date (dd/mm/yyyy): '))
            priority = int(input('Priority: '))
            cost_estimate = float(input('Cost estimate: $'))
            completion_percentage = float(input('Percent complete: '))
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
            print(f'{name} has been added')
        elif choice == 'u':
            for i, project in enumerate(projects):
                print(f'{i} {project}')
            project_index = get_valid_number('Project choice: ')
            while project_index > len(projects):
                print('Invalid index')
                project_index = get_valid_number('Project choice: ')
            project_choice = projects[project_index]
            print(project_choice)
            new_percentage = get_updated_value('New Percentage: ')
            new_priority = get_updated_value('New Priority: ')
            if new_percentage != '':
                project_choice.completion_percentage = new_percentage
            if new_priority != '':
                project_choice.priority = new_priority
        choice = get_choice()
    print('Would you like to save to projects.txt? no, I think not.')
    print('Thank you for using custom-built project management software.')

def load_projects():
    projects = []
    # in_filename = input('Filename: ')
    in_filename = 'projects.txt'
    try:
        with open(f'prac_07/{in_filename}', 'r') as in_file:
            header = in_file.readline().strip()
            for line in in_file:
                data = line.strip().split('\t')
                project = Project(data[0], convert_string_to_date(data[1]), data[2], data[3], data[4])
                projects.append(project)
        print(f'Loaded {len(projects)} projects from {in_filename}')
    except FileNotFoundError:
        print('Invalid filename')
    return (projects, header)

def get_choice():
    choice = input(MENU).lower()
    while choice not in ['l', 's', 'd', 'f', 'a', 'u', 'q']:
        print('Invalid choice')
        choice = input(MENU).lower()
    return choice

def convert_string_to_date(date):
    return datetime.strptime(date, '%d/%m/%Y')

def get_valid_number(prompt):
    """Get a number"""
    value = input(prompt)
    while isinstance(value, str):
        try:
            value = int(value)
        except ValueError:
            print('Invalid input; enter a valid number')
            value = input(prompt)
    return value

def get_updated_value(prompt):
    """"""
    value = input(prompt)
    while isinstance(value, str):
        try:
            value = int(value)
        except ValueError:
            if value == '':
                return value
            print('Invalid input; enter a valid number')
            value = input(prompt)
    return value
main()
