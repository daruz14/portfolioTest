from unicodedata import name
from stocks import Stocks

class MarketOfStocks():
  def __init__(self, name, stocksName):
    self.name = name
    self.setStocks(stocksName)
  
  def setStocks(self, stocksName):
    self.stocks = {tickerSymbol : Stocks(tickerSymbol) for tickerSymbol in stocksName}