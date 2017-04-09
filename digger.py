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
