import requests
from settings import owmapikey, zipcode

url = "http://api.openweathermap.org/data/2.5/weather?zip={},us&APPID={}".format(zipcode,owmapikey)


def weatherTempF():
    try:
        try:
            resp = requests.get(url)
            if resp.ok:
                currentTemp = resp.json()['main']['temp']
                tempF = ("%.1f" % ((currentTemp * 9/5) - 459.67))
            else:
                tempF = "0"
        except Exception:
            tempF = "APIERR"
    except requests.exceptions.RequestException as e:
        tempF = "NOCONN"
    return tempF


def weatherIconF():
    try:
        resp = requests.get(url)
        if resp.ok:
            iconCode = resp.json()['weather'][0]['id']
        else:
            iconCode = "711"
    except Exception:
        iconCode = "711"
    return iconCode