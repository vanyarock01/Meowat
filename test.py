from bs4 import BeautifulSoup
import urllib.request



# https://yande.re/post?tags=                  | main
# https://yande.re/post?page=1&tags=           | also main
# https://yande.re/post?page=2&tags=vocaloid   | search pictures by tegs vocaloid in second page
# https://yande.re/post?tags=vocaloid+gumi+    | search pictures by tegs vocaloid & gumi

tags = input()
link = "https://yande.re/post?tags=" + tags

with urllib.request.urlopen(link) as url:
    html = url.read()


soup = BeautifulSoup(html, 'html.parser')
full_img_links = {a['href'] for a in soup.findAll('a', {"class": "directlink largeimg"})}
print(full_img_links)
