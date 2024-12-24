from qAlgTrading.src.algorithms.TradingAlgorithm.TradingAlgorithm import TradingAlgorithm


class TestTradingAlgorithm(TradingAlgorithm):
    def __init__(self):
        self.a = 1

    def train(self, historical_data):
        return NotImplemented

    def fit(self, current_data, next_day_data):
        return NotImplemented

    def history(self):
        raise NotImplementedError

    def save(self, directory: str):
        raise NotImplementedError

    def load(self, directory: str):
        raise NotImplementedError
