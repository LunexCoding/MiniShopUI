from PySide2 import QtGui
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal, QSize

from forms.ui_elementProduct import Ui_elementProduct


class ElementProduct(QWidget):
    def __init__(self, name, description, cost, image, parent=None):
        super(ElementProduct, self).__init__(parent)
        self.ui = Ui_elementProduct()
        self.ui.setupUi(self)

        self._name = name
        self._description = description
        self._cost = cost
        self._image = image


        self.ui.productName.setText(self._name)
        self.ui.productDescription.setText(self._description)
        self.ui.productCost.setText(self._cost)

        size = self.ui.imageArea.size()
        img = QtGui.QImage(self._image)
        pixmap = QtGui.QPixmap(img.scaled(size))
        self.ui.imageArea.setPixmap(pixmap)
