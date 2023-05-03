from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from game_screens import*
from save import SaveLoad

class Scene_builder():
    global Scene,list_screens

    def scene_loader(self,**kwargs):
        '''Main Screens'''''''''''''''''''''''''''''''''
        Builder.load_file('../styles/mainwidow.kv')
        Builder.load_file('../styles/newgame.kv')
        Builder.load_file('../styles/aboutgame.kv')
        ''''''''''''''''''''''''''''''''''''''''''''''''

        '''Game Screens'''''''''''''''''''''''''''''''''
        Builder.load_file('../styles/gamestyle.kv')
        ''''''''''''''''''''''''''''''''''''''''''''''''


        Scene = ScreenManager()
        Scene.add_widget(MenuScreen(name='menu'))

        Scene.add_widget(AboutGameScreen(name='AboutGameScreen'))
        Scene.add_widget(TypeScreen(name='TypeScreen'))

        list_screens = []
        list_screens.extend([ScreenOfNewGame0,ScreenOfNewGame1, ScreenOfNewGame2,
                       ScreenOfNewGame3, ScreenOfNewGame4, ScreenOfNewGame5,
                       ScreenOfNewGame6, ScreenOfNewGame7, ScreenOfNewGame8,
                       ScreenOfNewGame9, ScreenOfNewGame10, ])

        for i in range(len(list_screens)):
            Scene.add_widget(list_screens[i](name='ScreenOfNewGame%d' % i))
        print(int(len(list_screens)))

        return Scene


