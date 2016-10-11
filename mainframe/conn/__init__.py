#coding:utf-8

import pymongo
import redis

#connecting mongodb
conn = pymongo.MongoClient('localhost', 27017)

# database:
mainframe = conn.mainframe

#collections:
mainframeusers = mainframe.MainframeUsers
uploadrecord = mainframe.UploadRecord
questions = mainframe.Questions


#connecting redis
rconn = redis.Redis(
 host='localhost',
 port=6379,
)


if __name__ == '__main__':
    print(mainframeusers.find_one())
