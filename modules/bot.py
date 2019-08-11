import random
import vk_requests

import lists

class Bot(object):
	""" Work with user messages """
	
	def __init__(self, user_id, token):
		self.APP_TOKEN = token
		self.USER_ID = user_id
		self.user_name = self.get_user_info()
		
	def new_message(self, message):
		""" Creating a new message """
		try:
			if message.upper() in lists.HELLO_Q:
				return random.choice(lists.HELLO_A) + self.user_name + random.choice(lists.SYMBOLS)
			elif message.upper() in lists.CREATOR_Q:
				return "https://vk.com/cact_us"
			elif message.upper() in lists.BYE_Q:
				return random.choice(lists.BYE_A)
			else:
				return "Я вас не понимаю.("
		except Exception as e:
			print("[New message] :: ", e)
	
	def get_user_info(self):
		""" Getting user information """

		try:
			api = vk_requests.create_api(service_token=self.APP_TOKEN)
			user = api.users.get(user_ids=self.USER_ID)
			return user[0]['first_name']
		except Exception as e:
			print("[Get user info] :: ", e)