import digger


def read_base(file_name):
    f = open(file_name)
    dic = {}
    for line in f:
        line = line.split('\n')[0].split('-')
        tags = line[1]
        dic[line[0][0:]] = tags
    f.close()
    return dic


def find_id(id, file_name):
    if id in read_base(file_name):
        return True
    else:
        return False


def write_db(url, file_name, soup, tag):
    f = open(file_name, 'a')
    f.write(digger.get_id(url) + '-' + tag + '\n')
    f.close()


def if_save(url):
    id = digger.get_id(url)
    f = open('base_date.txt')
    for line in f:
        if id in line:
            return True
    return False

def str_replace(old_str,new_str):
    file = open('base_date.txt', 'r')
    text = file.read()
    file.close()
    file = open('base_date.txt', 'w')
    file.write(text.replace(old_str, new_str))
    file.close()
