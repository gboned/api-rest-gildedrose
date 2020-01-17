
class Root():
    def __init__(self, as_view):
        self.as_view = {}
    def saludo(self):
        self.as_view['welcome!'] = 'Ollivanders'
        return self.as_view
x = Root('a').saludo()
print(x)
