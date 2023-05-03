from all.game_screens import MenuScreen

class ReaderS(MenuScreen):
    global text_for_scene
    global actual_text
    def check_scene(self,strin = ''):
        actual_text = False
        strin = strin[15:16]
        Num = int(strin)
        print(Num)
        #number_scene = int(SaveLoad().continue_game())        nu
        number_scene = Num
        text_for_scene = ''
        try:
            f = open("../files/skip_text.txt", mode='r', encoding='utf-8-sig')
            #todo make var of begin text and end text for this down
            for text in f.readlines():
                if text == "#" + str(number_scene) +"\n": #begin from #count
                    actual_text = True
                if text == "#" + str(number_scene) + " end" + "\n":  # end read
                    break
                if actual_text == True and text != "#" + str(number_scene) +"\n":
                    text_for_scene = text_for_scene + str(text)
            f.close()
        except IOError:
            print("No file saves or new game start")
        return  text_for_scene