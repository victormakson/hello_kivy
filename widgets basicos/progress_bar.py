from kivy.app import App
from kivy.uix.progressbar import ProgressBar

class minhaapp(App):
    def build(self):
        return ProgressBar(value=50)
    
if __name__ == "__main__":
    minhaapp().run()