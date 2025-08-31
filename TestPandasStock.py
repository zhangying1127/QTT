import pandas as pd
import akshare as ak


class TestPandasStock:
    def getData(self):
        df = ak.stock_zh_a_hist(
            symbol="000001", 
            period="daily", 
            start_date="20090106", 
            end_date="20090206", 
            adjust="")      #adjust = ""未复权  ; "qfq"前复权;   "hfq" 后复权
        df = df.rename(columns={'日期': 'date', 
                                '股票代码': 'stock_id', 
                                '收盘': 'close', 
                                '开盘': 'open', 
                                '最高': 'high', 
                                '最低': 'low', 
                                '成交量': 'volumn'})
        
        df.to_csv("./QTT/data/demo000001.csv", header=True, index=False)
        df.to_excel("./QTT/data/demo000001.xlsx",header=True,index=False)
          
    
    def testReadFile(self):
        file_name = "./QTT/data/demo000001.csv"
        df = pd.read_csv(file_name)
        
        print(df.info())
        print("----------------")
        print(df.describe())
        
    def testTime(self):
        file_name = "./QTT/data/demo000001.csv"
        df = pd.read_csv(file_name)
        # df.columns = ["date","stock_id","close","open","high","low","volumn"]
        
        df["date"] = pd.to_datetime(df["date"])
        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month
        
        print(df)
        
    def testCloseMin(self):
        file_name = "./QTT/data/demo000001.csv"
        df = pd.read_csv(file_name)
        # df.columns = ["date","stock_id","close","open","high","low","volumn"]
        
        print("""close min : {}""".format(df["close"].min()))
        print("""close min index : {}""".format(df["close"].idxmin()))
        print("""close min frame : \n{}""".format(df.loc[df["close"].idxmin()]))
    
    def testMean(self):
        file_name = "./QTT/data/demo000001.csv"
        df = pd.read_csv(file_name)
        
        df["date"] = pd.to_datetime(df["date"])
        df["month"] = df["date"].dt.month
        
        print("""month close mean : {}""".format(df.groupby("month")["close"].mean()))
        print("""month open mean : {}""".format(df.groupby("month")["open"].mean()))
    
    def testRipples_ratio(self):
        file_name = "./QTT/data/demo000001.csv"
        df = pd.read_csv(file_name)
        
        df["date"] = pd.to_datetime(df["date"])
        
        df["rise"] = df["close"].diff()
        df["rise_ratio"] = df["rise"] / df.shift(-1)["close"]
        
        print(df)
            
            


tp = TestPandasStock()
tp.getData()
tp.testReadFile()
tp.testTime()

tp.testCloseMin()

tp.testMean()
tp.testRipples_ratio()