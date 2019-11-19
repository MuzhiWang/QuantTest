import sys
from PyQt5 import QtGui, QtWidgets, QtCore

class StrategyWindow(QtWidgets.QMainWindow):

    def __init__(self, strategy_name: str):
        QtWidgets.QMainWindow.__init__(self)

        self.setMinimumSize(QtCore.QSize(1280, 960))
        self.setWindowTitle(f"{strategy_name} Strategy Window")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    s_win = StrategyWindow("Eight Diagram")
    s_win.show()
    sys.exit(app.exec_())
