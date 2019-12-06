from Common.Exception.InvalidRequestException import InvalidRequestException
from .WebConfig import Constants
import json

def convert_ma_list(ma_list: []):
    res = []
    for ma in ma_list:
        if ma not in Constants.MA_DICT:
            raise InvalidRequestException(f'invalid ma value: {ma}')
        res.append(Constants.MA_DICT[ma])
    return res

def convert_index_names(index_names: []):
    res = []
    for name in index_names:
        if name not in Constants.INDEX_DICT:
            raise InvalidRequestException(f'invalid index name: {name}')
        res.append(Constants.INDEX_DICT[name])
    return res

def serialize_df_dict(df_dict: {}):
    res = {}
    for key, df in df_dict.items():
        res[key] = df.to_json()
    return json.dumps(res)