import requests
from bs4 import BeautifulSoup

def get_base_url(article=None):
    url = 'https://www.coindesk.com/'
    if article is not None:
        url += article
    return url

def get_text(article=None):
    if article is not None:
        soup = BeautifulSoup(requests.get(get_base_url(article)).content, 'lxml')
        return ''.join([ item.text for item in soup.select('div.article-pharagraph') ])
    else:
        print('  Error: no article provided\n Format: main.py <article>\nExemple: main.py bitcoin-ekes-out-gains-but-remains-in-red-amid-broader-market-rebound')

if __name__ == "__main__":
    #Exemple local, sinon passer l'article en parametre de la fonction get_text(<article>)
    article = 'bitcoin-ekes-out-gains-but-remains-in-red-amid-broader-market-rebound'
    print(get_text(article))