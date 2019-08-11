import random
import requests
import sys

from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import vk_requests

sys.path.insert(1, r'modules')
from weather import Weather
import cities
import lists

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

	def get_user_info(self, id):
		""" Getting user information """
		try:
			api = vk_requests.create_api(service_token=self.app_token)
			user = api.users.get(user_ids=id)
			return user[0]['first_name']
		except Exception as e:
			print("[Get user info] :: ", e)

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
							random_id = random.randrange(1, 500, 1)
							text = event.text
							command = event.text.split(" ")
							if text.upper() in lists.HELLO_Q:
								user_name = self.get_user_info(event.user_id)
								message = random.choice(lists.HELLO_A) + user_name + random.choice(lists.SYMBOLS)
								self.write_msg(event.user_id, random_id, message)
							elif text.upper() in lists.CREATOR_Q:
								message = "https://vk.com/cact_us"
								self.write_msg(event.user_id, random_id, message)
							elif text.upper() in lists.BYE_Q:
								message = random.choice(lists.BYE_A)
								self.write_msg(event.user_id, random_id, message)
							# Если пользователь хочет узнать текущую погоду.
							elif command[0].upper() == "ПОГОДА":
								weather_mod = Weather()
								try:
									city_id = weather_mod.searchCity(command[1])
									city = command[1].capitalize()
									message = weather_mod.current_weather(city_id, city)
									self.write_msg(event.user_id, random_id, message)
								except Exception as e:
									print("[Incorrect city input (current weather)] :: ", e)
									self.write_msg(event.user_id, random_id, "Не могу найти информацию по Вашему запросу.")
							# Если пользователь хочет узнать прогноз погоды.
							elif command[0].upper() == "ПРОГНОЗ":
								weather_mod = Weather()
								try:
									city_id = weather_mod.searchCity(command[1])
									city = command[1].capitalize()
									days = int(command[2])
									message = weather_mod.weather_forecast(city_id, city, days)
									# self.write_msg(event.user_id, random_id, message)
									self.write_msg(event.user_id, random_id, "Данная функция находится в разработке.")
								except Exception as e:
									print("[Incorrect city input (weather forecast)] :: ", e)
									self.write_msg(event.user_id, random_id, "Не могу найти информацию по Вашему запросу.")
							# Общение с ботом
							else:
								message = "Я вас не понимаю.("
								self.write_msg(event.user_id, random_id, message)
			except:
				print("[The bot is off]")
				exit = True



if __name__ == "__main__":
	BotMainLoop()