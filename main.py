import urllib.request
import os
import time

import configparser

import digger
import bdHandler



config = configparser.RawConfigParser()
config.read('Regulations.ini')
print (config.get('parsing', 'base_name'))


def page_save():
    page = 1
    base_name = config.get('parsing', 'base_name')
    tags = input()
    link = digger.page_url_linker(str(page), tags)
    html = urllib.request.urlopen(link).read()
    print (bdHandler.read_base('base_date.txt'))
    url_list = digger.get_url_list(html)
    i = 0
    while i < len(url_list):

        bdHandler.write_db(url_list[i],'base_date.txt')

        digger.image_download(url_list[i],tags)
        i += 1

page_save()