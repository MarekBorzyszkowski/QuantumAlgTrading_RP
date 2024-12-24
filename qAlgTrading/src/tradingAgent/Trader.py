import abc

class Trader(metaclass=abc.ABC):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'actUponPrediction') and
                callable(subclass.actUponPrediction) and
                hasattr(subclass, 'currentPortfolioValue') and
                callable(subclass.currentPortfolioValue) and
                hasattr(subclass, 'currentTraderValue') and
                callable(subclass.currentTraderValue) and
                hasattr(subclass, 'currentCapitalValue') and
                callable(subclass.currentCapitalValue)
                or NotImplemented)

    @abc.abstractmethod
    def actUponPrediction(self, historical_data, prediction):
        raise NotImplemented

    @abc.abstractmethod
    def currentPortfolioValue(self, stock_price):
        raise NotImplemented

    @abc.abstractmethod
    def currentTraderValue(self, stock_price):
        raise NotImplemented

    @abc.abstractmethod
    def currentCapitalValue(self):
        raise NotImplemented

    # def trade(self, price, decision):
    #     if decision == "buy" and self.cash >= price:
    #         self.shares += 1
    #         self.cash -= price
    #     elif decision == "sell" and self.shares > 0:
    #         self.shares -= 1
    #         self.cash += price
    #
    # def update_portfolio_value(self, current_price):
    #     total_value = self.cash + (self.shares * current_price)
    #     return total_value
