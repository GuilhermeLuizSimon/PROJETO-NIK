import os
import Commands.ai_ollama as ollama
import Commands.hour as hour
import Commands.music as music
import Commands.news as news
import Commands.weather as weather
import controller as ctrl
import pasteLocal as pl

def check_Nik(texto):
    texto = texto.lower()
    path = pl.paste()
    nik_active = False
    ativaction_words = ['niq','nique','nike','nik','nic','nick','nyc','neek','nikke','nyk','nyq','nyque',
                        'nyke','nykke','nyck','knick','nicke','nikki']
    
    for nik in ativaction_words:
        if nik in texto:
            nik_active = True
            break
    
    if nik_active:
            print("Foi ouvido NIK")
            #nik foi ativado
            #terminar código depois
            """ 
            #verificar se "Pesquisa" foi dito:
            if texto in ["pesquise","pesquisar"]:
                response = ollama.Ai_ollama(texto)
            
            #verificar se "Horas" foi dito:
            elif texto in ["horas","dia","dia da semana","mês","mes","ano","horário","horario"]:
                response = hour.Ai_hour(texto)
            
            #verificar se "Musica" foi dito:
            elif texto in ["toque a musica"]:
                response = music.Ai_music(texto)
            
            #verificar se "noticias" foi dito:
            elif texto in ["noticias","noticia"]:
                response = news.Ai_news(texto)
            
            #verificar se "Clima" foi dito:
            elif texto in ["clima","previsao do tempo","previsao","previsão","previsão do tempo","tempo"]:
                response = weather.Ai_weather(texto)
            
            else:
                response = ""           
        
        """
        #não importa o resultado
    path = path + "\InUse"
    ctrl.deleteFile(path)