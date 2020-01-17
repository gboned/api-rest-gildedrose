from flask import Flask
from flask_restful import Resource, Api

from resources.inventario import Inventario
from config import *
from resources.root import Root

app = Flask(__name__)
api = Api(app)

api.add_resource(Root, '/')
api.add_resource(Inventario, '/inventario')
# api.add_resource(UpdateQuality, '/updateQuality')


if __name__ == '__main__':
    app.run(debug=True)
