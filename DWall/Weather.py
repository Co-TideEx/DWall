from tkinter import *
import requests
import json

window = Tk()

#Weather Map
x = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Indiana&units=imperial&appid=70f51f3e60f38e95a87cc6695474f899")
api = json.loads(x.content)

y = api['main']
current_temprature = y['temp']
feelsLike = y['feels_like']
tempmin = y['temp_min']
tempmax = y['temp_max']

weather = Label(window, text= str(current_temprature) + " Feels Like: " + str(feelsLike))
weather.pack()

#Air Quality
api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=46040&distance=25&API_KEY=F28BA57C-69E9-45FE-AE5D-4A398A258C67")

api = json.loads(api_request.content)
city = api[0]['ReportingArea']
quality = api[0]['AQI']
category = api[0]['Category']['Name']

airQuality = Label(window, text=city + " - Air Quality : " + str(quality) + " " + category)
airQuality.pack()

window.mainloop()