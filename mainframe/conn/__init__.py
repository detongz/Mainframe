#coding:utf-8

import pymongo

#connect with mongodb
conn = pymongo.MongoClient('localhost', 27017)

mainframe = conn.mainframe

mainframeusers = mainframe.MainframeUsers


if __name__ == '__main__':
    print mainframeusers.find_one()
