# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceYCppyS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomStackedWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 741)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"* {\n"
"	border: None;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget {\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#headerContainer, #footerContainer {\n"
"	background-color: #2c313c;\n"
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
"	background-color: #16191d;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"#inputSpecifications {\n"
"	border-top-left-radius: 0;\n"
"	border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"#specificationsOptions {\n"
"	border-top-right-radius: 0;\n"
"	border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:verti"
                        "cal {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: #262a30;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: #262a30;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	bord"
                        "er: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color:#262a30;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR */\n"
" QScrollBar:horizontal {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    height: 14px;\n"
"    margin: 0 15px 0 15px;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:horizontal {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-width: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:hori"
                        "zontal:hover{	\n"
"	background-color: #262a30;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	width: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-top-left-radius: 7px;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {	\n"
"	background-color: #262a30;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	width: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-top-left-radius: 7px;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {	\n"
"	background-color:#262a30;\n"
"}\n"
"\n"
"QScrollBar::add-line:hor"
                        "izontal:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setAutoFillBackground(False)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(30, 25))
        self.label_5.setPixmap(QPixmap(u":/images/warehouse.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon = QIcon()
        icon.addFile(u":/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy1)
        self.mainBodyContent.setMinimumSize(QSize(850, 650))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, -1, 10, -1)
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.pageProducts = QWidget()
        self.pageProducts.setObjectName(u"pageProducts")
        self.verticalLayout_18 = QVBoxLayout(self.pageProducts)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_9 = QFrame(self.pageProducts)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"margin-left: 180%;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_7, 0, Qt.AlignRight)


        self.horizontalLayout_9.addWidget(self.frame_11, 0, Qt.AlignRight)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.openCartBtn = QPushButton(self.frame_10)
        self.openCartBtn.setObjectName(u"openCartBtn")
        self.openCartBtn.setMaximumSize(QSize(25, 16777215))
        self.openCartBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openCartBtn.setIcon(icon3)
        self.openCartBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.openCartBtn)


        self.horizontalLayout_9.addWidget(self.frame_10, 0, Qt.AlignRight)


        self.verticalLayout_18.addWidget(self.frame_9)

        self.scrollArea = QScrollArea(self.pageProducts)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: rgb(56, 56, 85);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: rgb(56, 56, 85);\n"
"}\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaProducts = QWidget()
        self.scrollAreaProducts.setObjectName(u"scrollAreaProducts")
        self.scrollAreaProducts.setGeometry(QRect(0, 0, 794, 596))
        self.horizontalLayout_13 = QHBoxLayout(self.scrollAreaProducts)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.productsLayout = QVBoxLayout()
        self.productsLayout.setSpacing(0)
        self.productsLayout.setObjectName(u"productsLayout")
        self.productsLayout.setContentsMargins(0, -1, -1, -1)

        self.horizontalLayout_13.addLayout(self.productsLayout)

        self.scrollArea.setWidget(self.scrollAreaProducts)

        self.verticalLayout_18.addWidget(self.scrollArea)

        self.mainPages.addWidget(self.pageProducts)
        self.pageCart = QWidget()
        self.pageCart.setObjectName(u"pageCart")
        self.verticalLayout = QVBoxLayout(self.pageCart)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_12 = QFrame(self.pageCart)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.toProductPageBtn = QPushButton(self.frame_14)
        self.toProductPageBtn.setObjectName(u"toProductPageBtn")
        self.toProductPageBtn.setMaximumSize(QSize(25, 16777215))
        self.toProductPageBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toProductPageBtn.setIcon(icon4)
        self.toProductPageBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.toProductPageBtn)


        self.horizontalLayout_11.addWidget(self.frame_14, 0, Qt.AlignLeft)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"margin-right: 180%;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.label_8)


        self.horizontalLayout_11.addWidget(self.frame_13, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_12)

        self.frame_3 = QFrame(self.pageCart)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scrollArea_2 = QScrollArea(self.frame_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaProductsInCart = QWidget()
        self.scrollAreaProductsInCart.setObjectName(u"scrollAreaProductsInCart")
        self.scrollAreaProductsInCart.setGeometry(QRect(0, 0, 470, 578))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaProductsInCart)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.productsCartLayout = QVBoxLayout()
        self.productsCartLayout.setObjectName(u"productsCartLayout")

        self.horizontalLayout_2.addLayout(self.productsCartLayout)

        self.scrollArea_2.setWidget(self.scrollAreaProductsInCart)

        self.horizontalLayout_3.addWidget(self.scrollArea_2)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(300, 400))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_16)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_15.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.countProductsInCart = QLabel(self.frame_16)
        self.countProductsInCart.setObjectName(u"countProductsInCart")

        self.horizontalLayout_15.addWidget(self.countProductsInCart)


        self.verticalLayout_4.addWidget(self.frame_16, 0, Qt.AlignLeft)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 9, 0, 0)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.cost = QLabel(self.frame_8)
        self.cost.setObjectName(u"cost")

        self.horizontalLayout_6.addWidget(self.cost, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.frame_8, 0, Qt.AlignLeft)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_14.addWidget(self.label_4)

        self.address = QLabel(self.frame)
        self.address.setObjectName(u"address")

        self.horizontalLayout_14.addWidget(self.address)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_15)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)

        self.inputEmail = QLineEdit(self.frame_15)
        self.inputEmail.setObjectName(u"inputEmail")

        self.verticalLayout_2.addWidget(self.inputEmail)


        self.verticalLayout_4.addWidget(self.frame_15)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#makeAnOrderBtn {\n"
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
"  -webki"
                        "t-user-select: none;\n"
"  touch-action: manipulation;\n"
"}\n"
"\n"
"#makeAnOrderBtn:hover {\n"
"  box-shadow: rgba(0, 1, 0, .2) 0 2px 8px;\n"
"  opacity: .85;\n"
"}\n"
"\n"
"#makeAnOrderBtn:active {\n"
"  outline: 0;\n"
"}\n"
"\n"
"#makeAnOrderBtn:focus {\n"
"  box-shadow: rgba(0, 0, 0, .5) 0 0 0 3px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.makeAnOrderBtn = QPushButton(self.frame_2)
        self.makeAnOrderBtn.setObjectName(u"makeAnOrderBtn")
        font3 = QFont()
        font3.setFamily(u"expo-brand-demi")
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setWeight(75)
        font3.setStrikeOut(False)
        self.makeAnOrderBtn.setFont(font3)

        self.verticalLayout_3.addWidget(self.makeAnOrderBtn)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.horizontalLayout_3.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_3)

        self.mainPages.addWidget(self.pageCart)

        self.verticalLayout_15.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)


        self.verticalLayout_10.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.headerContainer.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"LunexShop", None))
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u044b", None))
        self.openCartBtn.setText("")
        self.toProductPageBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0437\u0438\u043d\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u043e\u0432\u0430\u0440\u043e\u0432:", None))
        self.countProductsInCart.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a \u043e\u043f\u043b\u0430\u0442\u0435:", None))
        self.cost.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441:", None))
        self.address.setText(QCoreApplication.translate("MainWindow", u"255 Maine Street Brunswick ME 04011 USA", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.makeAnOrderBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0444\u043e\u0440\u043c\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
    # retranslateUi

