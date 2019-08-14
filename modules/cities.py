"""
----------------------------------------ТЗ----------------------------------------

-Проблемные буквы
"""
import random
import xml.etree.cElementTree as et
import sys



class Game(object):
    """ City's main game class """
    def __init__(self):
        self.inaccessible_pool = []
        self.available_pool = []
        self.__readCityNames(r"data\coutries.xml")
        self.previous_city = ""

    def gameMainLoop(self, text):
        try:
            text = text.upper()
            digit = self.__checkTrueDigit(text, self.previous_city)
            if digit == 0:
                return f'Вам на "{self.previous_city[-1]}"'
            else:
                check = self.__checkCityName(text)
                if check == 100:
                    return "Этот город уже назывался"
                elif check == 102:
                    return "Такого города в России нет"
                else:
                    self.__addCityToUsedPool(text)
                    return self.__getAnswer(text)
        except Exception as e:
            print("[MainLoop] :: ", e)

    def resetGame(self):
        self.available_pool += self.inaccessible_pool
        self.inaccessible_pool.clear()

    def sendUsedCitues(self):
        if not self.inaccessible_pool:
            return "Названных городов нет"
        else:
            names = ""
            for name in self.inaccessible_pool:
                names += name.capitalize() + ", "
            names = names[:-2]
            names += "."
            return names

    def __checkTrueDigit(self, user, bot):
        try:
            if bot != "":
                now_digit = user[0]
                bot_digi = bot[-1]
                if now_digit == bot_digi:
                    return 1
                else:
                    return 0
        except Exception as e:
            print("[Check digit] :: ", e)

    def __getAnswer(self, text):
        text = text[-1]
        random.shuffle(self.available_pool)
        for city in self.available_pool:
            if city[0] == text:
                self.previous_city = city
                return city.capitalize()

    def __readCityNames(self, file_name):
        """ Reading city names from file """
        try:
            tree = et.ElementTree(file=file_name)
            root = tree.getroot()
            for country in root.findall("city"):
                id = country.find("country_id").text
                if id == "3159":
                    name = country.find("name").text
                    self.available_pool.append(name.upper())
        except Exception as e:
            print("[Read city names] ::", e)
            sys.exit()

    def __checkCityName(self, city):
        if city in self.inaccessible_pool:
            return 100                      # Название находиться в недоступном пуле
        else:
            if city in self.available_pool:
                return 101                  # Название доступно для использования
            else:
                return 102                  # Такого города в России не существует
    
    def __addCityToUsedPool(self, city):
        self.inaccessible_pool.append(city)
        self.available_pool.remove(city)