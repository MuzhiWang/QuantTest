from flask import Flask

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from Config.StockConfig import StockDataSource, StockDataType
from Core.Provider.StockProvider import StockProvider

app = Flask(__name__)

@app.route('/')
def hello():
    # raise Exception('not sure')
    stock_provider = StockProvider()
    df = stock_provider.get_stock_df(StockDataSource.TDX, StockDataType.ONE_MIN,
                                     '000001', '2019-07-25', '2019-11-20')
    df_dict = {
        '000001 sz': df.to_json()
    }
    return df_dict


if __name__ == '__main__':
    app.run()