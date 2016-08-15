import requests
import json

zipcode = "48917"
owmapikey = "30c2deb5375a3862235e730f122c40ad"
url = "http://api.openweathermap.org/data/2.5/weather?zip=%s,us&APPID=%s" % (zipcode,owmapikey)

def weatherTempF():
    fetchWeather = requests.get(url)
    weatherData = fetchWeather.json()
    currentTemp = weatherData['main']['temp']
    tempF = ("%.1f" % ((currentTemp * 9/5) - 459.67))
    return tempF