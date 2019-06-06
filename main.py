import random as rnd
import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
from bot import Bot

# Авторизация для сообщества
vk = vk_api.VkApi(token="00b73157edcc1908a48d21a259762638b7cec649e01375e2dc70f5dc5a44f2ec88c6b80d66c85df03343f")
longpoll = VkLongPoll(vk)

# Функция отправки сообшений
def write_msg(user_id, random_id, message):
	vk.method("messages.send", {"user_id": user_id, "random_id": random_id, "message": message})

# Прием сообшений
print("\n ### The bot is running.")
for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			bot = Bot(event.user_id)
			random_id = rnd.randrange(1, 500, 1)
			write_msg(event.user_id, random_id, bot.new_message(event.text))