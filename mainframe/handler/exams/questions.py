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
            self.render(
                        'exams/uploadquestions.html',
                        uploadpath = '/identity/login',
                        extfile = 'csv',
                        )
        else:
            self.write('请登录')

    def post(self):
        print(self.request.files['file'][0]['filename'])
        if not self.AuthTeacherIdentity():
            self.write('请登录')
            return

        try:
            self.SaveFile(GenerateId(),'exams')
            self.write(json.dumps({'status':'ok'}))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    print()
