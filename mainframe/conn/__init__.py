#coding:utf-8

import pymongo

#connecting mongodb
conn = pymongo.MongoClient('localhost', 27017)

# database:
mainframe = conn.mainframe

#collections:
mainframeusers = mainframe.MainframeUsers
uploadrecord = mainframe.UploadRecord
questions = mainframe.Questions


if __name__ == '__main__':
    print(mainframeusers.find_one())
