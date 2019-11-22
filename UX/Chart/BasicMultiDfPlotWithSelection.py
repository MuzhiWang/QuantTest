import random
import matplotlib
from matplotlib.ticker import FuncFormatter

from Common.Exception.UnimplementedException import UnimplementedException

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QHBoxLayout, QSizePolicy, QMessageBox, QWidget, QCheckBox
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import datetime



class MyMplCanvas(FigureCanvas):

    __init_dates = None
    __idx_length = None

    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100, df_map={}, x_asix='date', y_asix='close'):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.plot_map = {}
        self.x_asix = x_asix
        self.y_asix = y_asix
        # annot = self.axes.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
        #                     bbox=dict(boxstyle="round", fc="w"),
        #                     arrowprops=dict(arrowstyle="->"))
        # annot.set_visible(False)
        # self.annotaion = annot
        #
        # fig.canvas.mpl_connect("motion_notify_event", )

        self.compute_initial_figure(df_map)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self, df_map: {}):
        idx = None
        for key, df in df_map.items():
            # initial index and date xaxis
            if idx is None:
                MyMplCanvas.__idx_length = len(df.index)
                idx = np.arange(MyMplCanvas.__idx_length)
                MyMplCanvas.__init_dates = df[self.x_asix]
            vals = df[self.y_asix].to_numpy()
            p = self.axes.plot(idx, vals)
            self.plot_map[key] = p

        self.axes.xaxis.set_major_formatter(FuncFormatter(MyMplCanvas.format_date))

    def display_plot(self, plot_id: str, display: bool):
        for line in self.plot_map[plot_id]:
            line.set_visible(display)
        self.draw()

    @staticmethod
    def format_date(x, pos=None):
        # 保证下标不越界,很重要,越界会导致最终plot坐标轴label无显示
        thisind = np.clip(int(x + 0.5), 0, MyMplCanvas.__idx_length - 1)

        x = MyMplCanvas.__init_dates[thisind]

        # print(type(x))
        if isinstance(x, str):
            return x
        elif isinstance(x, np.int64) or isinstance(x, float) or isinstance(x, int):
            return datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d')
        else:
            raise UnimplementedException

class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""
    # def compute_initial_figure(self, df_map: {}):
    #     t = arange(0.0, 3.0, 0.01)
    #     s = sin(2*pi*t)
    #     p = self.axes.plot(t, s)
    #     self.test_plot = p
    pass


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
        self.setChecked(True)
        self.stateChanged.connect(self.check_clicked)

    def check_clicked(self, state):
        if state == QtCore.Qt.Checked:
            self.__canvas.display_plot(self.__label, True)
            # for line in self.__canvas.test_plot:
            #     print(f"test plot line: {line}")
            #     line.set_visible(True)
            print(f"{self.text()} is checked")
        else:
            self.__canvas.display_plot(self.__label, False)
            # for line in self.__canvas.test_plot:
            #     line.set_visible(False)
            print(f"{self.text()} unchecked")

class ApplicationWindow(QMainWindow):
    def __init__(self, df_dict: {}, x_asix='date', y_asix='close'):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("main window")
        self.setStyleSheet(StyleSheet)
        self.setMinimumSize(QtCore.QSize(1280, 960))

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
        main_layout.addLayout(plot_layout, stretch=4)
        main_layout.addLayout(label_layout, stretch=1)


        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100, df_map=df_dict, x_asix=x_asix, y_asix=y_asix)
        # dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100, df_map=df_map)
        plot_layout.addWidget(sc)
        # plot_layout.addWidget(dc)

        for key, df in df_dict.items():
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

StyleSheet = '''
QCheckBox {
    spacing: 5px;
    font-size:25px;     /* <--- */
}

QCheckBox::indicator {
    width:  33px;
    height: 33px;
}
'''
