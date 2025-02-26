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

import os

directory_path = "InUse"
try:
    files = os.listdir(directory_path)
    for file in files:
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
except OSError:
    print("Error occurred while deleting files.")