class Project:
    def __init__(self, name, starting_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.starting_date = starting_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage
    
    def __repr__(self):
        return f'{self.name}, {self.starting_date}, {self.priority}, {self.cost_estimate}, {self.completion_percentage}'