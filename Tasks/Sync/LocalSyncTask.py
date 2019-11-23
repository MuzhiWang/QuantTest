import time
from Config import StockConfig
from Core.Provider import StockProvider
from Common.RunningTimeDecorator import running_time

class LocalSyncTask(object):

    __stock_provider = None

    def __init__(self):
        self.__stock_provider = StockProvider.StockProvider()


    @running_time
    def tdx_local_sync_task(self):
        print(f"start to sync TDX data from local files")
        self.__stock_provider.get_and_store_local_stock(data_source=StockConfig.StockDataSource.TDX,
                                                        stock_data_type=StockConfig.StockDataType.FIVE_MINS,
                                                        force_upsert=False)
        self.__stock_provider.get_and_store_local_stock(data_source=StockConfig.StockDataSource.TDX,
                                                        stock_data_type=StockConfig.StockDataType.ONE_MIN,
                                                        force_upsert=False)




if __name__ == "__main__":
    local_sync_task = LocalSyncTask()
    local_sync_task.tdx_local_sync_task()