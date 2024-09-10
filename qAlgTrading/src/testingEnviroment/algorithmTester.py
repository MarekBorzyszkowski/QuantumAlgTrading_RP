from qAlgTrading.src.constants import FEATURES


class AlgorithmTester:
    def __init__(self, initial_cash=10000):
        self.cash = initial_cash
        self.shares = 0
        self.portfolio_value = []

    def trade(self, price, decision):
        if decision == "buy" and self.cash >= price:
            self.shares += 1
            self.cash -= price
        elif decision == "sell" and self.shares > 0:
            self.shares -= 1
            self.cash += price

    def update_portfolio_value(self, current_price):
        total_value = self.cash + (self.shares * current_price)
        self.portfolio_value.append(total_value)

    def perform_test(self, algorithm, data):
        """
        Wykonuje test na zadanym algorytmie przy użyciu dostarczonych danych.

        :param algorithm: Obiekt będący instancją klasy dziedziczącej po TradingAlgorithm.
        :param data: Tablica dwuwymiarowa (numpy array) z wartościami akcji dla danego przedziału czasu.
                     Wiersze reprezentują różne dni, a kolumny różne aktywa.
        :return: Wyniki modelu w postaci tabeli (numpy array) zawierającej predykcje algorytmu.
        """
        for i in range(len(data) - 1):
            current_day = data.iloc[i][FEATURES[:-1]].values
            next_day = data.iloc[i + 1][FEATURES[:-1]].values
            current_price = data.iloc[i]['Close']
            decision = algorithm.fit(current_day, next_day)
            self.trade(current_price, decision)
            self.update_portfolio_value(current_price)

        return self.portfolio_value
