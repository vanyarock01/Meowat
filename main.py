import urllib.request
import os
import time

import digger
import bdHandler

page = 1
base_name = 'base_date.txt'
tags = input()
link = digger.page_url_linker(str(page), tags)
print(link)
html = urllib.request.urlopen(link).read()

url_list = digger.get_url_list(html)
id_list = digger.get_id(html)
i = 0
id = url_list[0].split('/')[-1].split('%20')[1]

while i < len(url_list):
   bdHandler.write_db(url_list[i],'base_date.txt')
   i += 1

