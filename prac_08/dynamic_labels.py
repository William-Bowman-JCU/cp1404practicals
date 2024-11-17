from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class dynamic_labels(App):
    def on_start(self):
        self.names = ['John', 'Millie', 'Bobby', 'Douglas']
        for i, name in enumerate(self.names, 1):
            label = Label(text=f'Name {i}: {name}')
            self.root.ids.names_box.add_widget(label)
    
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root


dynamic_labels().run()