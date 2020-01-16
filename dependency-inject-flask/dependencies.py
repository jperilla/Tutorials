from injector import singleton
from flask_injector import request

from MyDatabase import DatabaseBase, MySqlDatabase
from MyService import MyService


def configure(binder):
    binder.bind(DatabaseBase, to=MySqlDatabase, scope=request)
    binder.bind(MyService, to=MyService, scope=request)
