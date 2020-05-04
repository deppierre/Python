import sys, requests
from bs4 import BeautifulSoup

def get_base_url(article=None):
    url = 'https://www.coindesk.com/'
    if article is not None:
        url += article
    return url

def get_text(article=None):
    try:
        article = sys.argv[1]
    except IndexError:
        print('  Error: no article provided\n Format: main.py <article>\nExemple: main.py bitcoin-ekes-out-gains-but-remains-in-red-amid-broader-market-rebound')
    
    if article is not None:
        soup = BeautifulSoup(requests.get(get_base_url(article)).content, 'lxml')
        return ''.join([ item.text for item in soup.select('div.article-pharagraph') ])

if __name__ == "__main__":
    #Exemple mis en dur, sinon passer l'article en parametre du fichier main
    article = 'bitcoin-ekes-out-gains-but-remains-in-red-amid-broader-market-rebound'
    print(get_text(article))