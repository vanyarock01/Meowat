from bs4 import BeautifulSoup
from urllib.request import urlretrieve


def get_url_list(html):
    """ Function for getting all list on full size url on picture for this page"""
    soup = BeautifulSoup(html, 'html.parser')
    return [a['href'] for a in soup.findAll('a', {"class": "directlink largeimg"})]


def get_id_list(html):
    """ Function for getting all list of id picture for this page"""
    soup = BeautifulSoup(html, 'html.parser')
    get_id = soup.findAll('ul', id="post-list-posts")
    soup = BeautifulSoup(str(get_id), 'html.parser')
    return [li['id'] for li in soup.findAll('li')]


# Link page algorithm

# https://yande.re/post?tags=                  | main
# https://yande.re/post?page=1&tags=           | also main
# https://yande.re/post?page=2&tags=vocaloid   | search pictures by tegs vocaloid in second page
# https://yande.re/post?tags=vocaloid+gumi+    | search pictures by tegs vocaloid & gumi

def page_url_linker(number, tag):
    return 'https://yande.re/post?page=' + number + '&tags=' + tag


# Seriously, so you can define a blank page

empty_page = '<p>Nobody here but us chickens!</p>'


def if_empty(html):
    if empty_page in str(html):
        return True
    else:
        return False


def image_download(url):
    destination = 'D:\''+ url.split('/')[-1]
    urlretrieve(url, destination)
