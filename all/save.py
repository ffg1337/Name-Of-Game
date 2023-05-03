from kivy.uix.screenmanager import ScreenManager

from scene_builder import *
global num_save

class SaveLoad(ScreenManager):
    def save(self,save_act,save_number,save_event,save_mark):
        try:
            saves = open("../files/saves.txt", "a", encoding='utf-8')
            saves.writelines(save_act+save_number+save_event+save_mark+"\n")
            saves = open("../files/saves.txt", "r")
            print(saves.read())
            saves.close()

        except IOError:
            print("No file saves or new game start !")
        return

    def reset_save(self):
        try:
            saves = open("../files/saves.txt", "w")
            saves.close()
        except IOError :
             print("No file saves !")

    def continue_game (self):
        try:
            saves = open("../files/saves.txt", "r", encoding='utf-8')
            for saveline in saves :
                open("../files/saves.txt", "r")
                list_save = saveline.split()
                for num_save in list_save:
                    num_save = list_save[1]
            saves.close()

        except IOError : print("No file saves or new game start !")

        return "ScreenOfNewGame"+str(num_save)

    def check(self):
        try:
            saves = open("../files/saves.txt", "r", encoding='utf-8')
            for saveline in saves :
                open("../files/saves.txt", "r")
                wsaves = saveline.split()
                for s in wsaves:
                    if s == 'End_Games':
                        print(s + " huy rckf")
            saves.close()

        except IOError : print("No file saves or new game start !")
        return  wsaves[1]

    def readers(self,text_doc):
        ss = "../files/texts_for_scenes/"+str(self.continue_game())+".txt"
        return text_doc.text(ss)

    def no_reader(self):

        print(self.check())
        a = ''
        ss1 = "../files/texts_for_scenes/"+str(self.check())+".txt"
        TEXT_FROM_FILE1 = open(ss1, "r", encoding='utf-8')

        for TEXT1 in TEXT_FROM_FILE1:
            a += TEXT1 + '\n'
            print(a)
        return a + 'huy'
