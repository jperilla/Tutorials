from flask import Flask
from flask_injector import FlaskInjector
from injector import inject

from MyService import MyService
from dependencies import configure

app = Flask(__name__)


@inject
@app.route('/data')
def get_data(service: MyService):
    print(f"MyService instance is {service}")  # We want to see the object that gets created
    return service.get_data()


# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])
