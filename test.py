import urllib.request
import digger
import swap
import requests



base_name = 'id_base.txt'
tags = input()
link = digger.page_url_linker('1', tags)
print(link)
html = urllib.request.urlopen(link).read()
# while digger.if_empty(html):



url_list = digger.get_url_list(html)
id_list = digger.get_id_list(html)
url = url_list[1]

r = requests.get(url)

swap.write_base(id_list[1], base_name)
short = swap.read_base(base_name)
print(swap.find_id(id_list[10],base_name))
print(url_list[1].split('/')[-1])
digger.image_download(url_list[1])