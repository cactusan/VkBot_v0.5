import datetime
import bs4 as bs4
import requests

class Bot:
	"""
	Отвечает на сообщения.
	"""
	def __init__(self, user_id):
		self.USER_ID = user_id
		self.COMMANDS = ["ПРИВЕТ", "СОЗДАТЕЛЬ", "ВРЕМЯ"]

	def get_time(self):
		time = datetime.datetime.now().strftime("%H:%M")
		return str(time)

	def new_message(self, message):
		# Привет
		if message.upper() == self.COMMANDS[0]:
			return "Привет!"
		# Создатель
		elif message.upper() == self.COMMANDS[1]:
			return "https://vk.com/cact_us"
		# Время
		elif message.upper() == self.COMMANDS[2]:
			return self.get_time()
		# Неизвестное сообщение
		else:
			return "Я вас не понимаю."