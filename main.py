from pathlib import Path

from Custom_Widgets.Widgets import *

from forms.ui_interface import Ui_MainWindow
from widgets.flowLayout import FlowLayout
from widgets.elementProduct import ElementProduct
from helpers.fileSystem import fileSystem
from helpers.database import databaseSession
from helpers.sqlQueries import SqlQueries


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

    def __loadData(self):
        fileSystem.makeDir(PRODUCT_IMAGE_DIRECTORY, recreate=True)
        with databaseSession as db:
            data = db.getRows(SqlQueries.selectAllProducts())
            if data:
                for product in data:
                    print(product)
                    self.__carWidgetAdded()

    def __carWidgetAdded(self, data):
        itemProduct = ElementProduct(
            ...
        )
        self.flowProductsLayout.addWidget(itemProduct)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec_())
