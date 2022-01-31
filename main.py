from json import dumps
from portfolio import Portfolio
from marketOfStocks import MarketOfStocks

if __name__ == '__main__':
  # Create two marketOfStocks only for the demo
  marketTechSmall = MarketOfStocks('marketTechSmall', ['CDK', 'HPE', 'DELL', 'HP', 'INTC'])
  marketTechBig = MarketOfStocks('marketTechBig', ['TSLA', 'AAPL', 'AMZN', 'MSFT', 'NIO', 'NVDA', 'FB'])

  # create own stockTickers in each market
  stockTickersSmall = ['CDK', 'HPE']
  stockTickersBig = ['TSLA', 'AAPL', 'AMZN', 'MSFT']

  # Create Portfolio
  portfolioSmall = Portfolio(stockTickersSmall, marketTechSmall)
  portfolioBig = Portfolio(stockTickersBig, marketTechBig)

  resultSmall = portfolioSmall.profit('2021-11-01', '2021-12-22')
  resultBig = portfolioBig.profit('2021-11-01', '2021-12-22')

  print('Portfolio Small Results:')
  print(dumps(resultSmall, sort_keys=True, indent=4), '\n')
  print('Portfolio Big Results:')
  print(dumps(resultBig, sort_keys=True, indent=4))