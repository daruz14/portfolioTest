# Portfolio Test

## Task Description
Construct a simple Portfolio class that has a collection of Stocks and a "Profit" method that receives 2 dates and returns the profit of the Portfolio between those dates. Assume each Stock has a "Price" method that receives a date and returns its price.
Bonus Track: make the Profit method return the "annualized return" of the portfolio between the given dates.

## Project Description
The project is capable of generating random stocks data and associate with markets of stocks. In `main.py` file can find examples de how to use. Ej:

```python
  # Create two marketOfStocks only for the demo
  marketTechSmall = MarketOfStocks('marketTechSmall', ['CDK', 'HPE', 'DELL', 'HP', 'INTC'])
  # create own stockTickers in each market
  stockTickersSmall = ['CDK', 'HPE']
  # Create Portfolio
  portfolioSmall = Portfolio(stockTickersSmall, marketTechSmall)
  resultSmall = portfolioSmall.profit('2021-11-01', '2021-12-22')
  print('Portfolio Small Results:')
  print(dumps(resultSmall, sort_keys=True, indent=4))
```

## Basic Configuration
In file `basicVariables.py` are the basic variables to change execution in Portfolio:

```python
MIN_STOCK_PRICE = 200 #base of min price to generate stocks random prices

TOTAL_DAYS = 365 * 2 #total time of days to emulate portfolio

START_DATE = datetime.now().date() - timedelta(days=TOTAL_DAYS) #used it to generate historic data in random stocks prices
```

In file `main.py`are the example of Portfolio configuration.

## Run

Execute:
```bash
python main.py
```

## Return Format

When execute Portfolio profiot, it return the information with the following format:

```python
# Portfolio:
{
  "dataPerStockTicker": {
    "<stockTicker>": {
        "annalizedReturn": -0.44,
        "profit": -16
    },
    "<stockTicker>": {
        "annalizedReturn": 0.6,
        "profit": 13
    }
  },
  "totalAnnualizedReturn": -0.05, # Total AnnualizedReturn from all stocks in the Portfolio
  "totalProfit": -3 # Total Profit from all stocks in the Portfolio
}
```

## Assumptions

- Using price variance +-10 when generating random prices
- There is no API for this Fintual test