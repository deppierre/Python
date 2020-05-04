import requests
from bs4 import BeautifulSoup

def get_base_url(article=None):
    url = 'https://www.coindesk.com'
    if article is not None:
        url += article
    return url

def get_text(article=None):
    if article is not None:
        soup = BeautifulSoup(requests.get(get_base_url(article)).content, 'lxml')
        return ''.join([ item.text for item in soup.find_all('div','article-pharagraph') ])
    else:
        print(' Error: no article provided\nFormat: get_text(<article>)')
        return None

def get_articles():
    articles = []
    soup = BeautifulSoup(requests.get(get_base_url('/news')).content, 'lxml')
    div = soup.find_all('div','text-content')
    for item in div:
        list = [ item for item in item.find_all('a',href=True) ]
        articles += [ item['href'].strip() for item in list if item['href'].count('/') == 1 ]
    return set(articles)
        
if __name__ == "__main__":
    for article in get_articles():
        print(get_text(article))
    print('-----\n {0} articles have been extracted \n-----'.format(len(get_articles())))