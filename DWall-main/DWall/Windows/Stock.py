from tkinter import *
import datetime
#import matplotlib.pyplot as pltyy
import pandas_datareader.data as web
#pip install pandas, pandas-datareader, matplotlib, beautifulsoup4, scikit-learn


start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
df = web.DataReader("TSLA", 'yahoo', start, end)

#stockInfo = Label(df.head)
#stockInfo.pack()

print(df.head)

