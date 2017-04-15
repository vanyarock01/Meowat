import configparser
import bdHandler
import os

config = configparser.RawConfigParser()
config.read('Regulations.ini')

def find_move():
    print('Start search moving')
    path = config.get('base', 'path')
    res = os.listdir(path)
    print(res)
    base = bdHandler.read_base('base_date.txt')
    print(base)
    for folder in res:
        content = os.listdir(path=path + folder)
        for str in content:
            id = str.split(' - ')[0]
            if base[id] != folder:
                bdHandler.str_replace(id + '-' + base[id], id + '-' + folder)
    print ('Search moving sccessfully completed')

#def getInfo():

