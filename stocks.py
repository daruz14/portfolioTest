import random
from datetime import timedelta
from basicVariables import *


class Stocks():
  '''
  Stock only has date and price and
  the stocks are stored in dictionary prices
  price format -> {date: price, ...}
  '''

  def __init__(self, tickerSymbol):
    self.tickerSymbol = tickerSymbol
    self.prices = {}
    self.generateRandomPrices()

  def generateRandomPrices(self):
    lastDayPrice = MIN_STOCK_PRICE
    for dayNumber in range(TOTAL_DAYS):
      self.prices[str(START_DATE + timedelta(days=dayNumber))] = random.randint(
        lastDayPrice - 10,
        lastDayPrice + 10
      )
  