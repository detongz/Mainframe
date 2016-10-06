#coding:utf-8

import os
import tornado.web

from handler.identity import url as IdentityUrl
from handler.exams import url as ExamsUrl

url=[]
url.extend(IdentityUrl.url)
url.extend(ExamsUrl.url)

setting = dict(
    template_path=os.path.join(os.path.dirname(__file__),"templates"),
    static_path=os.path.join(os.path.dirname(__file__),"static"),
    debug=True,
    )

application = tornado.web.Application(
    handlers=url,
    **setting
    )
