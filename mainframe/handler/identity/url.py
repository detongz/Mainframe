# coding: utf-8

from handler.identity import auth

url=[
    (r'/login', auth.LoginPageHandler),

    ]
