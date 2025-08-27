import pandas as pd
import matplotlib.pyplot as plt

class TestKDJ():
    
    file_name = "./QTT/data/demo_000001.csv"
    
    def cal_kdj(self,df):
        low_list = df['Low'].rolling(9,min_periods=9).min()
        low_list.fillna(value=df['Low'].expanding().min(), inplace=True)
        high_list = df['High'].rolling(9,min_periods=9).max()
        high_list.fillna(value=df['High'].expanding().max(), inplace=True)
        rav = (df['Close'] - low_list) / (high_list - low_list) * 100
        df["K"] = rav.ewm(com=2).mean()
        df["D"] = df["K"].ewm(com=2).mean()
        df["J"] = 3.0 * df["K"] - 2.0 * df["D"]
        return df
    
    
    def test_KDJ(self):
        df = pd.read_csv(self.file_name)        
        df["date"] = pd.to_datetime(df["date"])
        
        df_kdj = self.cal_kdj(df)
        print(df_kdj)
        
        plt.figure()
        df_kdj['K'].plot(color='red',label='K')
        df_kdj['D'].plot(label='d', color='yellow')
        df_kdj['J'].plot(label='j', color='blue')
        plt.legend(loc='best')
        
        major_index = df_kdj.index[df_kdj.index]
        major_xids = df_kdj["date"][df_kdj.index]
        plt.xticks(major_index, major_xids)
        plt.setp(plt.gca().get_xticklabels(),rotation=30)
        plt.grid(linestyle='-.')
        
        plt.title("KDJ指标")
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus']=False
        
        plt.show()
        
tk = TestKDJ()
tk.test_KDJ()      
             
        