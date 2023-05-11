from pathlib import Path

from Custom_Widgets.Widgets import *

from client.interface.forms.ui_interface import Ui_MainWindow
from client.interface.widgets.flowLayout import FlowLayout
from client.interface.widgets.productElement import ElementProduct
from client.interface.widgets.shoppingCartElement import ShoppingCartElement
from client.backend.dbApp.database import databaseSession
from client.backend.dbApp.sqlQueries import SqlQueries


PRODUCT_IMAGE_DIRECTORY = Path("productsImage")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles=["client/interface/style.json"])
        self.show()

        self.flowProductsLayout = FlowLayout()
        self.flowProductsCartLayout = FlowLayout()
        self.ui.productsLayout.addLayout(self.flowProductsLayout)
        self.ui.productsCartLayout.addLayout(self.flowProductsCartLayout)

        self.ui.makeAnOrderBtn.clicked.connect(lambda: self.__makeOrden())

        self.__loadData()

    def __loadData(self):
        with databaseSession as db:
            data = db.getRows(SqlQueries.selectAllProducts())
            if data:
                for product in data:
                    self.__productWidgetAdded(product)

    def __productWidgetAdded(self, product):
        productItem = ElementProduct(
            productID=product["id"],
            name=product["name"],
            description=product["description"],
            cost=product["cost"],
            image=product["image"]
        )
        self.flowProductsLayout.addWidget(productItem)
        productItem._addToCart.connect(self.__addProductToCart)

    def __addProductToCart(self, productID, name, cost, image):
        cartItem = ShoppingCartElement(
            productID=productID,
            name=name,
            cost=cost,
            image=image
        )
        self.flowProductsCartLayout.addWidget(cartItem)
        cartItem._delete.connect(self.__deleteProductFromCart)

    def __deleteProductFromCart(self, productID):
        widget = self.sender()
        self.flowProductsCartLayout.removeWidget(widget)
        widget.deleteLater()


