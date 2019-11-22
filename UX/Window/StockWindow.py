import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from UX.Chart.BasicMultiDfPlotWithSelection import ApplicationWindow
from Config.StockConfig import StockDataType
from Gateway.Config import TDX_BLOCK_NAME
from Controller.Entities import DF_MA
from Strategies.EightDiagrams import EightDiagrams
from Controller.StockController import StockController
from Core.Provider.StockProvider import StockProvider
from Config.StockConfig import StockDataSource, StockDataType

class StockWindow(QtWidgets.QMainWindow):

    def __init__(self, strategy_name: str):
        QtWidgets.QMainWindow.__init__(self)

        self.setMinimumSize(QtCore.QSize(1280, 960))
        self.setWindowTitle(f"{strategy_name} Stock Window")



if __name__ == '__main__':
    stock_provider = StockProvider()
    df = stock_provider.get_stock_df(StockDataSource.TDX, StockDataType.ONE_MIN,
                                     '000903', '2019-07-25', '2019-11-15')
    df_dict = {
        '000903 中证100': df
    }

    print(df_dict)

    app = QtWidgets.QApplication(sys.argv)
    aw = ApplicationWindow(df_dict=df_dict, y_asix='close')
    aw.show()
    sys.exit(app.exec_())