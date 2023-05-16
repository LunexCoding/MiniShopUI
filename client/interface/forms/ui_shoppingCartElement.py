# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShoppingCartElementqLXMAu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_shoppingCartElement(object):
    def setupUi(self, shoppingCartElement):
        if not shoppingCartElement.objectName():
            shoppingCartElement.setObjectName(u"shoppingCartElement")
        shoppingCartElement.resize(350, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(shoppingCartElement.sizePolicy().hasHeightForWidth())
        shoppingCartElement.setSizePolicy(sizePolicy)
        shoppingCartElement.setMinimumSize(QSize(350, 300))
        shoppingCartElement.setMaximumSize(QSize(370, 320))
        shoppingCartElement.setStyleSheet(u"* {\n"
"	color: #fff;\n"
"	background-color: #2a2f38;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #16191d;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"	font-size: 10px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(shoppingCartElement)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 20, 20)
        self.groupBox = QGroupBox(shoppingCartElement)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(350, 300))
        self.groupBox.setMaximumSize(QSize(350, 300))
        self.groupBox.setStyleSheet(u"border: none")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(300, 400))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.imageArea = QLabel(self.frame_3)
        self.imageArea.setObjectName(u"imageArea")
        self.imageArea.setMinimumSize(QSize(300, 200))
        self.imageArea.setMaximumSize(QSize(300, 300))

        self.verticalLayout_4.addWidget(self.imageArea)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(200, 250))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 0, 0)
        self.productName = QLabel(self.frame_4)
        self.productName.setObjectName(u"productName")
        self.productName.setMinimumSize(QSize(150, 0))
        self.productName.setAlignment(Qt.AlignCenter)
        self.productName.setWordWrap(True)

        self.verticalLayout.addWidget(self.productName)

        self.productCost = QLabel(self.frame_4)
        self.productCost.setObjectName(u"productCost")
        self.productCost.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.productCost)

        self.deleteProductFromCartBtn = QPushButton(self.frame_4)
        self.deleteProductFromCartBtn.setObjectName(u"deleteProductFromCartBtn")
        icon = QIcon()
        icon.addFile(u":/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteProductFromCartBtn.setIcon(icon)
        self.deleteProductFromCartBtn.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.deleteProductFromCartBtn)


        self.verticalLayout_4.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(shoppingCartElement)

        QMetaObject.connectSlotsByName(shoppingCartElement)
    # setupUi

    def retranslateUi(self, shoppingCartElement):
        shoppingCartElement.setWindowTitle(QCoreApplication.translate("shoppingCartElement", u"Form", None))
        self.groupBox.setTitle("")
        self.imageArea.setText("")
        self.productName.setText(QCoreApplication.translate("shoppingCartElement", u"TextLabel", None))
        self.productCost.setText(QCoreApplication.translate("shoppingCartElement", u"TextLabel", None))
        self.deleteProductFromCartBtn.setText("")
    # retranslateUi

