import requests

#Substitua pela sua chave de API da NewsAPI
api_key = 'sua_chave_de_api'

#Palavra-chave que você deseja pesquisar (pode ser qualquer coisa)
keyword = 'tecnologia'

#Definir o URL com a pesquisa personalizada
url = f'https://newsapi.org/v2/everything?q={keyword}&language=pt&pageSize=3&apiKey={api_key}'

#Fazer a requisição GET para a NewsAPI
response = requests.get(url)

#Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()

    # Exibir as notícias encontradas
    for article in data['articles']:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("-" * 50)
else:
    print(f"Erro na requisição: {response.status_code}")