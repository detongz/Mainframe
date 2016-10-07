# coding: utf-8
"""
Processing uploaded Question CSV file.
"""

import csv

from conn import questions
from oslo import question


def ReadCsv(path):
    # uploadrecord.insert()
    with open(path, newline='') as quiz:
        reader = csv.reader(quiz)
        number = 0
        for r in reader:
            tmp = r[0:3]
            tmp.insert(0,number)
            tmp.append(str([x for x in r[3:] if x]))
            tmp.append(question.GenerateId())
            print(tmp)
            query = "{'number' : '%s', 'type' : '%s', \
                    'question' : '%s', 'answer' :'%s', \
                    'options' : '%s', 'createtime' : new Date(),\
                    'id': '%s'\
                    }"\
                    % tuple(tmp)
            questions.insert(query)
            number += 1
    return


if __name__ == '__main__':
    f='/run/media/zdt/workspace/workspace/Mainframe/files/question-example.csv'
    ReadCsv(f)
