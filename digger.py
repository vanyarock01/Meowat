from bs4 import BeautifulSoup


def get_url_list(html):
    """ Function for getting all list on full size url on picture for this page"""
    soup = BeautifulSoup(html, 'html.parser')
    return [a['href'] for a in soup.findAll('a', {"class": "directlink largeimg"})]


def get_id_list(html):
    """ Function for getting all list of id picture for this page"""
    soup = BeautifulSoup(html, 'html.parser')
    get_id = soup.findAll('ul', id="post-list-posts")
    soup = BeautifulSoup(str(get_id), 'html.parser')
    return [li['id'] for li in soup.findAll('li')]


def write_base(file_id, file_name):
    f = open(file_name, 'a')
    f.write(file_id + ' ')
    f.close()


def read_base(file_name):
    f = open(file_name)
    res = f.read().split()
    f.close()
    return res


# Link page algorithm

# https://yande.re/post?tags=                  | main
# https://yande.re/post?page=1&tags=           | also main
# https://yande.re/post?page=2&tags=vocaloid   | search pictures by tegs vocaloid in second page
# https://yande.re/post?tags=vocaloid+gumi+    | search pictures by tegs vocaloid & gumi

def page_url_linker(number, tag):
    return 'https://yande.re/post?page=' + number + '&tags=' + tag


def find_id(file_id, file_name):
    if file_id in read_base(file_name):
        return True
    else:
        return False
