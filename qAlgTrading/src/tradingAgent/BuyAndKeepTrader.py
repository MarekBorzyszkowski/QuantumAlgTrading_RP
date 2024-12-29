from .Trader import Trader
from math import floor


class BuyAndKeepTrader(Trader):
    def __init__(self, initial_capital, max_percentage_of_portfolio_in_one_trade, number_of_stocks=0):
        self.capital = initial_capital
        self.max_percentage_of_value_in_one_trade = max_percentage_of_portfolio_in_one_trade
        self.number_of_stocks = number_of_stocks

    def actUponPrediction(self, historical_data, prediction):
        number_of_stocks_to_trade = self.calc_number_of_stock_to_trade(historical_data)
        if historical_data < prediction:
            max_stock_from_capital =  floor(self.capital/historical_data)
            number_of_stocks_can_trade = min(max_stock_from_capital, number_of_stocks_to_trade)
            self.number_of_stocks += number_of_stocks_can_trade
            self.capital -= number_of_stocks_can_trade * historical_data

    def calc_number_of_stock_to_trade(self, historical_data):
        return floor(self.currentTraderValue(historical_data) / historical_data * self.max_percentage_of_value_in_one_trade)

    def currentPortfolioValue(self, stock_price):
        return stock_price * self.number_of_stocks

    def currentTraderValue(self, stock_price):
        return self.currentPortfolioValue(stock_price) + self.capital

    def currentCapitalValue(self):
        return self.capital

    def name(self):
        return f"BuyAndKeepTrader: {self.max_percentage_of_value_in_one_trade*100}%"