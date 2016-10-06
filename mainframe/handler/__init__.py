#!/usr/bin/env python
#coding:utf-8

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def AuthTeacherIdentity(self):
        """教师登录验证"""
        if self.get_cookie('UnameTeacherMainframe'):
            return 1
        return 0
