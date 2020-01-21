
class Service():

    def getInventario(tienda):
        inventario = {}
        items = tienda.getItems()

        for item in items:
            inventario[item.name] = item.__dict__
        return inventario

    def updateQuality(tienda):
        # Para actualizar la calidad de los items y devolver el estado
        # actualizado de los mismos
        tienda.update_quality()
        return Service.getInventario(tienda)
