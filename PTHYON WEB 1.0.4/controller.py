import os
import pasteLocal as pl
import shutil
import audioConverter as ac
      
# CONTROLLER
# responsável pela a análise da busca dos arquivos de áudio dentro da pasta SongSaver

def checkFileAudio():
    caminho_atual = pl.paste()
    caminho_atual = caminho_atual+"/SongSaver"

    arquvios = os.listdir(caminho_atual)

    print(arquvios)


    for arq in arquvios:
        nome, estensao = os.path.splitext(arq)

        print(estensao)

        if estensao == ".mp3" or estensao == ".wav":
            #pegar esse arquivo e mover para a pasta InUse
            shutil.move(f'SongSaver\{nome}{estensao}', f'InUse/{nome}{estensao}')   
            #chame a função de áudio para texto
            ac.AudiotoText()
            break