import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression

from qAlgTrading.src.algorithms.tradingAlgorithm import TradingAlgorithm


class PcaAlgorithm(TradingAlgorithm):
    def __init__(self, history_length=5):
        self.history_length = history_length
        self.pca = PCA(n_components=history_length)
        self.model = LinearRegression()
        self.history_data = None

    def train(self, historical_data):
        if 'Close' not in historical_data.columns:
            raise ValueError("Historical data must contain column: 'Close'")

        close_prices = historical_data['Close'].values

        X = self._prepare_features(close_prices)
        y = close_prices[self.history_length:]

        X_reduced = self.pca.fit_transform(X)

        self.model.fit(X_reduced, y)

        self.history_data = historical_data

    def fit(self, historical_data):
        if 'Close' not in historical_data.columns:
            raise ValueError("Recent data must contain column: 'Close'")

        if len(historical_data) < self.history_length: #Do sprawdzenia
            raise ValueError("Insufficient data for prediction.")

        X = self._prepare_features_to_fit(historical_data['Close'].values) #Do sprawdzenia

        X_reduced = self.pca.transform(X)

        return self.model.predict(X_reduced).item()

    def history(self):
        raise NotImplementedError

    def save(self, directory: str):
        raise NotImplementedError

    def load(self, directory: str):
        raise NotImplementedError

    def name(self):
        return "PCA"

    def _prepare_features(self, close_prices):
        X = []
        for i in range(len(close_prices) - self.history_length):
            X.append(close_prices[i:i + self.history_length])
        return np.array(X)

    def _prepare_features_to_fit(self, close_prices):
        X = []
        for i in range(len(close_prices)):
            X.append(close_prices[i])
        return np.array(X).reshape(-1, self.history_length)