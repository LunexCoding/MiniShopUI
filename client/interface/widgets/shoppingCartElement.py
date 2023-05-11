from PySide2 import QtGui
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget

from client.interface.forms.ui_shoppingCartElement import Ui_shoppingCartElement


class ShoppingCartElement(QWidget):
    _delete = Signal(str)

    def __init__(self, productID, name, cost, image, parent=None):
        super(ShoppingCartElement, self).__init__(parent)
        self.ui = Ui_shoppingCartElement()
        self.ui.setupUi(self)

        self._productID = productID
        self._name = name
        self._cost = cost
        self._image = image

        self.ui.productName.setText(self._name)
        self.ui.productCost.setText(str(self._cost))

        size = self.ui.imageArea.size()
        img = QtGui.QImage()
        img.loadFromData(self._image)
        pixmap = QtGui.QPixmap.fromImage(img.scaled(size))
        self.ui.imageArea.setPixmap(pixmap)

    def delete(self):
        self._addToCart.emit(self._productID)