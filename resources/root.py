from flask_restful import Resource, Api
from config import tienda
from services.service import Service

class Root(Resource):
    def __init__(self, as_view):
        self.as_view = {}
    def saludo(self):
        self.as_view['welcome!'] = 'Ollivanders'
        return self.as_view
x = Root('a').saludo()
print(x)
