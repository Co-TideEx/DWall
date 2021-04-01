from tkinter import *
import requests
import json

window = Tk()

api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=46040&distance=25&API_KEY=F28BA57C-69E9-45FE-AE5D-4A398A258C67")

api = json.loads(api_request.content)
city = api[0]['ReportingArea']
quality = api[0]['AQI']
category = api[0]['Category']['Name']

airQuality = Label(window, text=city + " - Air Quality : " + str(quality) + " " + category)
airQuality.pack()

window.mainloop()