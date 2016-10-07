#coding: utf-8

"""
Defining some commonly used words concerning the questions uploaded.
"""

QuestionType = {
    0 : '单选',
    1 : '多选',
    2 : '判断',
    3 : '简答',
    4 : '填空'
}

def GenerateId():
    import random
    import datetime

    return str(datetime.datetime.now().microsecond)+str(random.randint(99,1000))

if __name__ == '__main__':
    GenerateId()
