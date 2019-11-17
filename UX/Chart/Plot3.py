import pyqtgraph as pg

from PyQt5 import QtGui
import numpy as np
import sys



def main():
    pass

def clicked1(curve, points):
    print(curve)

    print(points)

def clicked2(points):
    print(points)



app = QtGui.QApplication(sys.argv)

widg = QtGui.QWidget()

widg.move(100, 100)



pgWidg = pg.GraphicsLayoutWidget()

pgWidg.resize(750, 250)



graph = pgWidg.addPlot(row=1, col=1)

curve1 = graph.plot(y=np.sin(np.linspace(0, 20, 1000)), symbol='o',
clickable=True)

curve2 = graph.plot(y=np.sin(np.linspace(1, 21, 1000)), pen='r',
clickable=True)

curve3 = pg.PlotCurveItem(y=np.sin(np.linspace(2, 22, 1000)), pen='b',
clickable=True)

graph.addItem(curve3)



curve1.sigPointsClicked.connect(clicked1)

curve2.sigPointsClicked.connect(clicked1)

curve2.sigClicked.connect(clicked2)

curve3.sigClicked.connect(clicked2)



grid = QtGui.QGridLayout()

grid.addWidget(pgWidg, 0,0)

widg.setLayout(grid)

widg.show()

sys.exit(app.exec_())




if __name__ == '__main__':

    main()