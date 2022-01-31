from datetime import datetime


class Portfolio:
  def __init__(self, collectionOFStocks, marketOfStocks):
    self.collectionOFStocks = collectionOFStocks or {}
    self.marketOfStocks = marketOfStocks

  def stockTickerProfitBetweenDate(self, fromDate, endDate, stockTicker):
    return self.marketOfStocks.stocks[stockTicker].prices[endDate] - self.marketOfStocks.stocks[stockTicker].prices[fromDate]

  def annualizedRevenue(self, stockData):
    relativeRevenue = (stockData['finalValue'] - stockData['startValue'])  / stockData['startValue']
    
    fromDate = datetime.strptime(stockData['fromDate'], '%Y-%m-%d')
    endDate = datetime.strptime(stockData['endDate'], '%Y-%m-%d')
    years = endDate - fromDate

    porcentualTime = int(years.days) / 365

    annualizedRevenue = (((1 + relativeRevenue)**(1 / porcentualTime)) - 1) 
    return round(annualizedRevenue, 2)
  
  def stockTickerProfitAndAnnualizedReturn(self, stockTicker, fromDate, endDate):
    annalizedReturn = self.annualizedRevenue({
      'startValue': self.marketOfStocks.stocks[stockTicker].prices[fromDate],
      'finalValue': self.marketOfStocks.stocks[stockTicker].prices[endDate],
      'fromDate': fromDate,
      'endDate': endDate
    })
    return {
      'profit': self.stockTickerProfitBetweenDate(fromDate, endDate, stockTicker),
      'annalizedReturn': annalizedReturn
    }

  def profit(self, fromDate, endDate):
    initialCapital = 0
    finalCapital = 0
    stocksProfitAndAnnualizedReturn = {}
    for stockTicker in self.collectionOFStocks:
      stocksProfitAndAnnualizedReturn[stockTicker] = self.stockTickerProfitAndAnnualizedReturn(
        stockTicker,
        fromDate,
        endDate
      )
      initialCapital += self.marketOfStocks.stocks[stockTicker].prices[fromDate]
      finalCapital += self.marketOfStocks.stocks[stockTicker].prices[endDate]


    totalAnnualizedReturn = self.annualizedRevenue({
      'startValue': initialCapital,
      'finalValue': finalCapital,
      'fromDate': fromDate,
      'endDate': endDate
    })

    return {
      'totalAnnualizedReturn': totalAnnualizedReturn,
      'totalProfit': finalCapital - initialCapital,
      'dataPerStockTicker': stocksProfitAndAnnualizedReturn
    }