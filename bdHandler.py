import digger


def read_base(file_name):
    f = open(file_name)
    dic = {}
    for line in f:
        line = line.split('\n')[0].split('-')
        tags = line[1].split(',')
        dic[line[0][0:-1]] = tags
    f.close()
    return dic


def find_id(id, file_name):
    if id in read_base(file_name):
        return True
    else:
        return False


def write_db(url, file_name, soup):
    f = open(file_name, 'a')
    f.write(digger.post_linker(url, soup) + '\n')
    f.close()


