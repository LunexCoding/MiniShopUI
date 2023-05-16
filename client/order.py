class Order:
    def __init__(self, orderID):
        self.__orderID = orderID
        self.__products = []
        self.__cost = 0

    def addProduct(self, product):
        self.__products.append(product)
        self.__updateCost()

    def deleteProduct(self, product):
        self.__products.remove(product)
        self.__updateCost()

    def __updateCost(self):
        for product in self.__products:
            self.__cost += product.cost

    def clear(self):
        self.__products.clear()

    @property
    def orderID(self):
        return self.__orderID

    @property
    def products(self):
        return self.__products

    @property
    def cost(self):
        return self.__cost
