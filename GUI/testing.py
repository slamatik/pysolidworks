# from PyQt5 import QtWidgets, QtGui, QtCore
# import sys
#
#
# class Window(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super(Window, self).__init__(parent)
#
#         self.vlayout = QtWidgets.QVBoxLayout()
#         self.pushButton_ok = QtWidgets.QPushButton("Press me", self)
#         self.pushButton_ok.clicked.connect(self.addCheckbox)
#         self.vlayout.addWidget(self.pushButton_ok)
#
#         self.checkBox = QtWidgets.QCheckBox(self)
#         self.vlayout.addWidget(self.checkBox)
#         self.setLayout(self.vlayout)
#
#     def addCheckbox(self):
#         # checkBox = QtWidgets.QCheckBox()
#         self.vlayout.addWidget(QtWidgets.QCheckBox())
#
#
# application = QtWidgets.QApplication(sys.argv)
# window = Window()
# window.setWindowTitle('Dynamically adding checkboxes using a push button')
# window.resize(250, 180)
# window.show()
# sys.exit(application.exec_())


from PyQt5 import QtWidgets
import sys
"""
"""

class MyScrollWidget(QtWidgets.QWidget):

    def __init__(self):
        super(MyScrollWidget, self).__init__()
        lay = QtWidgets.QVBoxLayout(self)

        scrollArea = QtWidgets.QScrollArea()
        lay.addWidget(scrollArea)
        top_widget = QtWidgets.QWidget()
        top_layout = QtWidgets.QVBoxLayout()

        for i in range(10):
            group_box = QtWidgets.QWidget()
            # group_box.setTitle('GroupBox For Item {0}'.format(i))

            layout = QtWidgets.QHBoxLayout(group_box)

            # label = QtWidgets.QLabel()
            # label.setText('Label For Item {0}'.format(i))
            # layout.addWidget(label)

            box = QtWidgets.QCheckBox(group_box)
            layout.addWidget(box)
            # push_button = QtWidgets.QPushButton(group_box)
            # push_button.setText('Run Button')
            # push_button.setFixedSize(100, 32)
            # layout.addWidget(push_button)

            top_layout.addWidget(group_box)

        top_widget.setLayout(top_layout)
        scrollArea.setWidget(top_widget)
        self.resize(200, 500)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MyScrollWidget()
    widget.show()
    sys.exit(app.exec_())

