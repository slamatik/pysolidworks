from PyQt5 import QtWidgets
from UI_files.main_window import Ui_MainWindow
from UI_files.properties_window import Ui_PropertiesWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.properties_button.clicked.connect(self.hide)


class PropertiesWindow(QtWidgets.QMainWindow, Ui_PropertiesWindow):
    def __init__(self, parent=None):
        super(PropertiesWindow, self).__init__(parent)
        self.setupUi(self)
        self.back_b.clicked.connect(self.hide)


class Manager:
    def __init__(self):
        self.first = MainWindow()
        self.second = PropertiesWindow()

        self.first.properties_button.clicked.connect(self.second.show)
        self.second.back_b.clicked.connect(self.first.show)

        self.first.show()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())
