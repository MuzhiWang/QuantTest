import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtk

file = r'C:\Users\wmz66\PycharmProjects\Quant\QuantTest\Tests\stock_with_ma.csv'
df = pd.read_csv(file)
#用下标代理原始时间戳数据
idx_pxy = pd.to_datetime(df['date'], unit='s').to_numpy()
#下标-时间转换func
def x_fmt_func(x, pos=None):
    idx = np.clip(int(x + 0.5), 0, df.shape[0] - 1)
    return df['date'].iat[idx]
#绘图流程
def decorateAx(ax, xs, ys, x_func):
    ax.plot(xs, ys, color="green", linewidth=1, linestyle="-")
    ax.plot(ax.get_xlim(), [0,0], color="blue",
            linewidth=0.5, linestyle="--")
    if x_func:
        #set数据代理func
        ax.xaxis.set_major_formatter(mtk.FuncFormatter(x_func))
    ax.grid(True)
    return

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
print(idx_pxy)
decorateAx(ax1, idx_pxy, df['close'], x_fmt_func)
decorateAx(ax2, idx_pxy, df['close'], x_fmt_func)
#优化label显示,非必须
fig.autofmt_xdate()
plt.show()