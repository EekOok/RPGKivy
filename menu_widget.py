

from PIL import Image as PilImage
from io import BytesIO

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image as KvImage


BLANC = [1, 1, 1, 1]
NOIR = [0, 0, 0, 1]
BLEU_NUIT = (5, 5, 30)
ROUGE = [1, 0, 0, 1]
VERT = [0, 1, 0, 1]
BLEU = [0, 0, 1, 1]
JAUNE = [1.0, 216.0/255.0, 0, 1]
ORANGE = [255, 106, 0, 1]


class Menu(Widget):
    """ Class de base qui dessine le cadre des menus"""
    def __init__(self, nom, dimension, **kwargs):
        super().__init__(**kwargs)
        self.nom = nom
        self.color_fond = (30, 5, 5)

        self.dimension = dimension
        self.refx = self.dimension[0]
        self.refy = self.dimension[1]
        self.width = self.dimension[2]
        self.height = self.dimension[3]

        self.image_fond = KvImage(source="images/menu/fond.png", allow_stretch=True, keep_ratio=False,
                                  size=(self.width, self.height), pos=(self.refx, self.refy))
        self.add_widget(self.image_fond)

        self.image_bar_b = KvImage(source="images/menu/bar_b.png", allow_stretch=True, keep_ratio=False,
                                   size=(self.width, 16), pos=(self.refx, self.refy))
        self.add_widget(self.image_bar_b)

        self.image_bar_h = KvImage(source="images/menu/bar_h.png", allow_stretch=True, keep_ratio=False,
                                   size=(self.width, 16), pos=(self.refx, self.refy+self.height-16))
        self.add_widget(self.image_bar_h)

        self.image_bar_g = KvImage(source="images/menu/bar_g.png", allow_stretch=True, keep_ratio=False,
                                   size=(16, self.height), pos=(self.refx, self.refy))
        self.add_widget(self.image_bar_g)

        self.image_bar_d = KvImage(source="images/menu/bar_d.png", size=(16, self.height),
                                   pos=(self.refx+self.width-16, self.refy),
                                   allow_stretch=True, keep_ratio=False)
        self.add_widget(self.image_bar_d)

        self.image_coin_bas_droit = KvImage(source="images/menu/coin_bas_droit.png", size=(16, 16),
                                            pos=(self.refx+self.width-16, self.refy+0),
                                            allow_stretch=True, keep_ratio=False)
        self.add_widget(self.image_coin_bas_droit)

        self.image_coin_bas_gauche = KvImage(source="images/menu/coin_bas_gauche.png", size=(16, 16),
                                             pos=(self.refx, self.refy+0), allow_stretch=True, keep_ratio=False)
        self.add_widget(self.image_coin_bas_gauche)

        self.image_coin_haut_droit = KvImage(source="images/menu/coin_haut_droit.png", size=(16, 16),
                                             pos=(self.refx+self.width - 16, self.refy+self.height-16),
                                             allow_stretch=True, keep_ratio=False)
        self.add_widget(self.image_coin_haut_droit)

        self.image_coin_haut_gauche = KvImage(source="images/menu/coin_haut_gauche.png", size=(16, 16),
                                              pos=(self.refx+0, self.refy+self.height-16),
                                              allow_stretch=True, keep_ratio=False)

        self.add_widget(self.image_coin_haut_gauche)


class LabButton(Widget):
    def __init__(self, font, text, pos, action=None, **kwargs):
        super().__init__(**kwargs)
        self.font = font
        self.lbl = Label(text=text, color=JAUNE, size=(100, 20), pos=pos)
        self.add_widget(self.lbl)
        self.action = action

    def on_touch_move(self, touch):
        if self.lbl.collide_point(*touch.pos):
            self.lbl.color = ROUGE
        else:
            self.lbl.color = JAUNE

    def on_touch_down(self, touch):
        if self.lbl.collide_point(*touch.pos):
            self.lbl.color = JAUNE
            if self.action is not None:
                self.action()


