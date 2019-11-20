from __future__ import print_function

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.dates import bytespdate2num, num2date
from matplotlib.ticker import Formatter, FuncFormatter
import pandas as pd
import datetime

from Config.StockConfig import StockDataType
from Controller.Entities import DF_MA
from Strategies.EightDiagrams import EightDiagrams

# file = r'C:\Users\wmz66\PycharmProjects\Quant\QuantTest\Tests\stock_with_ma.csv'
# df = pd.read_csv(file)
LAST_DATE = -1

class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%Y-%m-%d'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        return datetime.datetime.fromtimestamp(x).strftime(self.fmt)

# formatter = MyFormatter(df['date'])



def format_date(x, pos=None):
    length = len(dates)
    #保证下标不越界,很重要,越界会导致最终plot坐标轴label无显示
    thisind = np.clip(int(x+0.5), 0, length - 1)

    x = dates[thisind]
    # print(f'x: {x}')
    return datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d')

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(FuncFormatter(format_date))


eight_diagrams = EightDiagrams()
ed_dict = eight_diagrams.get_industry_stocks_with_eight_diagrams(StockDataType.ONE_MIN,
                                                                 start_date="2019-07-25", end_date="2019-11-02",
                                                                 ma_list=[DF_MA.MACatogary.TWNTY_DAYS,
                                                                          DF_MA.MACatogary.TEN_DAYS,
                                                                          DF_MA.MACatogary.FIVE_DAYS],
                                                                 industry_ids=["852121"])

# idx = 0
markers = ['o-', 'r+']
dates = None
for key, df_val in ed_dict.items():
    dates = df_val['date']
    vals = df_val['eight_diagrams'].to_numpy()


    length = len(df_val.index)
    idx = np.arange(length)

    ax.plot(idx, vals, 'o-')
    # idx += 1
fig.autofmt_xdate()
plt.show()