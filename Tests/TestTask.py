import unittest
import time
from Controller import StockController
from Controller.Entities import DF_MA
import pandas as pd
from Strategies.EightDiagrams import EightDiagrams
from Common.Log.Logger import Logger
from Common.RunningTimeDecorator import running_time

from Controller.StockController import StockController
from Config.StockConfig import StockDataType
from Gateway.Config import TDX_BLOCK_NAME
from Tasks.Sync import LocalSyncTask


class TestTask(unittest.TestCase):

    __local_sync_task = LocalSyncTask.LocalSyncTask()

    @running_time
    def test_local_sync_task(self):
        TestTask.__local_sync_task.tdx_local_sync_stocks_task(
            stock_ids=['000001', '000001.IDX'],
            stock_date_type=StockDataType.DAILY
        )