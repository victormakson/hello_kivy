from kivy.app import App
from kivy.uix.video import Video

class minhaapp(App):
    def build(self):
        return Video(source='C:\Users\aluno.sesipaulista\Downloads\Oblongs.mp4')
    
if __name__ ==  "__main__":
    minhaapp().run()