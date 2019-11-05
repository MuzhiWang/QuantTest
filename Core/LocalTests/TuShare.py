import tushare as ts
import pprint
import csv
import pandas
import matplotlib.pyplot as plt
import os


print(ts.__version__)

ts.set_token('2fe3395cd410fb8ef0c467b5f5c5e871a69050f7d1ba434299d7ceab')
pandas.set_option('expand_frame_repr', False)

pro = ts.pro_api()

# df = pro.query('trade_cal', exchange='', start_date='20180901', end_date='20181001', fields='', is_open='0')

df = ts.pro_bar(ts_code='000001.SZ', start_date='20181001', end_date='20181011', freq='1min')[['trade_time', 'close']]

df['trade_time'] = pandas.to_datetime(df['trade_time'])
df.set_index('trade_time', inplace=True)

if not os.path.exists('/tmp'):
    os.mkdir('/tmp')
file = '/tmp/000001.csv'
f = open(file, 'w')
df.to_csv(file)

# print(df['trade_time'])

# with open('test_csv.csv', 'wb') as file:
print(df)
print(df.dtypes)


ax = df.plot(color='RED')
ax.set_xlabel('trade_date')
ax.set_ylabel('399300.SZ close')
# plt.show()
