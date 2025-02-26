import openai
import os
import pasteLocal as pl
import speech_recognition as sr 
import checkNik as cn
import pyttsx3
from pydub import AudioSegment
#converter o audio do GravacaoVoz em texto, caso a palavra Pesquisar for falada

# função de audio para texto
def AudiotoText(caminho_audio):
    audio = AudioSegment.from_file(caminho_audio) 
    audio.export("audio.wav", format="wav") # Converter para WAV 

    #Inicializar o reconhecedor
    reconhecedor = sr.Recognizer()

    #Abrir o arquivo de áudio
    with sr.AudioFile("audio.wav") as fonte:
        audio_gravado = reconhecedor.record(fonte)  # Ler o áudio

    #Tentar reconhecer o áudio
    try:
        texto = reconhecedor.recognize_google(audio_gravado, language='pt-BR')
        texto = texto.lower()
        print("Texto reconhecido:", texto)
        
        # VERIFICAÇÃO SE O NIK FOI ATIVO
        cn.check_Nik(texto)
        
    except sr.UnknownValueError:
        print("O Google Speech Recognition não conseguiu entender o áudio")
    except sr.RequestError as e:
        print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala: {e}")


def TexttoAudio(text):
    #tranformar audio em texto
    #Inicializa o mecanismo de conversão de texto em fala
    engine = pyttsx3.init()

    #Define a taxa de fala (opcional)
    engine.setProperty('rate', 150)  # Aumente ou diminua a taxa conforme necessário

    #Define o volume (opcional)
    engine.setProperty('volume', 1)  # Volume de 0.0 a 1.0

    #Define a voz (opcional)
    voices = engine.getProperty('voices')
    #Seleciona a voz masculina (geralmente a primeira voz é masculina)
    engine.setProperty('voice', voices[0].id)

    #Converte o texto em fala
    engine.say(text)