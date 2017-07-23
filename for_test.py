#coding=utf8

# from OnePy.tools.to_Mongodb import Forex_CSV_to_MongoDB
import pandas as pd
import matplotlib.pyplot as plt
import OnePy as op
from OnePy import indicator as ind
###### save csv to MongoDB Demo
# test = Forex_CSV_to_MongoDB(database='Forex_30m', collection='EUR_JPY')
# test.csv_to_db(path='EUR_JPY30m.csv')


####### Strategy Demo
class MyStrategy(op.StrategyBase):
        # 可用参数：
        #     list格式： self.cash, self.position, self.margin,
        #                self.total, self.unre_profit
    def __init__(self,marketevent):
        super(MyStrategy,self).__init__(marketevent)

    def prenext(self):
        # print sum(self.re_profit)
        # print self.unre_profit[-1]
        pass

    def next(self):
        """这里写主要的策略思路"""
        # if ind.SMA(period=5, index=-1)

        # print self.i
        if self.i.SMA(period=5, index=-1) > self.i.SMA(period=10,index=-1):

            self.Buy(2,limit=self.pips(50))
        else:
            self.Sell(0.1)

go = op.OnePiece()

data = op.Forex_CSVFeed(datapath='data/EUR_USD30m.csv',instrument='EUR_JPY',
                        fromdate='2012-03-01',todate='2012-04-02',
                         timeframe=1)

data2 = op.Tushare_CSVFeed(datapath='data/000001.csv',instrument='000001',
                        # fromdate='2012-03-01',todate='2012-04-02',
                         timeframe=1)

data_list = [data]
portfolio = op.PortfolioBase
strategy = MyStrategy
broker = op.SimulatedBroker

# go.set_backtest(data_list,[strategy],portfolio,broker,'Stock')
# go.set_commission(commission=0.1,margin=0,mult=1)         # Stock Mode

go.set_backtest(data_list,[strategy],portfolio,broker,'Forex')
go.set_commission(commission=20,margin=325,mult=100000)
go.set_cash(100000)                 # 设置初始资金

# go.set_notify()                    # 打印交易日志
# go.set_pricetype(‘close’)        # 设置成交价格为close，若不设置，默认为open
go.sunny()                         # 开始启动策略
go.plot('EUR_JPY')
# 画图模块缓慢开发中，先随意画出价格图
# df = pd.DataFrame(go.feed_list[0].bar_dict['EUR_JPY'])
# df.set_index('date',inplace=True)
# df['close'].plot(figsize=(15,3))
# plt.show()
# print df

# 简易的画图，将后面想要画的选项后面的 1 删掉即可
# go.oldplot(['un_profit','re_profit','position1','cash1',
#         'total','margin1','avg_price1','total_profit'])
