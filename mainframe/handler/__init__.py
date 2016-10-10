#coding:utf-8

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def AuthTeacherIdentity(self):
        """Authenticate teacher's cookie."""
        if self.get_cookie('UnameTeacherMainframe'):
            return 1
        return 0

    def SaveFile(self,name,fp):
        """
        Save files when needed.
        param name string: File name without parameter.

        return stored filename.
        """
        import os

        fpath = os.path.join(os.path.dirname(__file__)[:-8],'static/userfile',fp)

        f = self.request.files['file'][0]

        try:
            filename = name + '.' + f['filename'].split('.')[-1]
            filedir = os.path.join(fpath,filename)
            with open(filedir,'wb') as fi:
                fi.write(f['body'])
            print(filename)
        except Exception as e:
            print(e)
        finally:
            return filename
