# coding: utf-8

from conn import rconn
from handler import BaseHandler
from oslo.question import GenerateId

class UploadCourseMaterial(BaseHandler):
    def get(self):
        if not self.AuthTeacherIdentity():
            self.write("请登录")
            return

        # self.clear_cookie('materialId')
        #
        # materialId = 'material' + str(GenerateId())
        # for rconn.get(materialId):
        #     materialId = 'material' + str(GenerateId())
        #
        # self.set_cookie('materialId',materialId)
        # rconn.set(materialId,[])

        self.render(
                    'courserelated/uploadmaterial.html',
                    uploadpath = '/relate/uploadmaterial',
                    extfile = '*'
        )


    def post(self):
        pass

class UploadCourseMaterialAttachment(BaseHandler):
    def post(self):
        pass
