def write_base(file_id, file_name):
    f = open(file_name, 'a')
    f.write(file_id + ' ')
    f.close()


def read_base(file_name):
    f = open(file_name)
    res = f.read().split()
    f.close()
    return res


def find_id(file_id, file_name):
    if file_id in read_base(file_name):
        return True
    else:
        return False
