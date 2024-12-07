import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

from .tradingAlgorithm import TradingAlgorithm


class SvmAlgorithm(TradingAlgorithm):
    def __init__(self, history_length=5, kernel='rbf'):
        self.scaler_X = StandardScaler()
        self.scaler_Y = StandardScaler()
        self.model = SVR(kernel=kernel)
        self.history_data = None
        self.history_length = history_length

    def train(self, historical_data):
        if 'Close' not in historical_data.columns:
            raise ValueError("Historical data must contain column: 'Close'")

        close_prices = historical_data['Close'].values

        X = self._prepare_features(close_prices)
        Y = [[element] for element in close_prices[self.history_length:]]

        X_scaled = self.scaler_X.fit_transform(X)
        Y_scaled = self.scaler_Y.fit_transform(Y)

        self.model.fit(X_scaled, Y_scaled)

        self.history_data = historical_data

    def fit(self, historical_data):
        if 'Close' not in historical_data.columns:
            raise ValueError("Recent data must contain column: 'Close'")

        if len(historical_data) < self.history_length:
            raise ValueError("Insufficient data for prediction.")

        close_prices = historical_data['Close'].values
        X = self._prepare_features_to_fit(close_prices)

        X_scaled = self.scaler_X.transform(X)

        return self.scaler_Y.inverse_transform([self.model.predict(X_scaled)]).item()

    def history(self):
        raise NotImplementedError

    def save(self, directory: str):
        raise NotImplementedError

    def load(self, directory: str):
        raise NotImplementedError

    def name(self):
        return "Svm"

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
