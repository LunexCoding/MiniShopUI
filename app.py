from pathlib import Path

from Custom_Widgets.Widgets import *

from forms.ui_interface import Ui_MainWindow
from widgets.flowLayout import FlowLayout
from widgets.elementProduct import ElementProduct
from dbApp.database import databaseSession
from dbApp.sqlQueries import SqlQueries


PRODUCT_IMAGE_DIRECTORY = Path("productsImage")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show()

        self.flowProductsLayout = FlowLayout()
        self.ui.productsLayout.addLayout(self.flowProductsLayout)

        self.ui.makeAnOrderBtn.clicked.connect(lambda: self.__makeOrden())

        # self.__loadData()

    def __loadData(self):
        with databaseSession as db:
            data = db.getRows(SqlQueries.selectAllProducts())
            if data:
                for product in data:
                    print(product)

    def __carWidgetAdded(self, data):
        itemProduct = ElementProduct(
            ...
        )
        self.flowProductsLayout.addWidget(itemProduct)
