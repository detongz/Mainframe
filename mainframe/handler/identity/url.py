# coding: utf-8

from handler.identity import auth

url=[
    (r'/auth/login', auth.LoginPageHandler),
    (r'/auth/logout', auth.LogoutHandler),
    ]
