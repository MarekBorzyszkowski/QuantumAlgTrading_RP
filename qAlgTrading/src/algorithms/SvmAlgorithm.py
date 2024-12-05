import numpy as np
import pandas as pd
from qAlgTrading.src.algorithms.tradingAlgorithm import TradingAlgorithm
from sklearn.svm import SVC, SVR
from sklearn.preprocessing import StandardScaler

from qAlgTrading.src.constants import FEATURES

# https://github.com/772003pranav/Stock-Price-Prediction-using-LSTM-and-SVM

class SvmAlgorithm(TradingAlgorithm):
    def __init__(self):
        self.scaler = StandardScaler()
        self.model = SVR()
        self.history_data = None

    def train(self, historical_data):
        if 'Close' not in historical_data.columns:
            raise ValueError("Historical data must contain column: 'Close'")

        close_prices = historical_data['Close'].values

        X = self._prepare_features(close_prices)
        y = close_prices[len(close_prices) - len(X):]

        X_scaled = self.scaler.fit_transform(X)

        self.model.fit(X_scaled, y)

        self.history_data = historical_data

    def fit(self, historical_data):
        if 'Close' not in historical_data.columns:
            raise ValueError("Recent data must contain column: 'Close'")

        if len(historical_data) < 5:
            raise ValueError("Insufficient data for prediction.")

        close_prices = historical_data['Close'].values
        X = self._prepare_features_to_fit(close_prices)

        X_scaled = self.scaler.transform(X)

        return self.model.predict(X_scaled)[-1]

    def history(self):
        raise NotImplementedError

    def save(self, directory: str):
        raise NotImplementedError

    def load(self, directory: str):
        raise NotImplementedError

    def _prepare_features(self, close_prices):
        X = []
        for i in range(len(close_prices) - 5):
            X.append(close_prices[i:i + 5])
        return np.array(X)

    def _prepare_features_to_fit(self, close_prices):
        X = []
        for i in range(len(close_prices)):
            X.append(close_prices[i])
        return np.array(X).reshape(-1, 5)