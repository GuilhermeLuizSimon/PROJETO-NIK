# Um pedaço da utilidade da captura das informações 

import requests
API_KEY = "API KEY"

# OU colocar com fixo "jundiai" OU perguntar ao usuário sua cidade
#nome da cidade
city_name = "jundiai"

# OpenWeather
link = f"https:// (...)"

requisicao = requests.get(link)

weather_time = requisicao.json()

description = weather_time['weather'][0]['description']
temp = weather_time['main'][0]['temp'] - 273.15
temp_max = weather_time['main'][0]['temp_max'] - 273.15
temp_min = weather_time['main'][0]['temp_min'] - 273.15