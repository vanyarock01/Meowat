import digger
import configparser

config = configparser.RawConfigParser()
config.read('Regulations.ini')
base = config.get('base', 'base_name')

def read_base(file_name):

    """ Read base data as dict and return him """

    f = open(file_name)
    dic = {}
    for line in f:
        line = line.split('\n')[0].split('-')
        tags = line[1]
        dic[line[0][0:]] = tags
    f.close()
    return dic


def write_db(url, tag):

    """ Write id-tag to the database"""

    f = open(base, 'a')
    f.write(digger.get_id(url) + '-' + tag + '\n')
    f.close()


def if_save(url):

    """Check file id in database"""

    id = digger.get_id(url)
    f = open(base)
    for line in f:
        if id in line:
            return True
    return False


def str_replace(old_str,new_str):

    """Search string by pattern and replase on new string"""

    file = open(base, 'r')
    text = file.read()
    file.close()
    file = open(base, 'w')
    file.write(text.replace(old_str, new_str))
    file.close()
