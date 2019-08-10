import random as rnd
import requests

from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api

from bot import Bot
from weather import Weather

class BotMainLoop(object):
	""" Bot main class """

	def __init__(self):
		self.app_token = ""
		self.vk = vk_api.VkApi(token=self.app_token)
		self.longpoll = VkLongPoll(self.vk)
		self.loop()

	def write_msg(self, user_id, random_id, message):
		""" Message sending function"""

		self.vk.method("messages.send", {"user_id": user_id, "random_id": random_id, "message": message})

	def loop(self):
		""" Main bot cycle """

		print("[The bot is running]")
		exit = False
		while not exit:
			try:
				# Прием сообшений
				for event in self.longpoll.listen():
					if event.type == VkEventType.MESSAGE_NEW:
						if event.to_me:
							bot = Bot(event.user_id, self.app_token)
							random_id = rnd.randrange(1, 500, 1)
							text = event.text.split(" ")
							# Если пользователь хочет узнать погоду.
							if text[0].upper() == "ПОГОДА":
								weather_mod = Weather(event.user_id)
								try:
									city_id = weather_mod.searchCity(text[1])
									city = text[1].capitalize()
									message = weather_mod.find_out_the_weather(city_id, city)
									self.write_msg(event.user_id, random_id, message)
								except Exception as e:
									print("[Incorrect city input] :: ", e)
									self.write_msg(event.user_id, random_id, "Не могу найти информацию по Вашему запросу.")
							# Общение с ботом
							else:
								self.write_msg(event.user_id, random_id, bot.new_message(event.text))
			except:
				print("[The bot is off]")
				exit = True



if __name__ == "__main__":
	BotMainLoop()