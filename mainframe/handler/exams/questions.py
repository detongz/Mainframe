# coding: utf-8

import os
import json

from conn import questions
from conn import uploadrecord
from handler import BaseHandler
from oslo.question import GenerateId


class UploadQuestions(BaseHandler):
    def get(self):
        print(self.get_cookie('UnameTeacherMainfram'))
        if self.AuthTeacherIdentity():
            self.render('exams/uploadquestions.html')
        else:
            self.write('请登录')

    def post(self):
        import pdb; pdb.set_trace()
        if not self.AuthTeacherIdentity():
            self.write('请登录')
            return

        try:
            self.SaveFile(GenerateId(),'examfiles')
            self.write(json.dumps({'status':'ok'}))
        except Exception as e:
            # print(e)
            self.write(json.dumps({'status':'fail'}))


if __name__ == '__main__':
    print()
