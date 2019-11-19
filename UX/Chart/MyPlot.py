from PyQt5 import QtWidgets, QtCore
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import sys

class MyPolt(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.__df_map = None

    def initUI(self, df_map: {}):
        self.__df_map = df_map
        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)

        # plot =

        # grid.addWidget()

        for key, df in df_map.items():
            cb = QtWidgets.QCheckBox(key)
            cb.move(10, df * 100)
            cb.toggle()
            cb.stateChanged.connect(self.selectCheckbox)
            grid.addWidget(cb)

        # self.
        self.show()


    def selectCheckbox(self, state):
        if state == QtCore.Checked:
            self.setWindowTitle('checked')
        else:
            self.setWindowTitle('no checked')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyPolt()
    ex.initUI({'00001': 1, '00002': 2})
    sys.exit(app.exec_())