class MenuStart(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cadre = Menu('debut', (0, 0, 640, 600))
        self.add_widget(self.cadre)

        self.btnnouveau = LabButton(font='arial', text='Nouvelle partie', size=(100, 20), pos=(270, 300),
                                    action=self.action1)
        self.add_widget(self.btnnouveau)

        self.btncharger = LabButton(font='arial', text='Charger', size=(100, 20), pos=(270, 280), action=None)
        self.add_widget(self.btncharger)

        self.btnoption = LabButton(font='arial', text='Option', size=(100, 20), pos=(270, 260), action=None)
        self.add_widget(self.btnoption)

        self.btncredit = LabButton(font='arial', text='Crédit', size=(100, 20), pos=(270, 240), action=None)
        self.add_widget(self.btncredit)

    def action1(self):
        self.parent.next_screen = 'crea1'

    def action2(self):
        pass


class Creaperso(Widget):
    def __init__(self, font, **kwargs):
        super().__init__(**kwargs)
        self.font = font
        self.hauteur_premier_rang = 250
        # cardre haut
        if True:
            self.cadre_haut = Menu('Haut', (0, 550, 640, 50))
            self.add_widget(self.cadre_haut)

            self.labhaut = Label(text='Apparence', color=JAUNE, pos=(270, 525))
            self.add_widget(self.labhaut)

        self.liste_coul = ["rouge", "rouge sombre", "bleu", "bleu sombre", "vert", "vert sombre", "black", "rose"]

        # cadre Choix couleur
        if True:
            self.cadre_couleur = Menu('couleur', (0, 300, 320, 250))
            self.add_widget(self.cadre_couleur)

            # self.label_couleur = Label(text='Couleur', color=JAUNE, pos=(110, 475))
            self.label_couleur = Label(text='Couleur', color=JAUNE, size=(110, 20), pos=(110, 515))
            self.add_widget(self.label_couleur)

            self.label_chev = SelectorCouleur(text='Cheveux', valueinit=6, pos=(40, 475))
            self.add_widget(self.label_chev)

            self.label_yeux = SelectorCouleur(text='Yeux', valueinit=2, pos=(40, 435))
            self.add_widget(self.label_yeux)

            self.label_peau = SelectorCouleur(text='Peau', valueinit=7, pos=(40, 395))
            self.add_widget(self.label_peau)

            self.label_chemise = SelectorCouleur(text='Chemise', valueinit=3, pos=(40, 355))
            self.add_widget(self.label_chemise)

            self.label_pantalon = SelectorCouleur(text='Pantalon', valueinit=1, pos=(40, 315))
            self.add_widget(self.label_pantalon)

            self.imagepj = KvImage(pos=(180, 380), size=(128, 128), allow_stretch=True)
            self.add_widget(self.imagepj)

        # cadre Race
        if True:
            self.cadre_race = Menu('Race', (320, 550-self.hauteur_premier_rang, 320, self.hauteur_premier_rang))
            self.add_widget(self.cadre_race)

            self.label_race = Label(text='Race', color=JAUNE, pos=(430, 480))
            self.add_widget(self.label_race)

            self.race_selector = SelectorRace(nom='Race', spefont=self.font, pos=(380, 450))
            self.add_widget(self.race_selector)

            self.label_atout_race = Label(text="""Atout: 
                                                \n - +1 points de compétence/atout 
                                                \n - 2 compétences à +4
                                                \n - +1 Atout libre , +2 dK""",
                                          color=JAUNE, pos=(400, 330))
            self.add_widget(self.label_atout_race)

        # Cadre stat
        if True:
            # Colonne 1
            self.cadre_stat = Menu(nom="stat", dimension=(0, 50, 640, 250))
            self.add_widget(self.cadre_stat)

            self.label_Fo = AfficheurCarac(nom='Force', pos=(50, 210))
            self.add_widget(self.label_Fo)

            self.label_Dx = AfficheurCarac(nom='Dextérité', pos=(50, 180))
            self.add_widget(self.label_Dx)

            self.label_Co = AfficheurCarac(nom='Constitution', pos=(50, 150))
            self.add_widget(self.label_Co)

            self.label_It = AfficheurCarac(nom='Intelligence', pos=(50, 120))
            self.add_widget(self.label_It)

            self.label_Sg = AfficheurCarac(nom='Sagesse', pos=(50, 90))
            self.add_widget(self.label_Sg)

            self.label_Ch = AfficheurCarac(nom='Charisme', pos=(50, 60))
            self.add_widget(self.label_Ch)

            # Colonne 2
            self.label_pdv = AfficheurCompteur(nom='P.Vie', list_carac=[self.label_Co], pos=(185, 210))
            self.add_widget(self.label_pdv)

            self.label_ene = AfficheurCompteur(nom='P.Energie', list_carac=[self.label_Sg], pos=(185, 180))
            self.add_widget(self.label_ene)

            self.label_dk = AfficheurCompteur(nom='dK', list_carac=[self.label_Ch], type='dK', pos=(185, 150))
            self.add_widget(self.label_dk)

            self.label_port = AfficheurCompteur(nom='Portage', list_carac=[self.label_Fo,self.label_Co], type='portage',
                                              pos=(175, 120))
            self.add_widget(self.label_port)

            self.label_pc = AfficheurCompteur(nom='P.Compétences', list_carac=[self.label_It], type='comp',
                                                pos=(175, 90))
            self.add_widget(self.label_pc)
        self.drawme()

        # Cadre Pied
        if True:
            self.cadre_pied = Menu('pied', (0, 0, 640, 50))
            self.add_widget(self.cadre_pied)

            self.btn_retour = LabButton(text='Retour', action=self.back_click, font='arial', size=(32, 32),
                                        pos=(8, 16))
            self.btn_retour.bind(on_press=self.next_click)
            self.add_widget(self.btn_retour)

            self.btn_suivant = LabButton(text='Suivant', action=self.next_click, font='arial', size=(32, 32),
                                         pos=(640-100, 16))
            self.btn_suivant.bind(on_press=self.next_click)
            self.add_widget(self.btn_suivant)

    def back_click(self):
        self.parent.next_screen = 'menu'

    def next_click(self):
        self.parent.next_screen = 'map'

    def update_image(self, img2modify):
        color_cheveux = self.liste_coul[int(self.label_chev.slide.value)]
        color_oeuil = self.liste_coul[int(self.label_yeux.slide.value)]
        color_peau = self.liste_coul[int(self.label_peau.slide.value)]
        color_chemise = self.liste_coul[int(self.label_chemise.slide.value)]
        color_pantalon = self.liste_coul[int(self.label_pantalon.slide.value)]

        (largeur, hauteur) = img2modify.size

        px = img2modify.load()
        for x in range(largeur):
            for y in range(hauteur):
                coul = px[x, y]
                # Chemise ------------------------------
                if coul == (54, 56, 74):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_chemise, 'sombre'))
                elif coul == (26, 36, 43):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_chemise, 'tres sombre'))
                elif coul == (41, 48, 59):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_chemise, 'clair'))
                elif coul == (79, 82, 107):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_chemise, 'tres clair'))
                # Oeuil
                elif coul == (107, 23, 23):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_oeuil, 'clair'))
                elif coul == (163, 51, 51):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_oeuil, 'tres clair'))
                # Cheveux
                elif coul == (38, 41, 38):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_cheveux, 'tres sombre'))
                elif coul == (59, 56, 56):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_cheveux, 'sombre'))
                elif coul == (84, 89, 89):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_cheveux, 'medium'))
                elif coul == (133, 138, 140):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_cheveux, 'clair'))
                elif coul == (176, 184, 186):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_cheveux, 'tres clair'))
                # pantalon
                elif coul == (31, 48, 105):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_pantalon, 'tres sombre'))
                elif coul == (71, 102, 143):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_pantalon, 'sombre'))
                elif coul == (130, 173, 212):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_pantalon, 'clair'))
                # peau
                elif coul == (135, 88, 68):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_peau, 'tres sombre'))
                elif coul == (196, 159, 165):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_peau, 'sombre'))
                elif coul == (212, 153, 122):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_peau, 'medium'))
                elif coul == (255, 207, 176):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_peau, 'clair'))
                elif coul == (255, 232, 204):
                    img2modify.putpixel((x, y), self.retournecouleurset(color_peau, 'tres clair'))

        img2modify.save('./current/pj_type.png')

    def retournecouleurset(self, selection, teinte):
        print(self)
        colorset = {
            "rouge": {
                "tres clair": (255, 0, 0),
                "clair": (202, 0, 0),
                "medium": (121, 0, 0),
                "sombre": (160, 0, 0),
                "tres sombre": (128, 0, 0)},
            "rouge sombre": {
                "tres clair": (191, 0, 0),
                "clair": (138, 0, 0),
                "medium": (117, 0, 0),
                "sombre": (96, 0, 0),
                "tres sombre": (64, 0, 0)},
            "bleu": {
                "tres clair": (0, 0, 255),
                "clair": (0, 0, 202),
                "medium": (0, 0, 121),
                "sombre": (0, 0, 160),
                "tres sombre": (0, 0, 128)},
            "bleu sombre": {
                "tres clair": (0, 0, 191),
                "clair": (0, 0, 138),
                "medium": (0, 0, 117),
                "sombre": (0, 0, 96),
                "tres sombre": (0, 0, 64)},
            "vert": {
                "tres clair": (0, 255, 0),
                "clair": (0, 202, 0),
                "medium": (0, 121, 0),
                "sombre": (0, 160, 0),
                "tres sombre": (0, 128, 0)},
            "vert sombre": {
                "tres clair": (0, 191, 0),
                "clair": (0, 138, 0),
                "medium": (0, 117, 0),
                "sombre": (0, 96, 0),
                "tres sombre": (0, 64, 0)},
            "black": {
                "tres clair": (96, 96, 96),
                "clair": (64, 64, 64),
                "medium": (48, 48, 48),
                "sombre": (32, 32, 32),
                "tres sombre": (1, 1, 1)},

            "rose": {
                "tres clair": (255, 232, 204),
                "clair": (255, 207, 176),
                "medium": (212, 153, 122),
                "sombre": (196, 159, 165),
                "tres sombre": (135, 88, 68)},
        }
        return colorset[selection][teinte]

    def drawme(self):
        imgsource = './images/pj/pj_type.png'
        img2modify = PilImage.open(imgsource).convert('RGB')

        if self.race_selector.slide.value == 0:
            self.label_Co.base = 0
            self.label_Dx.base = 0
            self.label_Sg.base = 0
            self.label_pdv.update_value()
            self.label_ene.update_value()
            self.label_pc.update_value(base=1)
            self.label_dk.update_value(base=2)
            self.label_atout_race.text = """Atout: 
                                            \n - +1 points de compétence/atout
                                            \n - 2 compétences à +4
                                            \n - +1 Atout libre
                                            """
        else:
            if int(self.race_selector.slide.value) == 1:
                self.label_Co.base = 0
                self.label_Dx.base = 1
                self.label_Sg.base = 0
                self.label_pdv.update_value()
                self.label_ene.update_value()
                self.label_dk.update_value(base=0)
                self.label_pc.update_value(base=0)
                imgrace = './images/pj/oreille_elf.png'
                self.label_atout_race.text = """Atout: 
                                             \n - +1 Dextérité
                                             \n - Professionnel Armes Elfiques
                                             \n - +2dK gratuits en Observation"""
            else:  # nain
                self.label_Co.base = 1
                self.label_Dx.base = 0
                self.label_Sg.base = 0
                self.label_pdv.update_value()
                self.label_ene.update_value()
                self.label_dk.update_value(base=0)
                self.label_pc.update_value(base=0)
                self.label_atout_race.text = """Atout: 
                                              \n - +1 Constitution
                                              \n - Professionnel Armes Naines
                                              \n - +2dK en Artisanat"""
                imgrace = './images/pj/barbe_dwarf.png'

            img2add = PilImage.open(imgrace).convert('RGBA')
            img2modify.paste(img2add, mask=img2add)
            datas = img2modify.getdata()
            newdata = list()
            for item in datas:
                if item[0] == 0 and item[1] == 0 and item[2] == 0:
                    newdata.append((0, 0, 0, 0))
                else:
                    newdata.append(item)
            img2modify.putdata(newdata)

        self.update_image(img2modify)  # changement des couleurs
        modifiedimg = PilImage.open('./current/pj_type.png').convert('RGB')

        fragment = modifiedimg.crop((0, 0, 32, 32))  # extraction d'une partie

        data = BytesIO()
        fragment.save(data, format='png')
        data.seek(0)
        im = CoreImage(BytesIO(data.read()), ext='png')

        self.imagepj.texture = im.texture

    def recup_pj(self):
        print(self)
        return {'nom': 'Bob',
                'source_img': './current/pj_type.png',
                'caracs': [0, 0, 0, 0, 0, 0]}


