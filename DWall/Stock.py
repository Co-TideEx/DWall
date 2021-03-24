from tkinter import *
import datetime
#import matplotlib.pyplot as plt
#from matplotlib import style
#import pandas as pd
import pandas_datareader.data as web
# pip install pandas, pandas-datareader, matplotlib, beautifulsoup4, scikit-learn

window = Tk()

def submission():
    print(content.get())

Label(window, text="Start Date").grid(row=0)
Label(window, text="End Date").grid(row=1)

content = StringVar()
e1 = Entry(window, textvariable=content).grid(row=0, column=1)
e2 = Entry(window).grid(row=1, column=1)

Button(window, text='Submit', command=submission).grid(row=3, column=1, sticky=W, pady=4)



start = datetime.datetime(2021, 3, 1)
end = datetime.datetime.now()
df = web.DataReader("TSLA", 'yahoo', start, end)

#df.to_csv('tsla.csv')


#stockInfo = Label(window, "shit")
#stockInfo.pack()


window.mainloop()