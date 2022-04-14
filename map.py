from kivymd.app import MDApp
from kivy_garden.mapview import MapView
from kivymd.uix.label import MDLabel
from kivy.lang.builder import Builder   
from kivy.core.window import Window

from playsound import playsound


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
                self.root.ids.user.source = "user_ok.png"
            else:
                self.root.ids.user.source = "user.png"
        else:
                self.root.ids.user.source = "user.png"
        print(lon_diff) 
        print('after')
    
    #def display_bigger_photo(self,name):


    def audiofile_setup(self,name):
        self.audiofile = name
        self.root.ids.play_sound.disabled = False
    
    def play_sound(self):
        playsound(f'{self.audiofile}.mp3')

    def disable_sound(self):
        self.root.ids.play_sound.disabled = True


MapViewApp().run()

