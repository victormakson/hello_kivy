from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class minhaapp(App):
    def build(self):

        return AsyncImage(source='https://i.pinimg.com/736x/7e/c9/a0/7ec9a017ced03f6831c6151fda463ac2.jpg')
    

if __name__ == "__main__":
    minhaapp().run()