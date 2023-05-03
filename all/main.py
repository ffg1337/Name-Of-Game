import kivy
kivy.require('1.9.0')

from kivy.app import App

# To change the kivy default settings
# we use this module config
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False

'''Needed classes'''

from scene_builder import Scene_builder
from all.resolution import Resolution

class TitleApp(App):
    def build(self):
        self.icon = '../img/icon.png'
        TitleApp.title ="Name Of the Game"
        return Scene_builder().scene_loader()

if __name__ == '__main__':
    Resolution().check()
    TitleApp().run()


