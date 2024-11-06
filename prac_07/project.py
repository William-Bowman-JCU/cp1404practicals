from datetime import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)
    
    def __repr__(self):
        return f'{self.name:20}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:<12,.2f}, completion: {self.completion_percentage:6}%'
    
    def __lt__(self, other):
        return self.priority < other.priority