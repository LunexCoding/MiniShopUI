class Product:
    def __init__(self, productID, name, cost):
        self.__productID = productID
        self.__name = name
        self.__cost = float(cost)

    @property
    def productID(self):
        return self.__productID

    @property
    def name(self):
        return self.__name

    @property
    def cost(self):
        return self.__cost
