from bs4 import BeautifulSoup
import requests
import os

def page_url_linker(number, tag):
    return 'https://yande.re/post?page=' + number + '&tags=' + tag


# Seriously, so you can define a blank page
empty_page = '<p>Nobody here but us chickens!</p>'
not_exist_page = '<h1>Requested page does not exist</h1>'


def if_empty(html):
    if empty_page in str(html):
        return False
    else:
        return True


def if_exist(html):
    if not_exist_page in str(html):
        return False
    else:
        return True


def image_download(url, tag, soup):

    """Create folder and download into it image"""

    image_name = post_linker(url, soup).replace('"', '') + '.' + url.split('.')[-1]
    destination = "D:\\pictures\\"+ tag + '\\'

    if not os.path.exists(destination):
        os.makedirs(destination, mode=0o777, exist_ok=False)

    destination += image_name

    s = requests.get(url)
    out = open(os.path.normpath(destination), "wb")
    out.write(s.content)
    out.close()
    return print('Completed', image_name)


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


