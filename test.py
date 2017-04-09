import urllib.request
import digger



#Seriously, so you can define a blank page
empty_page = '<p>Nobody here but us chickens!</p>'
base_name = 'id_base.txt'
tags = input()
link = digger.page_url_linker('1', tags)
print(link)
html = urllib.request.urlopen(link).read()

if  empty_page in str(html):
    print('empty page')
else:
    url_list = digger.get_url_list(html)
    id_list = digger.get_id_list(html)

    digger.write_base(id_list[1], base_name)
    short = digger.read_base(base_name)
    print(digger.find_id(id_list[10],base_name))