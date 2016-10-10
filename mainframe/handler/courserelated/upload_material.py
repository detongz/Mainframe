# coding: utf-8

from handler import BaseHandler

class UploadCourseMaterial(BaseHandler):
    def get(self):
        if not self.AuthTeacherIdentity():
            self.write("请登录")
            return

        self.render('courserelated/uploadmaterial.html')


    def post(self):
        pass
