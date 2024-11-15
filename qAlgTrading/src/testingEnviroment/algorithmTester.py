from tqdm import tqdm

from qAlgTrading.src.constants import FEATURES
import pandas as pd


class AlgorithmTester:
    def __init__(self, initial_cash=10000):
        self.cash = initial_cash
        self.shares = 0

    def trade(self, price, decision):
        if decision == "buy" and self.cash >= price:
            self.shares += 1
            self.cash -= price
        elif decision == "sell" and self.shares > 0:
            self.shares -= 1
            self.cash += price

    def update_portfolio_value(self, current_price):
        total_value = self.cash + (self.shares * current_price)
        return total_value

    def perform_test(self, algorithm, data):
        """
        Wykonuje test na zadanym algorytmie przy użyciu dostarczonych danych.

        :param algorithm: Obiekt będący instancją klasy dziedziczącej po TradingAlgorithm.
        :param data: Tablica dwuwymiarowa (numpy array) z wartościami akcji dla danego przedziału czasu.
                     Wiersze reprezentują różne dni, a kolumny różne aktywa.
        :return: Wyniki modelu w postaci tabeli (numpy array) zawierającej predykcje algorytmu.
        """
        portfolio_value = []
        for i in tqdm(range(len(data) - 1)):
            current_day = pd.DataFrame(data.iloc[i][FEATURES]).transpose()
            next_day = pd.DataFrame(data.iloc[i + 1][FEATURES]).transpose()
            current_price = data.iloc[i]['Close']
            decision = algorithm.fit(current_day, next_day)
            self.trade(current_price, decision)
            portfolio_value.append(self.update_portfolio_value(current_price))

        return portfolio_value
