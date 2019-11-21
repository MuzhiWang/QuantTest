import configparser
import os
import json
from Common import FileUtils
from Config.StockConfig import StockDataType

class ConfigProvider(object):

    __parser = None
    __config = None

    def __init__(self):
        self.__parser = configparser.ConfigParser()
        current_file = os.path.abspath(os.path.dirname(__file__))
        config_file_path = os.path.join(
            current_file, FileUtils.convert_file_path_based_on_system('../../config.json'))
        with open(config_file_path, 'r') as config_file:
            self.__config = json.load(config_file)

        # print(parent_of_parent_dir)
        # self.__parser.read_file(open(config_file_path))

    def get_config(self):
        return self.__config

    def get_tdx_stock_directory_path(self, stock_data_type: StockDataType, subpath=None):
        path = self.get_config()['paths']['tdx_directory_path'][stock_data_type.name]
        return path if subpath is None else path[subpath]

    def get_tdx_block_directory_path(self):
        return self.get_config()['paths']['tdx_directory_path']['BLOCK']


