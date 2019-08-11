import requests
from datetime import datetime
import json

class Weather:
	""" Finds weather information in the specified city """
	def __init__(self):
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

	def parseUTC_Time(self, time):
		""" Time conversion from UTC to human-readable form """
		time = int(time)
		return datetime.utcfromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S")

	def current_weather(self, city_id, city):
		""" Receiving weather information in the specified city """
		try:
			res = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {"id": city_id, "units": "metric", "lang": "ru", "APPID": self.APPID})
			data = res.json()
			time = self.parseUTC_Time(data['dt'])
			weather_description = data["weather"][0]["description"]
			main_temp = data['main']['temp']
			humidity = data['main']['humidity']
			pressure = 	data['main']['pressure']
			wind_speed = data['wind']['speed']
			message = f"""
			Погода в {city}:
			Состояние: 						{weather_description}
			Температура: 					{main_temp} °С
			Влажность:						{humidity} %
			Давление: 						{pressure} мм рт.ст
			Скорость ветра: 				{wind_speed} м/с

			Данные получены {time} по UTC 
			p.s Москва +3 часа
			"""
			return message
		except Exception as e:
			print("[Find out the current weather] :: ", e)

	def weather_forecast(self, city_id, city, days):
		"""Receiving weather forecast information in the specified city"""
		try:
			res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params = {"id": city_id, "cnt": days, "units": "metric", "lang": "ru", "APPID": self.APPID})
			data = res.json()
		except Exception as e:
			print("[Weather forecast] :: ", e)