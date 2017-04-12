import urllib.request
import os
import time
from bs4 import BeautifulSoup
import configparser
import timer
import digger
import bdHandler

config = configparser.RawConfigParser()
config.read('Regulations.ini')
print(config.get('parsing', 'base_name'))


def page_save():
    page = 1
    base_name = config.get('parsing', 'base_name')
    tags = input()
    link = digger.page_url_linker(str(page), tags)
    html = urllib.request.urlopen(link).read()
    url_list = digger.get_url_list(html)
    i = 0



    while i < len(url_list):
        with timer.Profiler() as p:
            id = digger.get_id(url_list[i])
            link = 'https://yande.re/post/show' + '/' + id
            html = urllib.request.urlopen(link).read()
            soup = BeautifulSoup(html, 'html.parser')

            bdHandler.write_db(url_list[i], base_name, soup)
            digger.image_download(url_list[i], tags, soup)
            i += 1


page_save()
