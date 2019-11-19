import sys
import random
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QHBoxLayout, QSizePolicy, QMessageBox, QWidget, QCheckBox
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100, df_map={}):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.test_plot = None
        # We want the axes cleared every time plot() is called
        # self.axes.hold(False)

        self.compute_initial_figure(df_map)

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self, df_map: {}):
        pass

    def display_test_plot(self, display: bool):
        for line in self.test_plot:
            line.set_visible(display)
        self.draw()


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""
    def compute_initial_figure(self, df_map: {}):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        p = self.axes.plot(t, s)
        self.test_plot = p


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(500)

    def compute_initial_figure(self, df_map: {}):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]

        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()

class MyCheckbox(QCheckBox):

    def __init__(self, label, canvas: MyMplCanvas):
        super().__init__(label)
        self.__label = label
        self.__canvas = canvas
        self.stateChanged.connect(self.check_clicked)

    def check_clicked(self, state):
        if state == QtCore.Qt.Checked:
            self.__canvas.display_test_plot(True)
            # for line in self.__canvas.test_plot:
            #     print(f"test plot line: {line}")
            #     line.set_visible(True)
            print(f"{self.text()} is checked")
        else:
            self.__canvas.display_test_plot(False)
            # for line in self.__canvas.test_plot:
            #     line.set_visible(False)
            print(f"{self.text()} unchecked")

class ApplicationWindow(QMainWindow):
    def __init__(self, df_map: {}):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Strategy main window")

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QWidget(self)

        main_layout = QHBoxLayout(self.main_widget)
        plot_layout = QHBoxLayout()
        label_layout = QVBoxLayout()
        main_layout.addLayout(plot_layout, stretch=1)
        main_layout.addLayout(label_layout, stretch=1)

        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100, df_map=df_map)
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100, df_map=df_map)
        plot_layout.addWidget(sc)
        plot_layout.addWidget(dc)

        for key, df in df_map.items():
            cb = MyCheckbox(key, sc)
            label_layout.addWidget(cb)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QMessageBox.about(self, "About",
        """test test test strategy with matplotlib in Pyqt5"""
  )

if __name__ == '__main__':
    app = QApplication(sys.argv)

    aw = ApplicationWindow({'000001':1, '000002':2})
    aw.show()
    sys.exit(app.exec_())