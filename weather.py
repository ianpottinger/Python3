
import requests

def weather_query():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=e9185b28e9969fb7a300801eb026de9c'
    response = requests.get(url)
    data = response.json()
    print(data)

weather_query()


r = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
print(r.json())

url = "https://api.coindesk.com/v1/bpi/currentprice/GBP.json"
response = requests.get(url)
data = response.json()
rate = data["bpi"]["GBP"]["rate"]
print("1 BTC = " + rate + " GBP")
