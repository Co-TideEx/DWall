from tkinter import *
import requests
import json

window = Tk()

#Weather Information
x = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Fishers&units=imperial&appid=70f51f3e60f38e95a87cc6695474f899")
api = json.loads(x.content)

y = api['main']
current_temprature = y['temp']
feelsLike = y['feels_like']
tempmin = y['temp_min']
tempmax = y['temp_max']
generalWeth = api['weather'][0]['main']

#Wind stuff
z = api['wind']
windSpeed = z['speed']
#Gets wind direction and converts it to NSEW
windDirection = z['deg']
sector = round((windDirection % 360)/45)
directions = ["N","NE","E","SE","S","SW","W","NW","N"]
windDirection = directions[sector]

#Air Quality
api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=46040&distance=25&API_KEY=F28BA57C-69E9-45FE-AE5D-4A398A258C67")

api = json.loads(api_request.content)
city = api[0]['ReportingArea']
quality = api[0]['AQI']
category = api[0]['Category']['Name']

#Labels and Grid
weatherInfo = Label(window, text="Weather: " + generalWeth + " High: " + str(tempmax) + " Low: " +str(tempmin))
weatherInfo.grid(row=4, column=0)

currentTemp = Label(window, text="Current Temp: " + str(current_temprature) + " Feels Like: " + str(feelsLike))
currentTemp.grid(row=5, column=0)

windInfo = Label(window, text="Wind Speed: " + str(windSpeed) + " Mph " + windDirection)
windInfo.grid(row=6, column=0)

airQuality = Label(window, text="Air Quality : " + str(quality) + " " + category)
airQuality.grid(row=7, column=0)

#User input
def submission():
    print(content1.get())
    print(content2.get())
#button labels
Label(window, text="City").grid(row=0)
Label(window, text="Zip Code").grid(row=1)

content1 = StringVar()
content2 = StringVar()
#entry boxes
e1 = Entry(window, textvariable=content1).grid(row=0, column=1)
e2 = Entry(window, textvariable=content2).grid(row=1, column=1)

Button(window, text='Submit', command=submission).grid(row=3, column=1, sticky=W, pady=4)

#mainloop
window.mainloop()