from kivy.properties import ObjectProperty

from random import randint

from all.game_screens import MenuScreen
from game_screens import *



class SecretClass(MenuScreen):
    secret_label = ObjectProperty(None)

    def secret_def(self,secret_label):
        RND_NUM = randint(0, 100)
        RND_NUM_CLR = randint(0, 255)
        SRT_TXT = open('../files/secret_text.txt', 'r', encoding='utf-8')
        SKP_TXT = open('../files/skip_text.txt', 'r', encoding='utf-8')

    # read
        for i in SRT_TXT and SKP_TXT:
            list_sct_txt = SRT_TXT.readlines()
            list_skp_txt = SKP_TXT.readlines()
    # vote fav
        if RND_NUM >= 90:
            secret_label.text = '?txt? ' + list_sct_txt[RND_NUM];
            secret_label.color = (RND_NUM_CLR,
                                  RND_NUM_CLR,
                                  RND_NUM_CLR, 1); SRT_TXT.close()
        else:
            secret_label.text = ' ' + list_skp_txt[RND_NUM];
            secret_label.color = (randint(0, 255),
                                  randint(0, 255),
                                  randint(0, 255), 0.5) ; SKP_TXT.close()
    def count(self,secret_label):
        global count
        if count >= 100:
            secret_label.text = ' Окей ты победил '
            print('www')
            count = 0
        else:
            count += 1
count = 0



