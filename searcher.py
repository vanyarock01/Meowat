import os


def __search__():
    res = os.listdir(path="D:\\pictures\\")
    for folder in res:
        print(os.listdir(path="D:\\pictures\\" + folder))


__search__()