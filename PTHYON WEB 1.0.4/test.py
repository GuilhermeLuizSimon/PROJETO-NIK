# import os
# caminho_atual = os.getcwd()
# caminho_atual = caminho_atual+"/SongSaver"

# arquvios = os.listdir(caminho_atual)

# print(arquvios)


# for arq in arquvios:
#     nome, estensao = os.path.splitext(arq)

#     print(estensao)

#     if estensao == ".mp3" or estensao == ".wav":
#         print(f"{arq} é um arquivo de áudio")

tema = ["Oi","Ola"]
texto = "Ola amigo"

if tema in texto:
    print(True)