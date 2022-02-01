import pandas as pd
import sys
import os
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from api.sldworks import SldWorks


class Ui_PropertiesWindow(object):
    def setupUi(self, PropertiesWindow):
        PropertiesWindow.setObjectName("PropertiesWindow")
        PropertiesWindow.resize(400, 300)

        self.centralwidget = QtWidgets.QWidget(PropertiesWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.excel_label = self.create_label(self.centralwidget, (20, 20, 80, 20), 'label_1', 'Open Excel file')
        self.export_label = self.create_label(self.centralwidget, (20, 80, 100, 20), 'label_2', 'Export properties')

        self.excel_b = self.create_button(self.centralwidget, (20, 40, 60, 20), 'excelButton', 'Open', self.open_excel)
        self.pushButton_2 = self.create_button(self.centralwidget, (20, 100, 60, 20), 'pushButton_2', 'Open', self.extract_properties)
        self.back_b = self.create_button(self.centralwidget, (140, 220, 80, 20), 'backButton', 'Back')

        # self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        # self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 20, 160, 60))
        # self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        #
        # self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        # self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout.setObjectName("verticalLayout")
        #
        # self.menubar = QtWidgets.QMenuBar(PropertiesWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        # self.menubar.setObjectName("menubar")
        # PropertiesWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(PropertiesWindow)
        # self.statusbar.setObjectName("statusbar")
        # PropertiesWindow.setStatusBar(self.statusbar)

        self.scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(QtCore.QRect(150, 20, 210, 180))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scrollArea")
        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 179, 219))
        self.scroll_area_widget_contents.setObjectName("scrollAreaWidgetContents")
        self.scroll_area.setWidget(self.scroll_area_widget_contents)

        PropertiesWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(PropertiesWindow)
        QtCore.QMetaObject.connectSlotsByName(PropertiesWindow)

    def create_label(self, widget, size, object_name, text):
        label = QtWidgets.QLabel(widget)
        label.setGeometry(QtCore.QRect(*size))
        label.setObjectName(object_name)
        label.setText(text)

    def create_button(self, widget, size, object_name, text, action=None):
        button = QtWidgets.QPushButton(widget)
        button.setGeometry(QtCore.QRect(*size))
        button.setObjectName(object_name)
        button.setText(text)
        if action:
            button.clicked.connect(action)
        return button

    def open_excel(self):
        path = QFileDialog.getOpenFileName(directory=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))[
            0]
        print(path)
        df = pd.read_excel(io=path, engine='openpyxl')
        properties = df.columns
        self.create_checkboxes(len(properties), properties)

    def create_checkboxes(self, n, names):
        top_widget = QtWidgets.QWidget()
        top_layout = QtWidgets.QVBoxLayout()
        checkboxes = []
        for i in range(n):
            group_box = QtWidgets.QWidget()
            layout = QtWidgets.QHBoxLayout(group_box)
            box = QtWidgets.QCheckBox(group_box)
            box.setText(names[i])
            box.setChecked(True)
            layout.addWidget(box)
            top_layout.addWidget(group_box)
            checkboxes.append(box)
        top_widget.setLayout(top_layout)
        self.scroll_area.setWidget(top_widget)
        return checkboxes

    def extract_properties(self):
        sw = SldWorks()
        sw.visible = True
        sw.command_in_progress = True
        sw.enable_background_processing = True
        path = QFileDialog.getExistingDirectory(directory=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
        sw.export_custom_properties(folder=path, file_name='test2')

    def retranslateUi(self, PropertiesWindow):
        _translate = QtCore.QCoreApplication.translate
        PropertiesWindow.setWindowTitle(_translate("PropertiesWindow", "MainWindow"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    PropertiesWindow = QtWidgets.QMainWindow()
    ui = Ui_PropertiesWindow()
    ui.setupUi(PropertiesWindow)
    PropertiesWindow.show()
    sys.exit(app.exec_())
