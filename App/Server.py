from flask import Flask, request
from flask_cors import CORS

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Common.Exception import InvalidRequestException
from Config.StockConfig import StockDataSource
from Core.Provider.StockProvider import StockProvider
from App.WebConfig import Constants
from Tasks.Sync.LocalSyncTask import LocalSyncTask

app = Flask(__name__)
CORS(app)

stock_provider = StockProvider()
local_sync_task = LocalSyncTask()

@app.route('/get_stock_df', methods=['GET'])
def get_stock_df():
    stock_id = request.args.get('stock_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    date_type = request.args.get('date_type')

    if stock_id is None or start_date is None \
        or end_date is None or date_type is None:
        raise InvalidRequestException

    print(stock_id)
    print(f'start {start_date} - end {end_date}')

    if date_type not in Constants.DATE_TYPE:
        raise InvalidRequestException

    df = stock_provider.get_stock_df(StockDataSource.TDX, Constants.DATE_TYPE[date_type],
                                     stock_id, start_date, end_date)

    return df.to_json()



@app.route('/sync_stocks_with_tdx_local_files', methods=['POST'])
def sync_stocks_with_tdx_local_files():
    data = request.get_json()
    stock_ids = data['stock_ids']
    date_type = data['date_type']

    if stock_ids is None or date_type is None:
        raise InvalidRequestException

    print(f'Try to sync stocks: {stock_ids}')

    if date_type not in Constants.DATE_TYPE:
        raise InvalidRequestException

    local_sync_task.tdx_local_sync_stocks_task(
        stock_ids=stock_ids,
        stock_date_type=Constants.DATE_TYPE[date_type]
    )

    return "OK"



if __name__ == '__main__':
    app.run()