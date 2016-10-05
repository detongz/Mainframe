# coding: utf-8

import hashlib


def md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()


if __name__ == '__main__':
    print(md5("hehehehehe"))
