import Tools

from kivy.uix.widget import Widget
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image as KvImage
from kivy.graphics import *

from PIL import Image as PilImage
from io import BytesIO


class Tile(KvImage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def extrudetile(ref, only_use):

    modifiedimg = PilImage.open(ref).convert('RGB')
    dico_xyref = {'0': (32, 5 * 32),
                  '1': (0,  5 * 32),
                  '2': (32, 4 * 32),
                  '3': (2 * 32, 4 * 32),
                  '4': (2 * 32, 5 * 32),

                  '10': (0, 0),
                  '11': (0, 32),
                  '12': (0, 2 * 32),
                  '13': (0, 3 * 32),

                  '14': (32, 0),
                  '15': (32, 32),
                  '16': (32, 2 * 32),
                  '17': (32, 3 * 32),

                  '19': (2 * 32, 32),
                  '20': (2 * 32, 2 * 32),
                  '21': (2 * 32, 3 * 32),
                  '22': (3 * 32, 0),

                  }
    dico_tile = {}

    for numtile in dico_xyref:
        if int(numtile) in only_use:
            xtile, ytile = dico_xyref[numtile]
            fragment = modifiedimg.crop((xtile, ytile, xtile + 32, ytile + 32))  # extraction d'une partie
            data = BytesIO()
            fragment.save(data, format='png')
            data.seek(0)
            im = CoreImage(BytesIO(data.read()), ext='png')
            dico_tile[numtile] = im.texture

    return dico_tile


class Map(Widget):
    def __init__(self, jsonlink='./map/map0.json', **kwargs):
        super().__init__(**kwargs)

        self.infomap = Tools.readthedict(jsonlink)
        self.source_tile = self.infomap["source_image"]
        self.map_image = self.infomap["map_image"]
        dico_only_use = {}
        for element in self.map_image:
            for element2 in self.map_image[element]:
                dico_only_use[element2] = True

        self.dico_tile = extrudetile(self.source_tile, dico_only_use)

        self.nbx, self.nby = self.infomap["dim"]
        self.tab_map = []

        for y in range(self.nby):
            ligne = []
            ytile = (self.nby-1-y) * 32
            ystr = str(y)

            for x in range(self.nbx):
                xtile = x * 32
                numref = self.map_image[ystr][x]
                atile = Tile(pos=(xtile, ytile), size=(32, 32), texture=self.dico_tile[str(numref)])
                self.add_widget(atile)
                ligne.append(atile)

            self.tab_map.append(ligne)

# -----------------------------------------------------


if __name__ == '__main__':

    from kivy.app import App

    # we use this module config
    from kivy.config import Config

    # 0 being off 1 being on as in true / false
    # you can use 0 or 1 && True or False
    Config.set('graphics', 'resizable', '1')

    # fix the height of the window
    Config.set('graphics', 'height', '600')
    Config.set('graphics', 'width', '640')


    class MainFenetre(Widget):
        def __init__(self):
            super().__init__()
            self.next_screen = 'None'
            self.amap = Map(size=(25*32, 25*32))
            self.add_widget(self.amap)


    # lancement du widget principal et de l'update du sequenceur
    class TestApp(App):
        def build(self):
            print('Build')

            test = MainFenetre()

            return test


    TestApp().run()
