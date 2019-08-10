import random as rnd
import requests

from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api

from bot import Bot
from weather import Weather

class BotMainLoop(object):
	""" Bot main class """

	def __init__(self):
		self.app_token = "00b73157edcc1908a48d21a259762638b7cec649e01375e2dc70f5dc5a44f2ec88c6b80d66c85df03343f"
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
								bot = Weather(event.user_id)
								try:
									city_id = bot.find_city(text[1])
									city = bot.upper_name(text[1])
									message = bot.find_out_the_weather(city_id, city)
									self.write_msg(event.user_id, random_id, message)
								except Exception as e:
									print("[Incorrect input] :: ", e)
									self.write_msg(event.user_id, random_id, "Не могу найти информацию по Вашему запросу.")
							# Общение с ботом
							else:
								self.write_msg(event.user_id, random_id, bot.new_message(event.text))
			except:
				print("[The bot is off]")
				exit = True



if __name__ == "__main__":
	BotMainLoop()