import time
from Config import StockConfig
from Core.Provider import StockProvider

class LocalSyncTask(object):

    __stock_provider = None

    def __init__(self):
        self.__stock_provider = StockProvider.StockProvider()


    def tdx_local_sync_task(self):
        print(f"start to sync TDX data from local files")
        start = time.time()
        self.__stock_provider.get_and_store_local_stock(StockConfig.StockDataSource.TDX,
                                                        StockConfig.StockDataType.FIVE_MINS)
        print(f"sync task {self.__str__()} spend time: {(time.time() - start) * 1000} ms")




if __name__ == "__main__":
    local_sync_task = LocalSyncTask()
    local_sync_task.tdx_local_sync_task()