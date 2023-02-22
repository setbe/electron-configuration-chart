from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QDockWidget, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(980, 340)
        MainWindow.setMinimumSize(QSize(650, 200))
        MainWindow.setStyleSheet(u"background: #FBF8F1;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.table = QLabel(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"background: #F6F0E8;\n"
"border-radius: 12px;")
        self.table.setText(u"")

        self.horizontalLayout_4.addWidget(self.table)

        MainWindow.setCentralWidget(self.centralwidget)
        self.dock_widget = QDockWidget(MainWindow)
        self.dock_widget.setObjectName(u"dock_widget")
        self.dock_widget.setMinimumSize(QSize(170, 102))
        self.dock_widget.setMaximumSize(QSize(524287, 150))
        font = QFont()
        font.setPointSize(8)
        self.dock_widget.setFont(font)
        self.dock_widget.setAutoFillBackground(False)
        self.dock_widget.setStyleSheet(u"QDockWidget {\n"
"	background: white;\n"
"	color: #632626;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QDockWidget:title {\n"
"	background : #F7ECDE;\n"
"	border-radius: 12px;\n"
"	padding-left: 5px\n"
"}\n"
"\n"
"QFrame {\n"
"	background: #F6F0E8;\n"
"	border-radius: 12px;\n"
"}")
        self.dock_widget.setFloating(False)
        self.dock_widget.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        #self.dock_widget.setAllowedAreas(Qt.BottomDockWidgetArea|Qt.TopDockWidgetArea)
        self.dock_widget.setWindowTitle(u"")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.horizontalLayout_3 = QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.dockWidgetContents_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(600, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.ok_btn = QPushButton(self.frame)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setGeometry(QRect(303, 14, 71, 34))
        font1 = QFont()
        font1.setPointSize(11)
        self.ok_btn.setFont(font1)
        self.ok_btn.setToolTipDuration(4)
        self.ok_btn.setStyleSheet(u"QPushButton {\n"
"	background :#976464;\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"	color: #FBF8F1;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: #745C5C;\n"
"	border-radius: 12px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #E9DAC1;\n"
"	color: white;\n"
"}")
        self.ok_btn.setText(u"   \u041e\u041a")
        self.ok_btn.setFlat(False)
        self.entry_line = QLineEdit(self.frame)
        self.entry_line.setObjectName(u"entry_line")
        self.entry_line.setGeometry(QRect(23, 22, 300, 34))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.entry_line.setFont(font2)
        self.entry_line.setStyleSheet(u"QLineEdit {\n"
"background: #E9DAC1;\n"
"border: 1px solid #E9DAC1;\n"
"border-radius: 12px;\n"
"color: #632626;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"}\n")
        self.entry_line.setInputMask(u"")
        self.entry_line.setText(u"")
        self.entry_line.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.entry_line.setPlaceholderText(u"\u0424\u043e\u0440\u043c\u0443\u043b\u0430")

        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_3 = QFrame(self.dockWidgetContents_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(200, 16777215))
        self.frame_3.setStyleSheet(u"QSpinBox {\n"
"	border: 0px;\n"
"	background: #E9DAC1;\n"
"	color: #632626;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.thickness_spinbox = QSpinBox(self.frame_3)
        self.thickness_spinbox.setObjectName(u"thickness_spinbox")
        self.thickness_spinbox.setGeometry(QRect(124, 20, 42, 22))
        self.thickness_spinbox.setAlignment(Qt.AlignCenter)
        self.thickness_spinbox.setSpecialValueText(u"")
        self.thickness_spinbox.setSuffix(u"")
        self.thickness_spinbox.setPrefix(u"")
        self.thickness_spinbox.setMinimum(1)
        self.thickness_spinbox.setMaximum(4)
        self.thickness_spinbox.setValue(2)
        self.label_thickness = QLabel(self.frame_3)
        self.label_thickness.setObjectName(u"label_thickness")
        self.label_thickness.setGeometry(QRect(114, 46, 61, 16))
        font3 = QFont()
        font3.setPointSize(10)
        self.label_thickness.setFont(font3)
        self.label_thickness.setStyleSheet(u"QLabel {\n"
"	color: #976464;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: #6F4A4A;\n"
"}")
        self.label_thickness.setText(u"\u0422\u043e\u0432\u0449\u0438\u043d\u0430")
        self.label_thickness.setAlignment(Qt.AlignCenter)
        self.label_size = QLabel(self.frame_3)
        self.label_size.setObjectName(u"label_size")
        self.label_size.setGeometry(QRect(24, 46, 61, 16))
        self.label_size.setFont(font3)
        self.label_size.setStyleSheet(u"QLabel {\n"
"	color: #976464;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: #6F4A4A;\n"
"}")
        self.label_size.setText(u"\u0420\u043e\u0437\u043c\u0456\u0440")
        self.label_size.setAlignment(Qt.AlignCenter)
        self.size_spinbox = QSpinBox(self.frame_3)
        self.size_spinbox.setObjectName(u"size_spinbox")
        self.size_spinbox.setGeometry(QRect(34, 20, 42, 22))
        self.size_spinbox.setWrapping(False)
        self.size_spinbox.setAlignment(Qt.AlignCenter)
        self.size_spinbox.setSpecialValueText(u"")
        self.size_spinbox.setSuffix(u"")
        self.size_spinbox.setPrefix(u"")
        self.size_spinbox.setMinimum(25)
        self.size_spinbox.setMaximum(50)
        self.size_spinbox.setValue(30)

        self.horizontalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.dockWidgetContents_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(200, 16777215))
        self.frame_4.setStyleSheet(u"QSpinBox {\n"
"	border: 0px;\n"
"	background: #E9DAC1;\n"
"	color: #632626;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_copy = QLabel(self.frame_4)
        self.label_copy.setObjectName(u"label_copy")
        self.label_copy.setGeometry(QRect(114, 46, 61, 16))
        self.label_copy.setFont(font3)
        self.label_copy.setStyleSheet(u"QLabel {\n"
"	color: #976464;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: #6F4A4A;\n"
"}")
        self.label_copy.setText(u"\u041a\u043e\u043f\u0456\u044e\u0432\u0430\u0442\u0438")
        self.label_copy.setAlignment(Qt.AlignCenter)
        self.label_save = QLabel(self.frame_4)
        self.label_save.setObjectName(u"label_save")
        self.label_save.setGeometry(QRect(24, 46, 61, 16))
        self.label_save.setFont(font3)
        self.label_save.setStyleSheet(u"QLabel {\n"
"	color: #976464;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: #6F4A4A;\n"
"}")
        self.label_save.setText(u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438")
        self.label_save.setAlignment(Qt.AlignCenter)
        self.save_btn = QPushButton(self.frame_4)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(39, 14, 32, 32))
        self.save_btn.setIconSize(QSize(24, 24))
        self.save_btn.setFont(font1)
        self.save_btn.setToolTipDuration(4)
        self.save_btn.setStyleSheet(u"border: 0px;\n"
"background: #F6F0E8;")
        self.save_btn.setText(u"")
        self.save_btn.setAutoDefault(False)
        self.save_btn.setFlat(True)
        self.copy_btn = QPushButton(self.frame_4)
        self.copy_btn.setObjectName(u"copy_btn")
        self.copy_btn.setGeometry(QRect(125, 14, 32, 32))
        self.copy_btn.setIconSize(QSize(24, 24))
        self.copy_btn.setFont(font1)
        self.copy_btn.setToolTipDuration(4)
        self.copy_btn.setStyleSheet(u"border: 0px;\n"
"background: #F6F0E8;")
        self.copy_btn.setText(u"")
        self.copy_btn.setAutoDefault(False)
        self.copy_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.frame_4)

        self.dock_widget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.TopDockWidgetArea, self.dock_widget)

        self.retranslateUi(MainWindow)

        self.save_btn.setDefault(False)
        self.copy_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Електронно-графічна Формула", None))
    # retranslateUi

