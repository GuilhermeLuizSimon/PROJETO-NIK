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
        meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        month = meses[month]
        #Dia da Semana
        week = clock.weekday()

        day_week = weekdays[week]

        if command in ['horas']:
                return f'O horário atual é {hour} horas e {minutes} minutos'
                
        if command in ['dia da semana']:
                return f'Hoje é {day_week}'
                
        if command in ['dia'] and not(command in ['mes'] or command in ['ano']):
                
                return f'Hoje é dia {day} de {month} de {year}'
                
        if command in ['mes']:
               return f'O mês de hoje é {month}'
                
                
        if command in ['ano']:
                return f'O ano atual é {year}'
                


