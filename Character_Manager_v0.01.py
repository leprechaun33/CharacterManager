import colorama
from colorama import Fore, Back, Style
import sys
import os
import sqlite3
import pathlib


class Menus():
    titleStr = "Character Manager v0.01"
    colorama.init()
    mainMenuList = []
    charMenuList = []
    spellMenuList = []
    itemMenuList = []

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        Menus.ClearScreen()
        while True:
            try:
                print(Fore.GREEN + self.titleStr)
                print(f"Main Menu{Style.RESET_ALL}")
                print("Character Menu: 0")
                print("Spell Menu: 1")
                print("Item Menu: 2")
                print("Exit: 3")
                mainMenuInput = int(input("Selection: "))
            except ValueError:
                Menus.BadChoice()
            else:
                if 0 <= mainMenuInput <= len(self.mainMenuList):
                    self.mainMenuList[mainMenuInput](self)
                else:
                    Menus.BadChoice()

    def BadChoice():
        Menus.ClearScreen()
        print(f"\n{Back.RED}{Fore.BLACK}That is not an option!\
              {Style.RESET_ALL}\n")

    def FillerText():
        Menus.ClearScreen()
        print("More to come\n")

    def SubMenu(self, subMenuList, subMenuTitle):
        Menus.ClearScreen()
        while True:
            try:
                print(Fore.GREEN + self.titleStr)
                print(subMenuTitle + Style.RESET_ALL)
                x = 0
                for i in subMenuList:
                    indexStr = str(x)
                    try:
                        nameStr = str(subMenuList[x].__name__)
                        nameStr2 = nameStr.replace("_", " ")
                        print(nameStr2 + ": " + indexStr)
                        x += 1
                    except AttributeError:
                        print(subMenuList[x] + ": " + indexStr)
                        subMenuInput = int(input("Selection: "))
                        x += 1
            except ValueError:
                Menus.BadChoice()
            else:
                if 0 <= subMenuInput <= len(subMenuList):
                    if isinstance(subMenuList[subMenuInput], str):
                        Menus.ClearScreen()
                        break
                    else:
                        subMenuList[subMenuInput](self)
                else:
                    Menus.BadChoice()

    def ClearScreen():
        if os.name == 'nt':
            os.system('cls')
        else:
            print("\033c", end="")

    def CharacterMenu(self):
        Menus.SubMenu(self, self.charMenuList, "Character Menu")

    def SpellMenu(self):
        Menus.SubMenu(self, self.spellMenuList, "Spell Menu")

    def ItemMenu(self):
        Menus.FillerText()

    def ExitProgram(self):
        colorama.deinit()
        DBManager.dbCon.close()
        sys.exit()

    def View_Character(self):
        Menus.FillerText()

    def New_Spell(self):
        Menus.FillerText()

    def View_Spell_List(self):
        Menus.FillerText()

    def Edit_Spell(self):
        Menus.FillerText()

    def Delete_Spell(self):
        Menus.FillerText()

    mainMenuList.append(CharacterMenu)
    mainMenuList.append(SpellMenu)
    mainMenuList.append(ItemMenu)
    mainMenuList.append(ExitProgram)

    charMenuList.append(View_Character)
    charMenuList.append("Main Menu")

    spellMenuList.append(View_Spell_List)
    spellMenuList.append(New_Spell)
    spellMenuList.append(Edit_Spell)
    spellMenuList.append(Delete_Spell)
    spellMenuList.append("Main Menu")


class DBManager():
    dbFile = str(pathlib.Path(__file__).parent) + "data.sqlite"
    dbCon = sqlite3.connect(dbFile)
    dbCur = dbCon.cursor()

    def DBNewSpell(self):



if __name__ == '__main__':
    program = Menus()
