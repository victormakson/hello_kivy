from kivy.app import App
from kivy.uix.image import Image

class minhaapp(App):
    def build(self):
        return Image(source='/Users/aluno.sesipaulista/Pictures/fodase.jpg')


if __name__ == "__main__":
    minhaapp().run()