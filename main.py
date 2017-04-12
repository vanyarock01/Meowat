import urllib.request
import os
import time

import configparser

import digger
import bdHandler



config = configparser.RawConfigParser()
config.read('Regulations.ini')
print (config.get('parsing', 'base_name'))


'''
def page_s():
    page = 1
    base_name = 'base_date.txt'
    tags = input()
    link = digger.page_url_linker(str(page), tags)

config = ConfigParser.RawConfigParser()
config.read('configuration.cfg')
print(config.get('parser', 'base_name'))
#html = urllib.request.urlopen(link).read()

print (bdHandler.read_base('base_date.txt'))
print(bdHandler.read_base('base_date.txt'))
url_list = digger.get_url_list(html)
id_list = digger.get_id(html)
i = 0
while i < len(url_list):
   bdHandler.write_db(url_list[i],'base_date.txt')
   i += 1

'''