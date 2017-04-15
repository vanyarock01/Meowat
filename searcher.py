import bdHandler
import os


def find_move():
    res = os.listdir(path="D:\\pictures\\")
    print(res)
    base = bdHandler.read_base('base_date.txt')
    print(base)
    for folder in res:
        content = os.listdir(path="D:\\pictures\\" + folder)
        print(content)
        for str in content:
            id = str.split(' - ')[0]
            if base[id] != folder:
                print(id + '-' + base[id])
                bdHandler.str_replace(id + '-' + base[id], id + '-' + folder)
    print (base)
find_move()

