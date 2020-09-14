import requests


response = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&
exclude=hourly,daily&appid=af349f763951ecf1e4ec9395b38aa701')

print(response)

#af349f763951ecf1e4ec9395b38aa701