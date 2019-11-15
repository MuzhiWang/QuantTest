# -*- coding: utf-8 -*-
"""
This example demonstrates the creation of a plot with a customized
AxisItem and ViewBox. 
"""

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import time
import random
import pandas as pd
from Strategies.EightDiagrams import EightDiagrams
from Controller.Entities import DF_MA

class DateAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        # strns = []
        # rng = max(values)-min(values)
        # #if rng < 120:
        # #    return pg.AxisItem.tickStrings(self, values, scale, spacing)
        # if rng < 3600*24:
        #     string = '%H:%M:%S'
        #     label1 = '%b %d -'
        #     label2 = ' %b %d, %Y'
        # elif rng >= 3600*24 and rng < 3600*24*30:
        #     string = '%d'
        #     label1 = '%b - '
        #     label2 = '%b, %Y'
        # elif rng >= 3600*24*30 and rng < 3600*24*30*24:
        #     string = '%b'
        #     label1 = '%Y -'
        #     label2 = ' %Y'
        # elif rng >=3600*24*30*24:
        #     string = '%Y'
        #     label1 = ''
        #     label2 = ''
        # for x in values:
        #     try:
        #         strns.append(time.strftime(string, time.localtime(x)))
        #     except ValueError:  ## Windows can't handle dates before 1970
        #         strns.append('')
        # try:
        #     label = time.strftime(label1, time.localtime(min(values)))+time.strftime(label2, time.localtime(max(values)))
        # except ValueError:
        #     label = ''
        # #self.setLabel(text=label)
        return "t"

class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)
        self.setMouseMode(self.RectMode)
        
    ## reimplement right-click to zoom out
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.autoRange()
            
    def mouseDragEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            ev.ignore()
        else:
            pg.ViewBox.mouseDragEvent(self, ev)


app = pg.mkQApp()

eight_diagrams = EightDiagrams()
ed_dict = eight_diagrams.get_industry_stocks_with_eight_diagrams(
            start_date="2019-09-27",
            end_date="2019-11-02",
            ma_list=[DF_MA.MACatogary.TWNTY_DAYS, DF_MA.MACatogary.TEN_DAYS, DF_MA.MACatogary.FIVE_DAYS],
            industry_ids=["852121"] # 6 stocks
            # industry_ids=["801770"] # 104 stocks
            # industry_ids=["801710"] # 67 stocks
            # industry_ids=["801710", "852121", "801770"] # 67 stocks
        )
ed_df = ed_dict["852121"]

axis = DateAxis(orientation='bottom')
vb = CustomViewBox()

pw = pg.PlotWidget(viewBox=vb, axisItems={'bottom': axis}, enableMenu=False, title="PlotItem with custom axis and ViewBox<br>Menu disabled, mouse behavior changed: left-drag to zoom, right-click to reset zoom")
dates = pd.to_datetime(ed_df['date'], unit='s').to_numpy()
vals = ed_df['eight_diagrams'].to_numpy()
pw.plot(x=dates, y=vals, symbol='o')
pw.show()
pw.setWindowTitle('pyqtgraph example: customPlot')

# r = pg.PolyLineROI([(0,0), (10, 10)])
# pw.addItem(r)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
