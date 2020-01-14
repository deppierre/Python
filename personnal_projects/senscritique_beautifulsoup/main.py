import json
import unidecode #pip3.8.exe install unidecode
import pathlib
import time
from os import path
import requests
from bs4 import BeautifulSoup

def get_base_url(user_name=None, page_no=1):
    url = 'https://www.senscritique.com/'
    if user_name is not None:
        url += user_name + '/collection/all/all/all/all/all/all/all/all/all/page-' + str(page_no)
    return url

def get_num_pages(url):
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    collection_pages = soup.find_all('a', {'class': 'eipa-anchor'})

    try:
        num_pages = int(collection_pages[-1].attrs['data-sc-pager-page'])
    except IndexError:
        num_pages = 1
    return num_pages

def improve_readability(text):
    return text.replace('\n', '').replace('\t', '')

def read_soup_result(soup_result, simplify_text=True):
    if simplify_text:
        text = [improve_readability(sample.text) for sample in soup_result]
    else:
        text = [sample.text for sample in soup_result]

    if len(text) == 1:
        text = text[0]

    if len(text) == 0 or text == ' ' or text == '-':
        text = None

    return text

def parse_keyword(user_name='wok'):
    url = get_base_url(user_name=user_name)
    num_pages = get_num_pages(url)

    data = dict()
    for page_no in range(num_pages):
        progress = (100 * page_no) // num_pages

        page_data = parse_collection_page(user_name=user_name, page_no=page_no)
        print(str(progress) + '%')
        data.update(page_data)

    return data

def parse_collection_page(user_name='wok', page_no=1):
    url = get_base_url(user_name=user_name, page_no=page_no)
    soup = BeautifulSoup(requests.get(url).content, 'lxml')

    collection_items = soup.find_all('li', 'elco-collection-item')

    data = dict()
    for item in collection_items:
        user_rating = item.find_all('div', {'class': 'elco-collection-rating user'})
        name = item.find_all('a', {'class': 'elco-anchor'})
        original_title = item.find_all('p', {'class': 'elco-original-title'})
        game_system = item.find_all('span', {'class': 'elco-gamesystem'})
        release_date = item.find_all('span', {'class': 'elco-date'})
        description = item.find_all('p', {'class': 'elco-baseline elco-options'})
        author = item.find_all('a', {'class': 'elco-baseline-a'})
        site_rating = item.find_all('a', {'class': 'erra-global'})
        item_id = name[0].attrs['id'].strip('product-title-')

        data[item_id] = dict()
        data[item_id]['name'] = unidecode.unidecode(read_soup_result(name))
        data[item_id]['original_title'] = read_soup_result(original_title)
        data[item_id]['author'] = read_soup_result(author)
        data[item_id]['user_rating'] = read_soup_result(user_rating)
        data[item_id]['site_rating'] = read_soup_result(site_rating)
        data[item_id]['description'] = unidecode.unidecode(read_soup_result(description))
        data[item_id]['game_system'] = read_soup_result(game_system)
        data[item_id]['release_date'] = read_soup_result(release_date)

        #Adaptation
        if data[item_id]['original_title'] == None: data[item_id]['original_title'] = data[item_id]['name']
        if data[item_id]['game_system'] != None: del data[item_id]

    return data

def print_data(data, file_name, debug):
    if debug == 1: print(data)
    # Reference of the following line: https://stackoverflow.com/a/14364249
    pathlib.Path('\\data').mkdir(parents=True, exist_ok=True)

    with open(file_name, 'w', encoding='utf8') as f:
        f.write(json.dumps(data))
    
    return

def parse_and_cache(user_name, debug = 0):
    json_filename_suffix = '.json'

    # Get current day as yyyymmdd format
    date_format = '%Y%m%d'
    current_date = time.strftime(date_format)

    # Database filename
    save_file_name = 'data/' + current_date + '_' + user_name + json_filename_suffix

    if pathlib.Path(save_file_name).is_file():
        with open(save_file_name, 'r', encoding='utf8') as f:
            data = json.load(f)
            print('You have ' + str(len(data)) + ' movies in cache')
            print('Cache file: ' + path.realpath(save_file_name))
            if debug == 1: print(data)
    else:
        data = parse_keyword(user_name=user_name)
        if len(data) > 0:
            print(str(len(data)) + ' movies extracted')
            print_data(data, save_file_name, debug)
    return data

def main(): 
    parse_and_cache(user, debug)

if __name__== "__main__":
    user = 'deppierre'
    debug = 1

#MAIN
main()
