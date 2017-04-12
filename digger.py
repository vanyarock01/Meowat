from bs4 import BeautifulSoup
import os
import requests

def page_url_linker(number, tag):
    return 'https://yande.re/post?page=' + number + '&tags=' + tag


# Seriously, so you can define a blank page

empty_page = '<p>Nobody here but us chickens!</p>'


def if_empty(html):
    if empty_page in str(html):
        return True
    else:
        return False


def image_download(url, tag, soup):
    image_name = post_linker(url, soup) + '.' + url.split('.')[-1]
    destination = "D:\\pictures\\"+ tag + '\\'

    if not os.path.exists(destination):
        os.makedirs(destination, mode=0o777, exist_ok=False)

    destination += image_name

    s = requests.get(url)
    out = open(os.path.normpath(destination), "wb")
    out.write(s.content)
    out.close()
    return print('Complite', image_name)


def get_url_list(html):
    """ Function for getting all list on full size url on picture for this page"""
    soup = BeautifulSoup(html, 'html.parser')
    return [a['href'] for a in soup.findAll('a', {"class": "directlink largeimg"})]

# Link page algorithm

# https://yande.re/post?tags=                  | main
# https://yande.re/post?page=1&tags=           | also main
# https://yande.re/post?page=2&tags=vocaloid   | search pictures by tegs vocaloid in second page
# https://yande.re/post?tags=vocaloid+gumi+    | search pictures by tegs vocaloid & gumi


def get_tag_set(soup):
    return [li['data-name'] for li in soup.findAll('li', {"class": "tag-link"})]


def get_id(url):
    return url.split('/')[-1].split('%20')[1]


def post_linker(url,soup):
    return get_id(url) + ' - ' + str(get_tag_set(soup))[1:-1].replace('\'', '')


'''
def get_id_list(html):
    """ Function for getting all list of id picture for this page"""
    soup = BeautifulSoup(html, 'html.parser')
    get_id = soup.findAll('ul', id="post-list-posts")
    soup = BeautifulSoup(str(get_id), 'html.parser')
    id = [li['id'] for li in soup.findAll('li')]
    i = 0
    for s in id:
        id[i] = s[1:]
        i += 1
    return id
'''