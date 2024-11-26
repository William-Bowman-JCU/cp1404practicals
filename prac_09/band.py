
class Band:
    def __init__(self, name):
        self.name = name
        self.members = []

    def __str__(self):
        """String representation of the band, showing members & their instruments"""
        return f'{self.name} ({', '.join([str(member) for member in self.members])})'

    def add(self, musician):
        """Add musicians to the band"""
        self.members.append(musician)

    def play(self):
        return '\n'.join([member.play() for member in self.members])
