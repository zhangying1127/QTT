import numpy as np
import akshare as ak
import matplotlib.pyplot as plt

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


import os
os.environ["PYTHONIOENCODING"] = "utf-8"

import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    os.environ['PYTHONLEGACYWINDOWSFSENCODING'] = '1'

class MyPython:
    # ��ȡ�й�ƽ��ǰ��Ȩ��ʷ����
    def getData(self):
        df = ak.stock_zh_a_hist(symbol="601318", period="daily", 
            start_date="20090101", end_date="20090201", 
            adjust="")      #adjust = ""δ��Ȩ  ; "qfq"ǰ��Ȩ;   "hfq" ��Ȩ
        
        df.to_csv("./量化交易/data/demo.csv", header=False, index=False)
        df.to_excel("./量化交易/data/demo.xlsx")
        #df.to_csv("./量化交易/data/demo.csv")

    def testReadFile(self):
        #file_name = "C:\\zy_pw\\量化交易\data\\demo.csv"
        file_name = "./量化交易/data/demo.csv"
        end_price,volumn = np.loadtxt(
            fname = file_name,
            delimiter = ',',
            usecols = (2,6),
            unpack = True,
            encoding='utf-8'
        )
        print(end_price)
        print(volumn)

    def testMaxAndMin(self):
        file_name = "./量化交易/data/demo.csv"
        high_price,low_price = np.loadtxt(
                fname = file_name,
                delimiter = ',',
                usecols = (4,5),
                unpack = True
        )
        print("max_price = {}".format(high_price.max()))
        print("min_price = {}".format(low_price.min()))

    def testPtp(self):
        file_name = "./量化交易/data/demo.csv"
        high_price,low_price = np.loadtxt(
                fname = file_name,
                delimiter = ',',
                usecols = (4,5),
                unpack = True
        )
        print("max - min of high price : {}".format(np.ptp(high_price)))
        print("max - min of low price: {}".format(np.ptp(low_price)))
    def testAVG(self):
        file_name = "./量化交易/data/demo.csv"
        end_price,volumn = np.loadtxt(
            fname = file_name,
            delimiter = ',',
            usecols = (2,6),
            unpack = True
        )
        print("avg_price = {}".format(np.average(end_price)))
        print("VWAP = {}".format(end_price,weights = volumn))

    def testMedium(self):
        file_name = "./量化交易/data/demo.csv"
        end_price,volumn = np.loadtxt(
            fname = file_name,
            delimiter = ',',
            usecols = (2,6),
            unpack = True
        )
        print("median = {}".format(np.median(end_price)))

    def testVar(self):
        file_name = "./量化交易/data/demo.csv"
        end_price,volumn = np.loadtxt(
            fname = file_name,
            delimiter = ',',
            usecols = (2,6),
            unpack = True
        )
        print("var = {}".format(np.var(end_price)))
        print("var = {}".format(end_price.var()))




# �����Ʊ�����ʡ��겨���ʼ��²�����
# �������ǶԼ۸�䶯��һ�ֶ�������ʷ�����ʿ��Ը�����ʷ�۸����ݼ���ó���������ʷ������ʱ����Ҫ�õ�����������
# �겨���ʵ��ڶ��������ʵı�׼��������ֵ���ٳ��Խ����յ�ƽ������ͨ��������ȡ250��
# �²����ŵ��ڶ��������ʵı�׼��������ֵ���ٳ��Խ����յ�ƽ������ͨ��������ȡ12��

    def testVolatility(self):
        file_name = "./量化交易/data/demo.csv"
        end_price,volumn = np.loadtxt(
            fname = file_name,
            delimiter = ',',
            usecols = (2,6),
            unpack = True
        )
        log_return = np.diff(np.log(end_price))

        annual_volatility = log_return.std() / log_return.mean() * np.sqrt(250)

        mouthly_volatility = log_return.std() / log_return.mean() * np.sqrt(12)

        print("log_return = {}".format(log_return)) 
        print("annual_volatility = {}".format(annual_volatility)) 
        print("mouthly_volatility = {}".format(mouthly_volatility))

    def testSMA(self):
        file_name = "./量化交易/data/demo.csv"
        end_price = np.loadtxt(
            fname = file_name,
            delimiter = ',',
            usecols = (3),
            unpack = True
        )
        print(end_price)
        N = 5
        weights = np.ones(N) / N
        print(weights)
        sma = np.convolve(weights,end_price)[N-1:-N+1]
        print(sma)
        plt.plot(sma,linewidth=5)
        plt.show()
    
    def testEMA(self):
        file_name = "./量化交易/data/demo.csv"
        end_price = np.loadtxt(
            fname = file_name,
            delimiter = "," ,
            usecols = (3),
            unpack = True
        )
        print(end_price)
        N = 5
        weights = np.exp(np.linspace(-1,0,N))
        weights /=weights.sum()
        ema = np.convolve(weights,end_price)[N-1:-N+1]
        print(ema)

        t = np.arange(N-1,len(end_price))
        plt.plot(t,end_price[N-1:],lw=1.0)
        plt.plot(t,ema,lw=2.0)
        plt.show()
                 


mp = MyPython()
# mp.getData()
# mp.testReadFile()
# mp.testMaxAndMin()
# mp.testPtp()
# mp.testAVG()   
# mp.testMedium()    
# mp.testVar()
# mp.testVolatility() 

# mp.testSMA()
mp.testEMA()