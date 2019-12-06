import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from UX.Chart.BasicMultiDfPlotWithSelection import ApplicationWindow
from Config.StockConfig import StockDataType
from Gateway.Config import TDX_BLOCK_NAME
from Controller.Entities import DF_MA
from Strategies.EightDiagrams import EightDiagrams

class StrategyWindow(QtWidgets.QMainWindow):

    def __init__(self, strategy_name: str):
        QtWidgets.QMainWindow.__init__(self)

        self.setMinimumSize(QtCore.QSize(1280, 960))
        self.setWindowTitle(f"{strategy_name} Strategy Window")



if __name__ == '__main__':
    eight_diagrams = EightDiagrams()
    # ed_dict = eight_diagrams.get_industry_stocks_with_eight_diagrams(StockDataType.FIVE_MINS,
    #                                                                  start_date="2019-07-25", end_date="2019-11-02",
    #                                                                  ma_list=[DF_MA.MACatogary.TWNTY_DAYS,
    #                                                                           DF_MA.MACatogary.TEN_DAYS,
    #                                                                           DF_MA.MACatogary.FIVE_DAYS],
    #                                                                  # industry_ids=["852121", "801018"])
    #                                                                  industry_ids=["801111", "801203", "801051"]) # 47 + 50 + 33
    ed_dict = eight_diagrams.get_index_block_stocks_with_eight_diagrams(StockDataType.FIVE_MINS,
                                                                        start_date="2019-07-25", end_date="2019-11-02",
                                                                        ma_list=[DF_MA.MACatogary.TWNTY_DAYS,
                                                                           DF_MA.MACatogary.TEN_DAYS,
                                                                           DF_MA.MACatogary.FIVE_DAYS],
                                                                        # industry_ids=["852121", "801018"])
                                                                        # block_names=[TDX_BLOCK_NAME.ZHONGZHENG_100,
                                                                        #              TDX_BLOCK_NAME.CHUANGYEBANZHI,
                                                                        #              TDX_BLOCK_NAME.ZHONGZHENGHONGLI])
                                                                        block_names=[TDX_BLOCK_NAME.HUSHENG_300])

    app = QtWidgets.QApplication(sys.argv)
    aw = ApplicationWindow(df_dict=ed_dict, y_asix='eight_diagrams')
    aw.show()
    sys.exit(app.exec_())