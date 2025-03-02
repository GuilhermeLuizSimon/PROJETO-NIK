#########################################################################
# CONVERTOR DE ÁUDIO
#########################################################################
# responsável pela conversão dos áudios

import openai
import os, time
import speech_recognition as sr 
import checkNik as checkN
import pyttsx3
from pydub import AudioSegment
# import gtts
#converter o audio do GravacaoVoz em texto, caso a palavra Pesquisar for falada

# função de audio para texto
def AudiotoText(nome_arquivo):
    r = sr.Recognizer()

    with sr.AudioFile(nome_arquivo) as source:
        audio = r.record(source)  # Lê o arquivo de áudio
    try:
        texto = r.recognize_google(audio, language='pt-BR')  # Reconhece o áudio
        print("Texto reconhecido:", texto)
        
        # Verifica se a palavra "NIK" foi mencionada
        checkN.check_Nik(texto)
        
    except sr.UnknownValueError:
        print("Não consegui entender o áudio.")
    except sr.RequestError as e:
        print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala: {e}")



def TexttoAudio(text):
    print(f"texto par audio: {text}")
    # time.sleep(1.0)

    # # Criação do objeto gTTS
    # tts = gtts.gTTS(text=text, lang='pt-br')  

    # # Salvando o áudio em um arquivo
    # tts.save("Esp32/command.mp3")

    # # Opcional: Reproduzir o áudio (apenas em sistemas que suportam)
    # os.system("start command.mp3")


    # ===================================================================================
    # #tranformar audio em texto
    # #Inicializa o mecanismo de conversão de texto em fala
    # engine = pyttsx3.init()

    # #Define a taxa de fala (opcional)
    # engine.setProperty('rate', 150)  # Aumente ou diminua a taxa conforme necessário

    # #Define o volume (opcional)
    # engine.setProperty('volume', 1)  # Volume de 0.0 a 1.0

    # # #Define a voz (opcional)
    # voices = engine.getProperty('voices')

    # #Seleciona a voz masculina (geralmente a primeira voz é masculina)
    # engine.setProperty('voice', voices[0].id)

    # # Converte o texto em fala
    # engine.say(text)
    # engine.runAndWait()
    # engine.stop()
    
    #=================================================================================
    # The text that you want to convert to audio

    # Language in which you want to convert
    # language = 'pt'

    # # Passing the text and language to the engine, 
    # # here we have marked slow=False. Which tells 
    # # the module that the converted audio should 
    # # have a high speed
    # myobj = gTTS(text=text, lang=language, slow=False, tld='com.br')

    # # Saving the converted audio in a mp3 file named
    # # welcome 
    # myobj.save("Esp32/welcome.mp3")

    # # Initialize the mixer module
    # pygame.mixer.init()

    # # Load the mp3 file
    # pygame.mixer.music.load("Esp32/welcome.mp3")

    # # Play the loaded mp3 file
    # pygame.mixer.music.play()
    
# ================================================================================
    #     # Inicializa o mecanismo de TTS
    engine = pyttsx3.init()

    # Obtém as vozes disponíveis
    vozes = engine.getProperty('voices')

    # Seleciona a voz masculina (geralmente a primeira ou a segunda)
    for voz in vozes:
        if 'masculino' in voz.name.lower():  # Verifica se a voz é masculina
            engine.setProperty('voice', voz.id)
            break

    # Define a taxa de fala (opcional)
    engine.setProperty('rate', 150)  # Aumente ou diminua a taxa conforme necessário

    # Converte o texto em fala
    engine.say(text)
    engine.save_to_file(text,'Esp32/command.mp3')

    # Aguarda até que a fala termine
    engine.runAndWait()
    
    # ============================================================================
    # import boto3

    # # Inicializa o cliente do Polly
    # voz = 'Ricardo'
    # polly = boto3.client('polly')

    # # Solicita a síntese de fala
    # response = polly.synthesize_speech(
    #     Text=text,
    #     OutputFormat='mp3',
    #     VoiceId=voz
    # )

    # # Salva o áudio gerado
    # with open("Esp32/audio.mp3", "wb") as file:
    #     file.write(response['AudioStream'].read())

    # # Reproduz o áudio
    # os.system("start Esp32/audio.mp3")  # Para Windows, use "start", para Linux use "xdg-open"

