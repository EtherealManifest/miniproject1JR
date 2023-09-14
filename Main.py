# INF 601 Advanced Python
# Jacob Richmond
# Mini Project 1
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import copy
import pprint

#Added a phantom library to commit again
'''
(5/5 points) Initial comments with your name, class and project at the top of your .py file.
(5/5 points) Proper import of packages used.
'''

#(20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock
#tickers for the last 10 trading days.

# Apple = APPL
# Microsoft = MSFT
stocks = ["MSFT", "APPL", "GME", "META", "NTDOY"]



#loop through all the Tickers and pull their data
#get all stack info

#This method goes through and returns a list of all ofthe tickers closing prices for the
#last ten days and returns them in a list
def get_closing(Tick):
    stock = yf.Ticker(Tick)

    hist = stock.history(period = "10d")


    closingList = []

    for price in hist["Close"]:
        closingList.append(price)
    return closingList


#create empty list for the closing prices of all stocks

msft_closing = np.array(get_closing("MSFT"))
appl_closing = np.array(get_closing("AAPL"))
gme_closing = np.array(get_closing("GME"))
meta_closing = np.array(get_closing("META"))
ntdoy_closing = np.array(get_closing("NTDOY"))

for stock in stocks:
    stockClosing = np.array(get_closing(stock))
    days = list(range(1, len(stockClosing) + 1))

    #THis plots the graph, then we need to set our x axis min and max
    #set labels for the graph
    prices = get_closing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    plt.title("The Closing Prices for" + stock)
    plt.xlabel("Days")
    plt.ylabel("Closing Price")
    plt.axis([10,1, low_price-2, high_price + 2])
    #show the graph
    plt.plot(days, stockClosing)

plt.show()



#(10/10 points) Store this information in a list that you will convert to a ndarray in NumPy.

#(10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the

#documentation for matplotlib. At minimum it just needs to show 10 data points.

#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the

#project should save these when it executes. You may want to add this folder to your .gitignore file.

#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!

#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt

#file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the

# terminal prompt.

#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the

#pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.
