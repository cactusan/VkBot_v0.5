import requests

class Weather:
	""" Finds weather information in the specified city """
	def __init__(self, user_id):
		self.CITY_ID = 0
		self.APPID = "f72fd1bcfc594edd13ada64798f9da2f"

	def searchCity(self, city):
		""" Search city id """
		try:
			res = requests.get("http://api.openweathermap.org/data/2.5/find", params = {"q": city, "type": "like", "units": "metric", "APPID": self.APPID})
			data = res.json()
			self.CITY_ID = data["list"][0]["id"]
			return self.CITY_ID
		except Exception as e:
			print("[Search city] :: ", e)
			pass

	def find_out_the_weather(self, city_id, city):
		""" Receiving weather information in the specified city """
		try:
			res = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {"id": city_id, "units": "metric", "lang": "ru", "APPID": self.APPID})
			data = res.json()
			main_weather = data['weather'][0]['main']
			weather_description = data["weather"][0]["description"]
			main_temp = data['main']['temp']
			humidity = data['main']['humidity']
			pressure = 	data['main']['pressure']
			wind_speed = data['wind']['speed']
			message = f"""
			Погода в {city}: 				{main_weather}
			Состояние: 						{weather_description}
			Температура: 					{main_temp} °С
			Влажность:						{humidity} %
			Давление: 						{pressure} мм рт.ст
			Скорость ветра: 				{wind_speed} м/с
			"""
			return message
		except Exception as e:
			print("[Find out the weather] :: ", e)
			pass