from kivy.app import App
from kivy.uix.textinput import TextInput

class minhaapp(App):
    def build(self):
        return TextInput(text='digite aqui')
    
if __name__ == "__main__":
    minhaapp().run()