class AfficheurCarac(Label):
    def __init__(self, nom='carac', spefont='arial', pos=(0, 0), pointinvestit=0, modificateur=0, base=0, **kwargs):
        super().__init__(**kwargs)
        self.nom = nom
        self.spefont = spefont
        self.color = JAUNE
        self.pos = pos

        self._pointinvestit = pointinvestit
        self._modificateur = modificateur
        self._base = base

        self._total = self._base + self._modificateur + self._pointinvestit

        self.text = self.nom + ' : ' + str(self._total)

    def update_value(self):
        self._total = int(self._base + self._modificateur + self._pointinvestit)
        self.text = self.nom + ' : ' + str(self._total)

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, newval):
        self._base = newval
        self.update_value()

    @property
    def modificateur(self):
        return self._modificateur

    @modificateur.setter
    def modificateur(self, newval):
        self._modificateur = newval
        self.update_value()

    @property
    def total(self):
        return self._total


class SelectorRace(Label):
    def __init__(self, nom='Race', spefont='arial', pos=(0, 0), valueinit=0, race='Humain', **kwargs):
        super().__init__(**kwargs)
        self.nom = nom
        self.spefont = spefont
        self.color = JAUNE
        self.pos = pos

        self._race = race

        self.text = self.nom + ' : ' + str(self._race)
        self.slide = Slider(min=0, max=2, step=1, value=valueinit, pos=(self.pos[0]+150, self.pos[1]+40),
                            cursor_size=(20, 20), value_track=True, value_track_color=[1, 0.5, 0, 1],
                            value_track_width=2, background_width=0, height=20,
                            cursor_image='images/menu/cursor.png')
        self.add_widget(self.slide)

    def on_touch_move(self, touch):
        self.update_value()

    def update_value(self):
        liste_race = ['Humain', 'Elfe', 'Nain']
        self._race = liste_race[int(self.slide.value)]
        self.text = self.nom + ' : ' + self._race
        self.parent.drawme()


