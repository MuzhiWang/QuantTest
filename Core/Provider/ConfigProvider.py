import configparser
import os
import json

class ConfigProvider(object):

    __parser = None
    __config = None

    def __init__(self):
        self.__parser = configparser.ConfigParser()
        current_file = os.path.abspath(os.path.dirname(__file__))
        config_file_path = os.path.join(current_file, '../../config.json')
        with open(config_file_path, 'r') as config_file:
            self.__config = json.load(config_file)

        # print(parent_of_parent_dir)
        # self.__parser.read_file(open(config_file_path))

    def get_config(self):
        return self.__config

    def get_tdx_directory_path(self, subpath = None):
        path = self.get_config()['paths']['tdx_directory_path']
        return path if subpath is None else path[subpath]


