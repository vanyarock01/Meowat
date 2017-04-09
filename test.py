import urllib.request
import digger


# Link page algorithm

# https://yande.re/post?tags=                  | main
# https://yande.re/post?page=1&tags=           | also main
# https://yande.re/post?page=2&tags=vocaloid   | search pictures by tegs vocaloid in second page
# https://yande.re/post?tags=vocaloid+gumi+    | search pictures by tegs vocaloid & gumi


empty_page ='<p>Nobody here but us chickens!</p>'

tags = input()
link = "https://yande.re/post?tags=" + tags

html = urllib.request.urlopen(link).read()


if empty_page in str(html):
    print ('empty page')
else:
    url_list = digger.get_url_list(html)
    id_list = digger.get_id_list(html)
