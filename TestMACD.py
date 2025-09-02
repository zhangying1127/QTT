import pandas as pd
from unittest import TestCase
import matplotlib.pyplot as plt

class TestMACD(TestCase):
    def cal_macd(self,df,fastperiod=12,slowperiod=26,signalperoid=9):
        ewma12 = df['Close'].ewm(span=fastperiod,adjust=False).mean()
        ewma26 = df['Close'].ewm(span=slowperiod,adjust=False).mean()
        df["DIF"] = ewma12 - ewma26
        df["DEA"] = df["DIF"].ewm(span=signalperoid,adjust=False).mean()
        df["MACD"] = 2 * (df["DIF"] - df["DEA"])     
        df["BAR"]  = df["MACD"]
        return df
    
    def test_MACD(self):    
        file_name = "./QTT/data/demo_000001.csv"
        df = pd.read_csv(file_name)
        df["date"] = pd.to_datetime(df["date"])
        
        df_macd = self.cal_macd(df)
        print(df_macd)
        
        plt.figure()
        df_macd['DEA'].plot(color='red',label='DEA')
        df_macd['DIF'].plot(color='blue',label='DIF')
        plt.legend(loc = 'best')
        
        pos_bar = []
        pos_index = []
        neg_bar = []    
        neg_index = []
        
        for index,row in df_macd.iterrows():
            if row["BAR"] >= 0:
                pos_bar.append(row["BAR"])
                pos_index.append(index)
                # neg_bar.append(0)
                # neg_index.append(index)
            else:
                neg_bar.append(row["BAR"])
                neg_index.append(index)
                # pos_bar.append(0)
                # pos_index.append(index)
        # 大于0用红色表示
        plt.bar(pos_index,pos_bar,width=0.5,color='red')
        # 小于0用绿色表示
        plt.bar(neg_index,neg_bar,width=0.5,color='green')
        
        major_index = df_macd.index[df_macd.index]
        major_xids = df_macd["date"][df_macd.index]
        plt.xticks(major_index, major_xids)
        plt.setp(plt.gca().get_xticklabels(),rotation=30)
        plt.grid(linestyle='-.')
        plt.title("000001平安银行MACD指标")
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus']=False
        
        plt.show()
        
        
        
        
        
        
        
tm = TestMACD()
tm.test_MACD()
       

    
    