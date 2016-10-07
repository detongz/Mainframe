#coding:utf-8

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def AuthTeacherIdentity(self):
        """Authenticate teacher's cookie."""
        if self.get_cookie('UnameTeacherMainframe'):
            return 1
        return 0

    def SaveFile(self,name,reqname):
        """
        Save files when needed.
        param name string: File name without parameter.

        return a list of successfully stored files.
        """
        import os

        fpath = os.path.join(os.path.dirname(__file__)[:-13],'static/userfile')

        # request file id : 'csv'
        files = self.request.files[reqname]

        l,i = [], 0
        try:
            for f in files:
                filename = name + str(i) + '.' + f['filename'].split('.')[-1]
                filedir = os.join(fpath,filename)
                with open(filedir,'r') as fi:
                    fi.write(f['body'])
                print(filename)
                i += 1
                l.append(filename)
        except Exception as e:
            print(e)
            print(files)
        finally:
            return filename
