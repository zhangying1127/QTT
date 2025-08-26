from unittest import TestCase
import pandas as pd
# from mpl_finance import candlestick2_ochl
import mplfinance as mpf
import matplotlib.pyplot as plt
import akshare as ak




class TestPandasKLine():
    file_name = "./QTT/data/demo_000001.csv"
    
    # 获取数据    
    def getData(self):
        df = ak.stock_zh_a_hist(symbol="000001", period="daily", 
            start_date="20090101", end_date="20090201", 
            adjust="")      #adjust = ""未复权  ; "qfq"前复权;   "hfq" 后复权
        df = df.rename(columns={'日期': 'date', 
                                '股票代码': 'stock_id', 
                                '收盘': 'Close', 
                                '开盘': 'Open', 
                                '最高': 'High', 
                                '最低': 'Low', 
                                '成交量': 'Volume'})
        
        df.to_csv(self.file_name, header=True, index=False)
        df.to_excel(self.file_name,header=True,index=False)
    
    # 画K线图
    def testPandasKLine(self):
        #file_name = "./python/量化交易/data/demo_000001.csv"
        df = pd.read_csv(self.file_name)
        
        df['MA5'] = df['Close'].rolling(5).mean()
        df['MA10'] = df['Close'].rolling(10).mean()
        
        # fig = plt.figure()
        # axes =fig.add_subplot(111)
        
        # df.index = pd.to_datetime(df["date"])
        #df["date"] = pd.to_datetime(df["date"])
        
        df['date'] = pd.to_datetime(df['date'])
        df = df.set_index('date') 
        
        print(df)
        
        mpf.plot(
            df, 
            type='candle',
            style='yahoo',
            title='K线图示例',
            ylabel='价格',
            ylabel_lower='成交量',
            volume=True,
            mav=(5,10),
            show_nontrading=False)
        plt.show()
        
        # candlestick2_ochl(
        #     ax = axes,
        #     open = df["open"].value,
        #     close = df["close"].value,
        #     high = df["high"].value,
        #     low = df["low"].value,
        #     width = 0.75,
        #     colorup = "red",
        #     colordown = "green"
        #     )
        # plt.xticks(range(len(df.index.values)).df.index.values,ratation=30)
        # axes.grid(True)
        # plt.title("K-Line")
        # plt.show()
        
    def testKLineByVolume(self):
        # file_name = "./python/量化交易/data/demo_000001.csv"
        df = pd.read_csv(self.file_name)
        
        df = df[["date","Close","Open","High","Low","Volume"]]
        df["date"] = pd.to_datetime(df["date"])
        df = df.set_index("date")
        
        my_color = mpf.make_marketcolors(
            up = 'red',
            down = 'green',
            wick = 'i',
            volume = {'up':'red','down':'green'},
            ohlc = 'i'
        )
        
        my_style = mpf.make_mpf_style(
            marketcolors = my_color,
            gridaxis = 'both',
            gridstyle = '-.',
            rc = {'font.family':'STSong'}
        )
        
        mpf.plot(
            df,
            type = 'candle',
            title ='K-LineByVolume',
            ylabel = 'price',
            style = my_style,
            show_nontrading = False,
            volume = True,
            ylabel_lower = 'volume',
            datetime_format = '%Y-%m-%d',
            xrotation = 45,
            linecolor = '#00FF00',
            tight_layout = False
        )
        plt.show()
        
        
        
        

tp = TestPandasKLine()  
# tp.getData()
# tp.testPandasKLine()   
tp.testKLineByVolume()   