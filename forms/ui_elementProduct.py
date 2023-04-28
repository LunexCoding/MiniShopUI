# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elementProductHyqDkq.ui'
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
        elementProduct.resize(470, 520)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementProduct.sizePolicy().hasHeightForWidth())
        elementProduct.setSizePolicy(sizePolicy)
        elementProduct.setMinimumSize(QSize(450, 500))
        elementProduct.setMaximumSize(QSize(470, 520))
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
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(450, 500))
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
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(450, 500))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.imageArea = QLabel(self.frame_3)
        self.imageArea.setObjectName(u"imageArea")
        self.imageArea.setMinimumSize(QSize(450, 300))
        self.imageArea.setMaximumSize(QSize(450, 300))

        self.verticalLayout_4.addWidget(self.imageArea)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 250))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, -1, -1, -1)
        self.productName = QLabel(self.frame_4)
        self.productName.setObjectName(u"productName")

        self.verticalLayout_5.addWidget(self.productName)

        self.productDescription = QLabel(self.frame_4)
        self.productDescription.setObjectName(u"productDescription")

        self.verticalLayout_5.addWidget(self.productDescription)

        self.productCost = QLabel(self.frame_4)
        self.productCost.setObjectName(u"productCost")

        self.verticalLayout_5.addWidget(self.productCost)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"/* CSS */\n"
"#addToCartBtn {\n"
"  align-items: center;\n"
"  background-color: initial;\n"
"  background-image: linear-gradient(#464d55, #25292e);\n"
"  border-radius: 8px;\n"
"  border-width: 0;\n"
"  box-shadow: 0 10px 20px rgba(0, 0, 0, .1),0 3px 6px rgba(0, 0, 0, .05);\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  display: inline-flex;\n"
"  flex-direction: column;\n"
"  font-family: expo-brand-demi,system-ui,-apple-system,BlinkMacSystemFont,\"Segoe UI\",Roboto,\"Helvetica Neue\",Arial,\"Noto Sans\",sans-serif,\"Apple Color Emoji\",\"Segoe UI Emoji\",\"Segoe UI Symbol\",\"Noto Color Emoji\";\n"
"  font-size: 18px;\n"
"  height: 52px;\n"
"  justify-content: center;\n"
"  line-height: 1;\n"
"  margin: 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  transform: translate3d(0, 0, 0);\n"
"  transition: all 150ms;\n"
"  vertical-align: baseline;\n"
"  white-space: nowrap;\n"
"  user-select: none;\n"
""
                        "  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"}\n"
"\n"
"#addToCartBtn:hover {\n"
"  box-shadow: rgba(0, 1, 0, .2) 0 2px 8px;\n"
"  opacity: .85;\n"
"}\n"
"\n"
"#addToCartBtn:active {\n"
"  outline: 0;\n"
"}\n"
"\n"
"#addToCartBtn:focus {\n"
"  box-shadow: rgba(0, 0, 0, .5) 0 0 0 3px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addToCartBtn = QPushButton(self.frame_7)
        self.addToCartBtn.setObjectName(u"addToCartBtn")
        font = QFont()
        font.setFamily(u"expo-brand-demi")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.addToCartBtn.setFont(font)
        self.addToCartBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addToCartBtn.setStyleSheet(u"")
        self.addToCartBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.addToCartBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame)


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
        self.productDescription.setText(QCoreApplication.translate("elementProduct", u"TextLabel", None))
        self.productCost.setText(QCoreApplication.translate("elementProduct", u"TextLabel", None))
        self.addToCartBtn.setText(QCoreApplication.translate("elementProduct", u"\u0412 \u043a\u043e\u0440\u0437\u0438\u043d\u0443", None))
    # retranslateUi

