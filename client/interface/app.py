from pathlib import Path

from Custom_Widgets.Widgets import *

from client.interface.forms.ui_interface import Ui_MainWindow
from client.interface.widgets.flowLayout import FlowLayout
from client.interface.widgets.productElement import ElementProduct
from client.interface.widgets.shoppingCartElement import ShoppingCartElement
from client.backend.dbApp.database import databaseSession
from client.backend.dbApp.sqlQueries import SqlQueries
from client.backend.helpers.IDGenerator import g_IDGenerator
from client.backend.helpers.emailSender import g_emailSender
from client.product import Product
from client.order import Order


PRODUCT_IMAGE_DIRECTORY = Path("productsImage")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles=["interface/style.json"])
        self.show()

        self.__order = Order(g_IDGenerator.getOrderID())

        self.flowProductsLayout = FlowLayout()
        self.flowProductsCartLayout = FlowLayout()
        self.ui.productsLayout.addLayout(self.flowProductsLayout)
        self.ui.productsCartLayout.addLayout(self.flowProductsCartLayout)

        self.ui.makeAnOrderBtn.clicked.connect(self.__makeOrder)

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
        product = Product(
            productID=productID,
            name=name,
            cost=cost
        )
        self.__order.addProduct(product)
        self.__updateOrderForm()

    def __deleteProductFromCart(self, productID):
        widget = self.sender()
        self.flowProductsCartLayout.removeWidget(widget)
        widget.deleteLater()

    def __updateOrderForm(self):
        self.ui.countProductsInCart.setText(str(len(self.__order.products)))
        self.ui.cost.setText(str(self.__order.cost))

    def __makeOrder(self):
        if len(self.__order.products) > 0:
            productIDs = []
            for product in self.__order.products:
                productIDs.append(str(product.productID))
            with databaseSession as db:
                db.execute(
                    SqlQueries.insertOrder(
                        self.__order.orderID,
                        self.__order.cost,
                        " ".join(productIDs)
                    ),
                    data={
                        "orderID": self.__order.orderID,
                        "cost": self.__order.cost,
                        "productIDs": " ".join(productIDs)
                    }
                )
            email = self.ui.inputEmail.text()
            self.__sendEmail(email)

    def __sendEmail(self, email):
        if len(email) != 0:
            if g_emailSender.validateEmail(email):
                g_emailSender.sendEmail(email, "Заказ в LunexShop", message=f"""
Вы оформили заказ в LunexShop:
Кол-во товаров: {self.ui.countProductsInCart.text()}
Общая стоимость заказа: {self.ui.cost.text()}
Пункт выдачи: {self.ui.address.text()}
Для получения заказа в пункте выдачи предъявите код вашего заказа: {self.__order.orderID}
""")
