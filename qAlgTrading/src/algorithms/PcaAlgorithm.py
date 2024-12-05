import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression

from qAlgTrading.src.algorithms.tradingAlgorithm import TradingAlgorithm
from qAlgTrading.src.constants import FEATURES

# po prostu stąd: https://stackoverflow.com/questions/41866841/using-pca-on-linear-regression

class PcaAlgorithm(TradingAlgorithm):
    def __init__(self, n_components=5):
        self.n_components = n_components
        self.pca = PCA(n_components=n_components)
        self.model = LinearRegression()
        self.history_data = None

    def train(self, historical_data):
        if 'Close' not in historical_data.columns:
            raise ValueError("Historical data must contain column: 'Close'")

        close_prices = historical_data['Close'].values

        X = self._prepare_features(close_prices)
        y = close_prices[self.n_components:]

        X_reduced = self.pca.fit_transform(X)

        self.model.fit(X_reduced, y)

        self.history_data = historical_data

    def fit(self, historical_data):
        if 'Close' not in historical_data.columns:
            raise ValueError("Recent data must contain column: 'Close'")

        if len(historical_data) < self.n_components + 1: #Do sprawdzenia
            raise ValueError("Insufficient data for prediction.")

        X = self._prepare_features(historical_data['Close'].values) #Do sprawdzenia

        X_reduced = self.pca.transform(X)

        return self.model.predict(X_reduced)[-1]

    def history(self):
        raise NotImplementedError

    def save(self, directory: str):
        raise NotImplementedError

    def load(self, directory: str):
        raise NotImplementedError

    def _prepare_features(self, close_prices):
        X = []
        for i in range(len(close_prices) - self.n_components):
            X.append(close_prices[i:i + self.n_components])
        return np.array(X)