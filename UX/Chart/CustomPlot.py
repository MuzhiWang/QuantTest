# -*- coding: utf-8 -*-
"""
This example demonstrates the creation of a plot with a customized
AxisItem and ViewBox. 
"""

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import datetime
import random
import pandas as pd
from Strategies.EightDiagrams import EightDiagrams
from Controller.Entities import DF_MA

class DateAxis(pg.AxisItem):
    def __init__(self, dates, orientation, pen=None, linkView=None, parent=None, maxTickLength=-5, showValues=True):
        super(DateAxis, self).__init__(orientation, pen, linkView, parent, maxTickLength, showValues)
        self.dates = dates

    def tickStrings(self, values, scale, spacing):
        strns = []
        length = len(self.dates)
        for x in values:
            print(x)
            # 保证下标不越界,很重要,越界会导致最终plot坐标轴label无显示
            thisind = np.clip(int(x + 0.5), 0, length - 1)
            xx = self.dates[thisind]
            # print(f'x: {x}, xx:{xx}  thisind = {thisind}')
            try:
                strns.append(datetime.datetime.fromtimestamp(xx).strftime('%Y-%m-%d %H:%M:00'))
            except ValueError:  ## Windows can't handle dates before 1970
                strns.append('')
        return strns

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


click_idx = 0
symbols = ['o', 's', 't', 'd', '+']
def clicked1(curve, points):
    global click_idx
    print(curve)
    curve.setSymbol(symbols[click_idx % len(symbols)])
    click_idx += 1
    print(points)



app = pg.mkQApp()

eight_diagrams = EightDiagrams()
ed_dict = eight_diagrams.get_industry_stocks_with_eight_diagrams(
            start_date="2019-07-25",
            end_date="2019-11-02",
            ma_list=[DF_MA.MACatogary.TWNTY_DAYS, DF_MA.MACatogary.TEN_DAYS, DF_MA.MACatogary.FIVE_DAYS],
            industry_ids=["852121"] # 6 stocks
            # industry_ids=["801770"] # 104 stocks
            # industry_ids=["801710"] # 67 stocks
            # industry_ids=["801710", "852121", "801770"] # 67 stocks
        )
ed_df = ed_dict["852121"]
dates = ed_df['date'].to_numpy()

axis = DateAxis(orientation='bottom', dates=dates)
vb = CustomViewBox()

pw = pg.PlotWidget(viewBox=vb, axisItems={'bottom': axis}, enableMenu=False, title="PlotItem with custom axis and ViewBox<br>Menu disabled, mouse behavior changed: left-drag to zoom, right-click to reset zoom")
length = len(dates)
dates_idx = np.arange(length)
vals = ed_df['eight_diagrams'].to_numpy()

# axis.dates = dates
curve1 =pw.plot(x=dates_idx, y=vals, symbol='o')
curve1.sigPointsClicked.connect(clicked1)
pw.show()
pw.setWindowTitle('pyqtgraph example: customPlot')

# r = pg.PolyLineROI([(0,0), (10, 10)])
# pw.addItem(r)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
