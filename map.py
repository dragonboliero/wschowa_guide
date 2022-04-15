from kivymd.app import MDApp
from kivy_garden.mapview import MapView
from kivymd.uix.label import MDLabel
from kivy.lang.builder import Builder   
from kivy.core.window import Window

from pygame import mixer

descs = {'ratusz':{'img1':'Widok na ratusz od strony plantów',
'img2':'Widok z lewej storny',
'img3':'Widok od strony parku',
'desc':'Ratusz we Wschowie – najstarsza częścią ratusza jest monumentalna wieża pochodząca z XVI wieku. W latach 1860 budowli nadano obecny charakter neoromański. Jest to budynek murowany, trójkondygnacyjny, założony na rzucie prostokąta. W narożniku północno-zachodnim znajduje się wieża. Zachowała się na parterze w części północno-wschodniej sala nakryta późnogotyckim sklepieniem sieciowym (I połowa XV wieku).'},
'fara':{'img1':'Pierwsze zdjecie',
'img2':'Drugie zdjecie',
'img3':'Trzecie zdjecie',
'desc':'Pierwsza wzmianka o istnieniu parafii we Wschowie pochodzi z dokumentu z 1326 roku, w którym miejscowy proboszcz Jordan pełnił rolę świadka. Sama parafia i kościół zapewne istniały już wcześniej. Budowla wielokrotnie została zniszczona podczas licznych pożarów Wschowy, między innymi w latach 1435 i 1529. Po drugim pożarze kościół został odbudowany, dzięki szczodrości i działaniom kanonika wrocławskiego Mateusza Lamprechta, urodzonego we Wschowie. Podczas reformacji, przez kilka lat, świątynia była używana przez protestantów. Zwrócili ją gminie katolickiej w 1604 roku. Po raz kolejny kościół obrócił się w zgliszcza w 1685 roku, a mała parafia katolicka nie mogła sobie poradzić z jego odbudowaniem. Ostatecznie, świątynia została odbudowana w latach 1720-1726 według projektu słynnego włoskiego architekta Pompeo Ferrariego. W takim stanie kościół zachował się do dnia dzisiejszego. Jest to kościół bazylikowy o trzech nawach, reprezentujący styl barokowy, z elementami architektury gotyckiej. Wyposażenie wnętrza jest utrzymane w stylu barokowym i pochodzi z XVIII stulecia. '}}


class MapViewApp(MDApp):
    def build(self):
        self.audiofile = ''
        app_uix = Builder.load_file('map.kv')
        Window.size = (360,800)
        return app_uix

    def change_user_pos(self):
        print(str(self.root.ids.user.lat))
        print(str(self.root.ids.user.lon))
        self.root.ids.user.lat = float(self.root.ids.lat.text)
        self.root.ids.user.lon = float(self.root.ids.lon.text)
        self.root.ids.mapa.center_on(float(self.root.ids.lat.text),float(self.root.ids.lon.text))
        lat_diff = abs(self.root.ids.user.lat - self.root.ids.ratusz.lat)
        lon_diff = abs(self.root.ids.user.lon - self.root.ids.ratusz.lon)
        if lat_diff < 0.0003:
            if lon_diff < 0.0006:
                self.root.ids.user.source = "data/img/user_ok.png"
            else:
                self.root.ids.user.source = "data/img/user.png"
        else:
                self.root.ids.user.source = "data/img/user.png"
        print(lon_diff) 
        print('after')
    
    #def display_bigger_photo(self,name):


    def audiofile_setup(self,name):
        self.audiofile = name
        self.root.ids.play_sound.disabled = False
        self.root.ids.pause_sound.disabled = False
        self.root.ids.unpause_sound.disabled = False
    
    def play_sound(self):
        mixer.init()
        mixer.music.load(f"data/audio/{self.audiofile}.mp3")
        mixer.music.play()
    
    def stop_sound(self):
        try:
            mixer.music.pause()
        except:
            pass
    def unpause_sound(self):
        try:
            mixer.music.unpause()
        except:
            pass

    def disable_sound(self):
        self.root.ids.play_sound.disabled = True
        self.root.ids.pause_sound.disabled = True
        self.root.ids.unpause_sound.disabled = True

    def enable_content(self,name):
        #Setup images
        self.root.ids.img1.background_normal = f"data/img/{name}_1.jpg"
        self.root.ids.img1.background_down = f"data/img/{name}_1.jpg"
        #Change later to jpg
        self.root.ids.img2.source = f"data/img/{name}_2.jpg"
        self.root.ids.img3.source = f"data/img/{name}_3.jpg"
        #Setup img captions
        self.root.ids.img1_caption.text = descs[name]['img1']
        self.root.ids.img2_caption.text = descs[name]['img2']
        self.root.ids.img3_caption.text = descs[name]['img3']
        self.root.ids.item_desc.text = descs[name]['desc']
        


MapViewApp().run()

