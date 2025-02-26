# Um pedaço da utilidade da captura das informações 

# AI de coleta do CLIMA
# transformar tudo isso em uma função que possa ser chamada

# !!!
# Se a estrutura da pesquisa se mantiver a mesma, a coleta
# dos dados vei ocorrer conforme o esperado

#---------------------------------------------------------------------------------------
# (AVISO) GUILHERME
# quando for colocar no computador de servidor, fazer login e substituir a API atual
# e colocar sua nova no lugar
# Link do site: https://openweathermap.org/
#---------------------------------------------------------------------------------------

import requests

def Ai_weather(command):
    API_key = "6da14a8a13f5492d2e6c433c9aec555d"

    # OU colocar com fixo "jundiai" OU perguntar ao usuário sua cidade
    #nome da cidade
    city_name = "sao paulo"

    # OpenWeather
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"

    print(link)
    requisicao = requests.get(link)

    weather_time = requisicao.json()
    description = weather_time['weather'][0]['description']
    temp = weather_time['main']['temp'] - 273.15
    temp_max = weather_time['main']['temp_max'] - 273.15
    temp_min = weather_time['main']['temp_min'] - 273.15

    # APRESENTAÇÃO DOS DADOS DE TESTE,
    # alterar depois a partir do que tem que ser apresentado para o NIK
    # ou seja, retornar texto com as informações e passar para a 
    # função TexttoAudio(text) do audioConverter.py

    print(f"Descrição: {description}, Temperatura: {temp}ºC\n temp_max: {temp_max}\n temp_min: {temp_min}")