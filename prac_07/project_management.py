from project import Project
from datetime import datetime
from operator import attrgetter

MENU = '\nMenu:\n(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit\n>> '
INITIAL_FILENAME = 'projects.txt'

def main():
    """Load user defined projects & execute functions to modify them"""
    print('Welcome to the Pythonic Project Management')
    projects, header = load_projects(INITIAL_FILENAME)
    choice = get_choice()
    while choice != 'q':
        if choice == 'l':
            in_filename = get_valid_string('Filename: ')
            projects, header = load_projects(in_filename)
        elif choice == 's':
            save_projects(projects, header)
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
            date = get_valid_date('Show projects that start after date (dd/mm/yyyy): ')
            future_projects = sorted([project for project in projects if project.start_date >= date], key=attrgetter('start_date'))
            for project in future_projects:
                print(project)
        elif choice == 'a':
            print('Enter project details:')
            name = get_valid_string('Name: ')
            start_date = get_valid_date('Start date (dd/mm/yyyy): ')
            priority = get_valid_number('Priority: ')
            cost_estimate = float(get_valid_number('Cost estimate: $'))
            completion_percentage = get_valid_number('Percent complete: ')
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
            print(f'{name} has been added')
        elif choice == 'u':
            for i, project in enumerate(projects):
                print(f'{i} {project}')
            project_index = get_valid_number('Project choice: ')
            while project_index > len(projects) - 1:
                print('Invalid index')
                project_index = get_valid_number('Project choice: ')
            project_choice = projects[project_index]
            print(project_choice)
            new_percentage = get_valid_number('New Percentage: ', blank=True)
            new_priority = get_valid_number('New Priority: ', blank=True)
            if new_percentage != '':
                project_choice.completion_percentage = new_percentage
            if new_priority != '':
                project_choice.priority = new_priority
        choice = get_choice()
    is_final_save = get_valid_string('Would you like to save to projects.txt?\n>> ')
    if is_final_save == 'yes':
        save_projects(projects, header)
    print('Thank you for using custom-built project management software.')


def save_projects(projects, header):
    out_filename = get_valid_string('Filename: ')
    with open(f'prac_07/{out_filename}', 'w') as out_file:
        print(header, file=out_file)
        for project in projects:
            print(project.save_format(), file=out_file)

def get_valid_string(prompt):
    """Get a non-blank string"""
    value = input(prompt)
    while value == '':
        print('Invalid input')
        value = input(prompt)
    return value

def load_projects(in_filename):
    """Load all projects from the file with the given name"""
    projects = []
    try:
        with open(f'prac_07/{in_filename}', 'r') as in_file:
            header = in_file.readline().strip()
            for line in in_file:
                data = line.strip().split('\t')
                project = Project(data[0], datetime.strptime(data[1], '%d/%m/%Y'), data[2], data[3], data[4])
                projects.append(project)
        print(f'Loaded {len(projects)} projects from {in_filename}')
    except FileNotFoundError:
        print('Invalid filename')
    return (projects, header)

def get_choice():
    """Get a valid menu choice"""
    choice = input(MENU).lower()
    while choice not in ('l', 's', 'd', 'f', 'a', 'u', 'q'):
        print('Invalid choice')
        choice = input(MENU).lower()
    return choice

def get_valid_date(prompt):
    """Get a valid date string, in the dd/mm/yy or /yyyy format"""
    date = input(prompt)
    while not isinstance(date, datetime):
        try:
            date = datetime.strptime(date, '%d/%m/%Y')
        except:
            print('Invalid date')
            date = input(prompt)
    return date

def get_valid_number(prompt, blank=False):
    """Get a non negative number, and optionally a blank string"""
    value = input(prompt)
    while isinstance(value, str):
        try:
            if int(value) >= 0:
                return int(value)
            else:
                print('Invalid input; enter a valid number')
                value = input(prompt)
        except:
            if blank and value == '':
                return value
            print('Invalid input; enter a valid number')
            value = input(prompt)

main()
