from Custom_Widgets.Widgets import *

from admin.interface.forms.ui_interface import Ui_MainWindow
from admin.backend.dbApp.database import databaseSession
from admin.backend.dbApp.sqlQueries import SqlQueries


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles=["interface/style.json"])
        self.show()

        self.ui.findOrderBtn.clicked.connect(self.__findOrder)

    def __findOrder(self):
        orderID = self.ui.inputOrderID.text()
        if len(orderID) != 0:
            with databaseSession as db:
                data = db.getRows(
                    SqlQueries.selectOrder(orderID),
                    data={"orderID": orderID}
                )
            cost = data["cost"]
            countProducts = len(data["productIDs"].split())
            self.ui.costOrder.setText(str(cost))
            self.ui.countProducts.setText(str(countProducts))
            self.ui.mainPages.setCurrentIndex(1)



