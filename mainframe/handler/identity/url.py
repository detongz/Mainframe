# coding: utf-8

from handler.identity import auth

url=[
    (r'/identity/login', auth.LoginPageHandler),
    (r'/identity/logout', auth.LogoutHandler),
    ]
