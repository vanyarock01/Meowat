from bs4 import BeautifulSoup
import urllib.request
import configparser
import bdHandler
import digger
import timer

config = configparser.RawConfigParser()
config.read('Regulations.ini')
post_link = config.get('base', 'link')

tag = input('Enter tag for download: ')
page = input('Enter start page: ')

def page_save(tag, page):
    link = 'https://yande.re/post?page=' + str(page) + '&tags=' + tag
    html = urllib.request.urlopen(link).read()
    url_list = digger.get_url_list(html)

    if digger.if_empty(html) and digger.if_exist(html):
        num_pic = 0
        while num_pic < len(url_list):
            id = digger.get_id(url_list[num_pic])

            if bdHandler.if_save(url_list[num_pic]):
                print ('id: ',id, ' - downloaded before')
            else:

                with timer.count() as t:
                    link = post_link + '/' + id
                    html = urllib.request.urlopen(link).read()
                    soup = BeautifulSoup(html, 'html.parser')
                    bdHandler.write_db(url_list[num_pic], tag)
                    digger.image_download(url_list[num_pic], tag, soup)
            num_pic += 1
        print('Page №:', page, ' download')
        return page_save(tag,int(page) + 1)
    else:
        print('All picture save')
page_save(tag,page)
