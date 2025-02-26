# AI de coleta da HORA
# transformar tudo isso em uma função que possa ser chamada

# !!!
# Se a estrutura da pesquisa se mantiver a mesma, a coleta
# dos dados vei ocorrer conforme o esperado
from datetime import datetime, date

def Ai_hour(command):
        
        # PODE RETORNAR:
        # Horário
        # Dia
        # Dia da semana
        
        print("a")
    #Coleta do ANO/MES/DIA
        data = date.today()
        year = data.year
        month = data.month
        day = data.day

        print(f"{day}/{month}/{year}",end=" ")

        #Coleta da HORA/MINUTOS
        clock = datetime.now()
        hour = clock.hour
        minutes = clock.minute

        print(f"{hour}h{minutes}min\n Hoje é ",end="")

        weekdays = ["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]
        #Dia da Semana
        week = clock.weekday()

        day_week = weekdays[week]

