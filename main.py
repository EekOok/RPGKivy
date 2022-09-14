
import menu_widget
import mapisateur


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.config import Config


# ---------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU_NUIT = (5, 5, 30)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 216, 0)
ORANGE = (255, 106, 0)

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', '1')

# fix the height of the window
Config.set('graphics', 'height', '600')
Config.set('graphics', 'width', '640')


class MainFenetre(Widget):
    def __init__(self):
        super().__init__()
        self.size = (640, 600)
        self.next_screen = 'None'
        self.menu = menu_widget.MenuStart()
        self.add_widget(self.menu)

    def check_screen(self, dt):
        if dt > 10:
            print('laaaaag')

        if self.next_screen == 'menu':
            for child in self.children:
                self.remove_widget(child)
            self.menu = menu_widget.MenuStart()
            self.add_widget(self.menu)
            self.next_screen = 'None'

        elif self.next_screen == 'crea1':
            for child in self.children:
                self.remove_widget(child)
            self.menu = menu_widget.Creaperso('comicsans ms')
            self.add_widget(self.menu)
            self.next_screen = 'None'

        elif self.next_screen == 'map':
            for child in self.children:
                self.remove_widget(child)
            map = mapisateur.Map(size=(25*32, 25*32))
            self.add_widget(map)
            self.next_screen = 'None'



# lancement du widget principal et de l'update du sequenceur
class TestApp(App):
    def build(self):
        print('Build')

        test = MainFenetre()
        Clock.schedule_interval(test.check_screen, 1.0 / 60.0)
        return test


if __name__ == '__main__':
    TestApp().run()
