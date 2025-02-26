# RESPONSÁVEL PELO PROCESSO DE TRANSMISSÃO DE DADOS
# é o primeiro a ser ligado

import http.server
import socketserver
import webbrowser
import os
import sys
import pasteLocal as pl
import controller as con


# Define a porta que o servidor vai usar
PORT = 8000

# Define o diretório que será servido

# Obtém o caminho completo do diretório atual
caminho_atual = pl.paste()

DIRECTORY = caminho_atual

# Muda para o diretório especificado
os.chdir(DIRECTORY)

# Cria o handler para servir os arquivos
Handler = http.server.SimpleHTTPRequestHandler

# Inicia o servidor
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor iniciado na porta {PORT}")
    print(f"Acesse em: http://localhost:{PORT}")
    
    # Abre o navegador automaticamente
    #webbrowser.open_new_tab(f"http://localhost:{PORT}")
    
    # Mantém o servidor rodando
    print("Seridor Rodadndo!")
    while True: 
        con.checkFileAudio()
    httpd.serve_forever()


    # Felipe: Se a ideia geral é que apenas tenhamos que ligar esse unico arquivo para funcionar tudo
    # seria recomendado o arquivo gravacaoVoz.py ser retornado como uma função aqui
    # assim, só é necessário ligar esse arquivo que chama o gravacaoVoz.py que, consequentemente, chamaria 
    # todos os outros arquivos como funções, certo?
