from PyQt5 import QtWidgets
import sys

class MyScrollWidget(QtWidgets.QWidget):
    def __init__(self):
        super(MyScrollWidget, self).__init__()
        layout = QtWidgets.QVBoxLayout(self)
        scroll_area = QtWidgets.QScrollArea()
        layout.addWidget(scroll_area)

        top_widget = QtWidgets.QWidget()
        top_layout = QtWidgets.QVBoxLayout()

        for i in range(10):
            # c_box = QtWidgets.QCheckBox(layout)
            g_box = QtWidgets.QGroupBox()
            l = QtWidgets.QHBoxLayout(g_box)
            c_box = QtWidgets.QCheckBox(g_box)
            c_box.setText(f'{i}')
            l.addWidget(c_box)
            top_layout.addWidget(g_box)

        top_widget.setLayout(top_layout)
        scroll_area.setWidget(top_widget)
        self.resize(100, 100)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MyScrollWidget()
    widget.show()
    sys.exit(app.exec_())