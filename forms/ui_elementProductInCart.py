# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elementProductInCartRuSDHf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_elementProduct(object):
    def setupUi(self, elementProduct):
        if not elementProduct.objectName():
            elementProduct.setObjectName(u"elementProduct")
        elementProduct.resize(800, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementProduct.sizePolicy().hasHeightForWidth())
        elementProduct.setSizePolicy(sizePolicy)
        elementProduct.setMinimumSize(QSize(800, 250))
        elementProduct.setMaximumSize(QSize(800, 270))
        elementProduct.setStyleSheet(u"* {\n"
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
        self.verticalLayout_2 = QVBoxLayout(elementProduct)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 20, 20)
        self.groupBox = QGroupBox(elementProduct)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(800, 250))
        self.groupBox.setMaximumSize(QSize(800, 250))
        self.groupBox.setStyleSheet(u"border: none")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_3 = QFrame(self.frame_9)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(300, 200))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 10, 10)
        self.imageArea = QLabel(self.frame_3)
        self.imageArea.setObjectName(u"imageArea")
        self.imageArea.setMinimumSize(QSize(260, 200))
        self.imageArea.setMaximumSize(QSize(300, 200))

        self.verticalLayout_4.addWidget(self.imageArea)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_9)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 250))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.productName = QLabel(self.frame_4)
        self.productName.setObjectName(u"productName")
        self.productName.setMinimumSize(QSize(350, 0))
        self.productName.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.productName)

        self.productCost = QLabel(self.frame_4)
        self.productCost.setObjectName(u"productCost")

        self.horizontalLayout_6.addWidget(self.productCost)

        self.deleteProductFromCartBtn = QPushButton(self.frame_4)
        self.deleteProductFromCartBtn.setObjectName(u"deleteProductFromCartBtn")
        icon = QIcon()
        icon.addFile(u":/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteProductFromCartBtn.setIcon(icon)
        self.deleteProductFromCartBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.deleteProductFromCartBtn)


        self.horizontalLayout_5.addWidget(self.frame_4)


        self.horizontalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(elementProduct)

        QMetaObject.connectSlotsByName(elementProduct)
    # setupUi

    def retranslateUi(self, elementProduct):
        elementProduct.setWindowTitle(QCoreApplication.translate("elementProduct", u"Form", None))
        self.groupBox.setTitle("")
        self.imageArea.setText("")
        self.productName.setText(QCoreApplication.translate("elementProduct", u"TextLabel", None))
        self.productCost.setText(QCoreApplication.translate("elementProduct", u"TextLabel", None))
        self.deleteProductFromCartBtn.setText("")
    # retranslateUi

