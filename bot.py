import random

import bs4 as bs4
import requests

import lists

class Bot:
	"""
	Отвечает на сообщения.
	"""
	def __init__(self, user_id):
		self.USER_ID = user_id

	def new_message(self, message):
		# Привет
		if message.upper() in lists.HELLO_Q:
			return random.choice(lists.HELLO_A)
		# Создатель
		elif message.upper() in lists.CREATOR_Q:
			return "https://vk.com/cact_us"
		elif message.upper() in lists.BYE_Q:
			return random.choice(lists.BYE_A)
		# Неизвестное сообщение
		else:
			return "Я вас не понимаю.("