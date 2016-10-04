# coding: utf-8

import conn
from conn.mongo import mainframeusers
from handler import BaseHandler
from oslo import encrypt

class LoginPageHandler(BaseHandler):
    def get(self):
        """Render the login page."""
        if self.get_cookie('UnameTeacherMainframe'):
            self.write("already loged in")
            return
        self.render('identity/login.html')

    def post(self):
        query='{"pwd" : "%s", "id" : "%s"}' % (encrypt.md5(self.get_argument('p')), self.get_argument('i'))
        user = mainframeusers.find_one(query)

        print user
        if not user:
            self.write("0")
            return

        self.set_cookie("UnameTeacherMainframe", user.name)
        self.write("1")

if __name__ == '__main__':
    print  mainframeusers.find_one()
