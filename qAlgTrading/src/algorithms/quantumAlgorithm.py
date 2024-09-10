from qAlgTrading.src.algorithms.tradingAlgorithm import TradingAlgorithm


class QuantumAlgorithm(TradingAlgorithm):

    def __init__(self):
        pass

    def train(self, historical_data):
        raise NotImplementedError

    def fit(self, current_data, next_day_data):
        raise NotImplementedError

    def history(self):
        raise NotImplementedError

    def save(self, directory: str):
        raise NotImplementedError

    def load(self, directory: str):
        raise NotImplementedError