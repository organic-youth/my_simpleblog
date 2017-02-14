import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# pagination
POSTS_PER_PAGE = 3

OPENID_PROVIDERS = [
    {'name' : 'Google' , 'url': 'https://www.google.com/accounts/o8/id'},
    {'name' : 'Yahoo' , 'url' : 'https://me.yahoo.com'},
    {'name' : 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name' : 'Flicker' , 'url' : 'http://www.flicker..com/<username>'},
    {'name' : 'MyOpenID' , 'url' : 'http://www.myopenid.com'}
]

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

ADMINS = ['1694405718@qq.com']

