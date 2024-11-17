from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

KM_CONVERSION_VALUE = 1.60934

class ConvertMilesKm(App):
    result = StringProperty()
    
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, number):
        miles = self.root.ids.miles_input.text
        try:
            self.root.ids.miles_input.text = str(int(miles) + number)
        except:
            self.root.ids.miles_input.text = str(0 + number)
    
    def convert_miles_km(self):
        miles = self.root.ids.miles_input.text
        try:
            km = float(miles) * KM_CONVERSION_VALUE
            if km < 0:
                km = 0.0
        except:
            km = 0.0
        self.result = str(km)



ConvertMilesKm().run()