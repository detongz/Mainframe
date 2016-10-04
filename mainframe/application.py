#coding:utf-8

import os
import tornado.web

from handler.identity import url as IdentityUrl

url=[]
url.extend(IdentityUrl.url)

setting = dict(
    template_path=os.path.join(os.path.dirname(__file__),"templates"),
    static_path=os.path.join(os.path.dirname(__file__),"static"),
    debug=True,
    )

application = tornado.web.Application(
    handlers=url,
    **setting
    )
