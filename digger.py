
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import urllib.request
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


def image_download(url, tag):

    destination = "D:\\pictures\\"+url.split('/')[-1]# os.path.join(tag,url.split('/')[-1]))
    #destination = os.path.join(destination,url.split('/')[-1])
    #print (os.path.normpath(destination))
    p = requests.get(url)
    out = open(os.path.normpath(destination), "wb")
    out.write(p.content)
    out.close()


def get_url_list(html):
    """ Function for getting all list on full size url on picture for this page"""
    soup = BeautifulSoup(html, 'html.parser')
    return [a['href'] for a in soup.findAll('a', {"class": "directlink largeimg"})]

def get_id(html):
    soup = BeautifulSoup(html, 'html.parser')
    return [a['href'] for a in soup.findAll('a', {"class": "thumb"})]


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

# Link page algorithm

# https://yande.re/post?tags=                  | main
# https://yande.re/post?page=1&tags=           | also main
# https://yande.re/post?page=2&tags=vocaloid   | search pictures by tegs vocaloid in second page
# https://yande.re/post?tags=vocaloid+gumi+    | search pictures by tegs vocaloid & gumi


def get_tag_set(id):
    link = 'https://yande.re/post/show'+ '/' + id
    print(link)
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, 'html.parser')
    return [li['data-name'] for li in soup.findAll('li', {"class": "tag-link"})]