from flask import Flask, request
from flask_cors import CORS
import json

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Common.Exception import InvalidRequestException
from Config.StockConfig import StockDataSource
from Core.Provider.StockProvider import StockProvider
from App.WebConfig import Constants, BlockCategory
import App.WebUtils as webUtils
from Tasks.Sync.LocalSyncTask import LocalSyncTask
from Strategies.EightDiagrams import EightDiagrams
import Gateway.Config as cfg
from Handler import TdxReader

app = Flask(__name__)
CORS(app)

stock_provider = StockProvider()
local_sync_task = LocalSyncTask()
eight_diagrams = EightDiagrams()

@app.route('/get_stock_df', methods=['GET'])
def get_stock_df():
    stock_id = request.args.get('stock_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    date_type = request.args.get('date_type')
    index = request.args.get('index')

    if stock_id is None or start_date is None \
        or end_date is None or date_type is None:
        raise InvalidRequestException

    print(stock_id)
    print(f'start {start_date} - end {end_date}')

    if date_type not in Constants.DATE_TYPE:
        raise InvalidRequestException

    is_index = False
    if index is not None and index:
        is_index = True

    if is_index:
        df = stock_provider.get_index_df(StockDataSource.TDX, Constants.DATE_TYPE[date_type],
                                         stock_id, start_date, end_date)
    else:
        df = stock_provider.get_stock_df(StockDataSource.TDX, Constants.DATE_TYPE[date_type],
                                     stock_id, start_date, end_date)

    if df is None:
        raise Exception(f"stock {stock_id} data not exist in system!")

    return df.to_json()



@app.route('/sync_data/stocks_with_tdx_local_files', methods=['POST'])
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

@app.route('/get_industries', methods=['GET'])
def get_industries():
    # industry_code should be
    # sw_l1 = 0 # 申万一级行业;
    # sw_l2 = 1 # 申万二级行业;
    # sw_l3 = 2 # 申万三级行业
    # jq_l1 = 3 # 聚宽一级行业
    # jq_l2 = 4 # 聚宽二级行业
    # zjw = 5  # 证监会行业
    industry_code = request.args.get('industry_code')

    if industry_code is None:
        raise InvalidRequestException(f'no <code> query parameter')

    df = stock_provider.get_industries(cfg.IndustryCode[industry_code])
    return df.to_json()


@app.route('/get_industry_stocks', methods=['GET'])
def get_industry_stocks():
    # Specific industry code, e.g. '801740', '801020'
    industry_code = request.args.get('code')

    if industry_code is None:
        raise InvalidRequestException(f'no <code> query parameter')

    stock_list = stock_provider.get_industry_stocks(industry_code)

    return json.dumps(stock_list)

@app.route('/get_all_index_with_stocks', methods=['GET'])
def get_all_index_with_stocks():
    df = stock_provider.get_all_blocks_with_stocks(StockDataSource.TDX)

    return df.to_json()


@app.route('/strategy/eight_diagrams_scores', methods=['POST'])
def get_eight_diagrams_scores():
    data = request.get_json()
    block = data['block']
    if block is None or block not in Constants.BLOCK_DICT:
        raise InvalidRequestException(f'block {block} must exist or be <index> or <industry>')

    start_date = data['start_date']
    end_date = data['end_date']
    date_type = data['date_type']
    ma_list = webUtils.convert_ma_list(data['ma_list'])
    if start_date is None or ma_list is None \
        or end_date is None or date_type is None:
        raise InvalidRequestException

    if Constants.BLOCK_DICT[block] == BlockCategory.INDEX:
        index_names = webUtils.convert_index_names(data['index_names'])
        if index_names is None or len(index_names) == 0:
            raise InvalidRequestException(f'no index names')
        df_dict = eight_diagrams.get_index_block_stocks_with_eight_diagrams(
            stock_date_type=Constants.DATE_TYPE[date_type],
            start_date=start_date,
            end_date=end_date,
            ma_list=ma_list,
            block_names=index_names
        )
        return webUtils.serialize_df_dict(df_dict)
    elif Constants.BLOCK_DICT[block] == BlockCategory.INDUSTRY:
        industry_codes = data['industry_codes']
        if industry_codes is None or len(industry_codes) == 0:
            raise InvalidRequestException(f'no industry codes')
        df_dict = eight_diagrams.get_industry_stocks_with_eight_diagrams(
            stock_date_type=Constants.DATE_TYPE[date_type],
            start_date=start_date,
            end_date=end_date,
            ma_list=ma_list,
            industry_ids=industry_codes
        )
        return webUtils.serialize_df_dict(df_dict)
    else:
        raise InvalidRequestException(f'no block registered')


if __name__ == '__main__':
    TdxReader.serve()
    app.run()
