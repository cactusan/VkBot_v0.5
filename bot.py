import random

import bs4 as bs4
import requests

class Bot:
	"""
	Отвечает на сообщения.
	"""
	def __init__(self, user_id):
		self.USER_ID = user_id
		self.HELLO = ["ПРИВЕТ", "ХАЙ", "ЗДРАВСТВУЙ"]
		self.HELLO_ANSWER = ["Привет!)", "Хай)", "Здравствуй))", "Hello my friend!"]
		self.BYE = ["Пока-пока!))", "До встречи!", "Увидимся)", "Славься хлеб!"]
		self.CREATOR = ["СОЗДАТЕЛЬ", "АВТОР", "РАЗРАБОТЧИК", "КТО ТВОЙ СОЗДАТЕЛЬ"]

	def new_message(self, message):
		# Привет
		if message.upper() in self.HELLO:
			return random.choice(self.HELLO_ANSWER)
		# Создатель
		elif message.upper() in self.CREATOR:
			return "https://vk.com/cact_us"
		elif message.upper() == "ПОКА":
			return random.choice(self.BYE)
		# Неизвестное сообщение
		else:
			return "Я вас не понимаю.("