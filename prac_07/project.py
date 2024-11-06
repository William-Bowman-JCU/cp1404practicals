from datetime import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = float(completion_percentage)
    
    def __repr__(self):
        return f'{self.name:20}, {self.start_date.strftime('%d/%m/%Y')}, {self.priority}, ${self.cost_estimate:<12,.2f}, {self.completion_percentage:6.2f}%'
    
    # def __lt__(self, other):
    #     return self.priority < other.priority