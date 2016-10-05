#coding: utf-8

import sys

from conn import mainframeusers
from oslo import encrypt
from handler import BaseHandler


class LoginPageHandler(BaseHandler):
    def get(self):
        """Render login page."""
        if self.get_cookie('UnameTeacherMainframe'):
            self.write("already loged in")
            return
        self.render('identity/login.html')

    def post(self):
        query='{"pwd" : "%s", "id" : "%s"}' % (encrypt.md5(self.get_argument('p')), self.get_argument('i'))
        user = mainframeusers.find_one()

        if not user:
            self.write("0")
            return

        self.set_cookie("UnameTeacherMainframe", user['name'])
        self.write("1")
