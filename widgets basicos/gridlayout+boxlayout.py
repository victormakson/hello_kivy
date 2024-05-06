from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class minhaapp(App):
    def build(self):
        layout_pricipal = GridLayout(cols=2)

        coluna_esquerda = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        menu_itens = ['Arquivo', 'Editar', 'Seleção', 'Ver', 'Acessar', 'Sair']
        Label1 = Label(text='Menu')
        coluna_esquerda.add_widget(Label1)
        for item in menu_itens:
            botao = Button(text=item)
            coluna_esquerda.add_widget(botao)

            coluna_direita = GridLayout(cols=1, rows=3)
            for i in range(3):
                botao = Button(text=f'botão {i+7}')
                coluna_direita.add_widget(botao)

                layout_pricipal.add_widget(coluna_esquerda)
                layout_pricipal.add_widget(coluna_direita)

                return layout_pricipal
            
if __name__ == "__main__":
    minhaapp().run()


