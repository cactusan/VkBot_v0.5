"""
----------------------------------------ТЗ----------------------------------------

-Пользователь пишет "Поиграем в города"
-Бот отвечает и предлагает пользователю первому назвать город
-Бот проверяет нет ли этого названия в списке названных городов
    -Если город уже был назван, то Бот сообщает об этом
    -Ждет название города
-Бот проверяет город в списке не названных городов
    -Если такого города в России нет, Бот сообщает об этом
    -Если название верно, то добавляет город в список использованных городов
    -Ждет название города
-Бот называет город из списка не названных городов
    -На последнюю букву названного пользователем города Бот в списке не названных городов находит "случайный" подходящий город
        (список каждый раз перемешивается) и говорит пользователю
    -Если название верно, то добавляет город в список использованных городов
    -Ждет название города
-Бот ждет команды "Стоп" или название города
"""
import random



class Game(object):
    """ City's main game class """
    def __init__(self):
        self.inaccessible_pool = []
        self.available_pool = []
        self.__readCityNames()

    def __readCityNames(self):
        """ Reading city names from file """
        with open(r"modules\RussiaCities.txt", "r") as file:
            for city in file:
                city = city[:-1]
                self.available_pool.append(city.upper())

    def gameMainLoop(self, text):
        text = text.upper()
        check = self.__checkCityName(text)
        if check == 100:
            return "Этот город уже назывался"
        elif check == 102:
            return "Такого города в России нет"
        else:
            self.__addCityToUsedPool(text)
            return "OK"

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

    def resetGame(self):
        self.available_pool += self.inaccessible_pool
        self.inaccessible_pool.clear()

    def sendUsedCitues(self):
        names = ""
        for name in self.inaccessible_pool:
            names += name.capitalize() + ", "
        names = names[:-2]
        names += "."
        return names