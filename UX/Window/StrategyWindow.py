import sys
from PyQt5 import QtGui, QtWidgets

class StrategyWindow(object):

    def window(self):
        app = QtGui.QGuiApplication(sys.argv)
        widget = QtWidgets.QWidget()
        label = QtWidgets.QLabel(widget)

        label.setText("Test label...")
        widget.setGeometry(100, 100, 200, 50)
        label.move(50, 20)
        widget.setWindowTitle("This widget")
        widget.show()

        sys.exit(app.exec_())


if __name__ == '__main__':
    s_win = StrategyWindow()
    s_win.window()
