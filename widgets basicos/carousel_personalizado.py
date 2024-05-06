from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage

class Carouselapp(App):
    def build(self):
        carousel = Carousel(direction='right', loop=True)
        imagens = ["fodase1.jpg", "fodase2.jpg", "fodase3.jpg", "fodase4.jpg", "fodase5.jpg", "fodase6.jpg"]

        for imagem in imagens:
            imagem_widget = AsyncImage(source=imagem)
            carousel.add_widget(imagem_widget)

            return carousel
        
if __name__ == "__main__":
    Carouselapp().run()