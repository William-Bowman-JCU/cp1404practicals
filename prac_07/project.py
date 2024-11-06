class Project:
    def __init__(self, name, starting_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.starting_date = starting_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage
    
    def __repr__(self):
        return f'{self.name:20}, {self.starting_date}, {self.priority}, ${self.cost_estimate:<10,}, {self.completion_percentage:6.2f}%'
    
    def __lt__(self, other):
        return self.priority < other.priority