class SelectorCouleur(Widget):
    def __init__(self, pos, text='Tête', valueinit=0, couleur='Rouge', **kwargs):
        super().__init__(size=(125, 40), pos=pos, **kwargs)
        self.pos = pos
        self.liste_coul = ["rouge", "rouge sombre", "bleu", "bleu sombre", "vert", "vert sombre", "black", "rose"]
        self.refx, self.refy = pos
        self.couleur = couleur

        self.lbl = Label(text=text, pos=(self.refx, self.refy+20), color=JAUNE, size=(125, 20), **kwargs)
        self.add_widget(self.lbl)

        self.max = len(self.liste_coul)-1
        self.slide = Slider(min=0, max=self.max, step=1, value=valueinit, size=(125, 20),
                            pos=(self.refx, self.refy),
                            cursor_size=(20, 20), value_track=True, value_track_color=[1, 0.5, 0, 1],
                            value_track_width=2, background_width=0, height=20,
                            cursor_image='images/menu/cursor.png')

        self.add_widget(self.slide)
        self.oldvalue = int(self.slide.value)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.update_value()

    def update_value(self):
        if self.oldvalue != int(self.slide.value):
            self.oldvalue = int(self.slide.value)
            self.couleur = self.liste_coul[int(self.slide.value)]
            self.parent.drawme()


class AfficheurCompteur(Label):
    def __init__(self, nom='cpt', list_carac=[0,], type='pv/ene', **kwargs):
        super().__init__(**kwargs)
        self.nom = nom
        self.list_carac = list_carac
        self.type = type
        self.update_value()

    def update_value(self, base=0):
        if self.type == 'dK':
            somme_carac = 0
            for carac in self.list_carac:
                somme_carac += carac.total

            self.valuemax = somme_carac+base
            self.text = self.nom + " : " + str(self.valuemax)

        elif self.type =='portage':
            somme_carac = 0
            for carac in self.list_carac:
                somme_carac += carac.total
            self.valuemax = somme_carac
            self.text = self.nom + " : " + str(self.valuemax)

        elif self.type == 'comp':
            somme_carac = 0
            for carac in self.list_carac:
                somme_carac += carac.total
            self.valuemax = somme_carac + 6 + base
            self.text = self.nom + " : " + str(self.valuemax)

        else:
            somme_carac = 0
            for carac in self.list_carac:
                somme_carac += carac.total
            self.valuemax = 10 + somme_carac
            self.recup = 1 + somme_carac
            self.text = self.nom + " : " + str(self.valuemax) + " / " + str(self.recup)