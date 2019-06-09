import requests

class Weather:
	"""
	Показывает информацию о погоде в указанном пользователем городе.
	"""
	def __init__(self, user_id):
		self.CITY_ID = 0
		self.APPID = "f72fd1bcfc594edd13ada64798f9da2f"

	def upper_name(self, city):
		city = list(city)
		city[0] = city[0].upper()
		city = "".join(city)
		return city

	def find_city(self, city):
		"""
		Поиск id нужного города.
		"""
		try:
			res = requests.get("http://api.openweathermap.org/data/2.5/find",
							params = {"q": city, "type": "like", "units": "metric", "APPID": self.APPID})
			data = res.json()
			cities = ["{} ({})".format(d["name"], d["sys"]["country"])
						for d in data["list"]]
			self.CITY_ID = data["list"][0]["id"]
			return self.CITY_ID
		except Exception as e:
			print("Exception (find): ", e)
			pass

	def find_out_the_weather(self, city_id, city):
		"""
		Вывод погоды в указанном городе.
		"""
		try:
			res = requests.get("http://api.openweathermap.org/data/2.5/weather",
							params = {"id": city_id, "units": "metric", "lang": "ru", "APPID": self.APPID})
			data = res.json()
			message = "Погода в {}:\nСостояние:		{}\nТемпература:		{}\nМинимальная температура:		{}\nМаксимальная температура:	{}\n".format(city, data["weather"][0]["description"], 
																																									data['main']['temp'], 
																																									data['main']['temp_min'], 
																																									data['main']['temp_max'])
			return message

		except Exception as e:
			print("Exception (weather): ", e)
			pass