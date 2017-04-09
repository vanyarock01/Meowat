from bs4 import BeautifulSoup
import urllib.request
import re


# https://yande.re/post?tags=                  | main
# https://yande.re/post?page=1&tags=           | also main
# https://yande.re/post?page=2&tags=vocaloid   | search pictures by tegs vocaloid in second page
# https://yande.re/post?tags=vocaloid+gumi+    | search pictures by tegs vocaloid & gumi

tags = input()
link = "https://yande.re/post?tags=" + tags

with urllib.request.urlopen(link) as url:
    html = url.read()


soup = BeautifulSoup(html, 'html.parser')
get = soup.findAll('ul', id="post-list-posts")


full_img_links = {a['href'] for a in soup.findAll('a', {"class": "directlink largeimg"})}
print(full_img_links)
soup = BeautifulSoup(str(get), 'html.parser')
#ul id="post-list-posts"
#print (get.find_all("li", text="creator-id-"))
post_base = soup.li['id']
post_base = {li['id'] for li in soup.findAll('li')}
print (post_base)
