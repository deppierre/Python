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
        print('  Error: no article provided\n Format: get_text(<article>)\nExemple: get_text(bitcoin-ekes-out-gains-but-remains-in-red-amid-broader-market-rebound)')
        return None

if __name__ == "__main__":
    #Exemple local, sinon passer l'article en argument de la fonction get_text(<article>)
    article = 'bitcoin-ekes-out-gains-but-remains-in-red-amid-broader-market-rebound'
    print(get_text(article))