from PySide2 import QtGui
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget

from client.interface.forms.ui_productElement import Ui_productElement


class ElementProduct(QWidget):
    _addToCart = Signal(int, str, float, bytes)

    def __init__(self, productID, name, description, cost, image, parent=None):
        super(ElementProduct, self).__init__(parent)
        self.ui = Ui_productElement()
        self.ui.setupUi(self)

        self._productID = productID
        self._name = name
        self._description = description
        self._cost = cost
        self._image = image

        self.ui.productName.setText(self._name)
        self.ui.productDescription.setText(self._description)
        self.ui.productCost.setText(str(self._cost))

        size = self.ui.imageArea.size()
        img = QtGui.QImage()
        img.loadFromData(self._image)
        pixmap = QtGui.QPixmap.fromImage(img.scaled(size))
        self.ui.imageArea.setPixmap(pixmap)

        self.ui.addToCartBtn.clicked.connect(self.addToCart)

    def addToCart(self):
        self._addToCart.emit(self._productID, self._name, self._cost, self._image)
