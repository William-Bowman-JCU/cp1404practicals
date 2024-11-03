class ProgrammingLanguage:
    def __init__(self, name='', typing='', reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return True if self.typing == 'Dynamic' else False