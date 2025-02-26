import os
import pasteLocal as pl
import shutil
import audioConverter as ac
import time
      
# CONTROLLER
# responsável pela a análise da busca dos arquivos de áudio dentro da pasta SongSaver
def deleteFile(directory_path):
   try:
     files = os.listdir(directory_path)
     for file in files:
       file_path = os.path.join(directory_path, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
   except OSError:
        print("Algo de errado aconteceu ao tentar eliminar os arquivos do InUse")
def checkInUseAudio():
    print("aqui")
    caminho_atual = pl.paste()
    
    #Evitando que ocorra problemas, todos os arquivos pré-salvos no InUse são deletados
    in_use = caminho_atual+"\InUse"
    deleteFile(in_use)
    
    caminho_atual = caminho_atual+"\SongSaver"
    print(caminho_atual)
    arquvios = os.listdir(caminho_atual)
    print(arquvios)
    for arq in arquvios:
        nome, estensao = os.path.splitext(arq)

        print(estensao)

        if estensao == ".mp3" or estensao == ".wav":
            return arq, True
        
    return arq, False


def checkFileAudio():
    
    arquivo, result = checkInUseAudio()
    if result:
          path = pl.paste()
          #pegar esse arquivo e mover para a pasta InUse
          shutil.move(f'{path}/SongSaver/{arquivo}', f'{path}/InUse/') 
          
          #chame a função de áudio para texto
          arquvio = f'{path}/InUse/{arquivo}'
          ac.AudiotoText(arquvio)
        