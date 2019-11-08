import jqdatasdk as jq

class JQData_GW(object):

    __user_name = "18611823120"
    __pw = "823120"
    client = None

    def __init__(self):
        pass
        jq.auth(self.__user_name, self.__pw)

    def test(self):
        # jqdatasdk.auth(self.__user_name, self.__pw)
        res = jq.get_price(security="000001.XSHE", frequency="1m")
        print(res)



gw = JQData_GW()
# gw.test()

print(jq.get_query_count())


stocks = jq.get_index_stocks('000300.XSHG')
print(stocks)