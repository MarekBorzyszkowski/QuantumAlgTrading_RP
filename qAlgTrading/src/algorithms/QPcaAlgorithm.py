import os
import pickle

import numpy as np

from .TradingAlgorithm import TradingAlgorithm
from sklearn.decomposition import KernelPCA
from sklearn.linear_model import LinearRegression
from qiskit_machine_learning.kernels import FidelityQuantumKernel


class QPcaAlgorithm(TradingAlgorithm):
    def __init__(self, history_length=5):
        self.history_length = history_length
        self.qpca = KernelPCA(n_components=history_length, kernel='precomputed')
        self.kernel = FidelityQuantumKernel()
        self.model = LinearRegression()
        self.history_data = None
        self.train_X = None
        self.X_reduced = None

    def train(self, historical_data):
        if 'Close' not in historical_data.columns:
            raise ValueError("Historical data must contain column: 'Close'")

        close_prices = historical_data['Close'].values

        X = self._prepare_features(close_prices)
        self.train_X = X
        y = close_prices[self.history_length:]
        print("Start matrix_train_prep")
        matrix_train = self.kernel.evaluate(x_vec=X)
        print("Start qpca fit transform")
        X_reduced = self.qpca.fit_transform(matrix_train)
        print("Start model fit")
        self.model.fit(X_reduced, y)
        self.X_reduced = X_reduced
        self.history_data = historical_data

    def fit(self, historical_data):
        if 'Close' not in historical_data.columns:
            raise ValueError("Recent data must contain column: 'Close'")

        if len(historical_data) < self.history_length: #Do sprawdzenia
            raise ValueError("Insufficient data for prediction.")

        X = self._prepare_features_to_fit(historical_data['Close'].values) #Do sprawdzenia
        matrix_test = self.kernel.evaluate(x_vec=X, y_vec=self.train_X)
        X_reduced = self.qpca.transform(matrix_test)

        return self.model.predict(X_reduced).item()

    def history(self):
        return self.history_data

    def save(self, directory: str):
        with open(os.path.join(directory, "qpca.pkl"), "wb") as f:
            pickle.dump(self.qpca, f)

        with open(os.path.join(directory, "qpca_kernel.pkl"), "wb") as f:
            pickle.dump(self.kernel, f)

        with open(os.path.join(directory, "qpca_model.pkl"), "wb") as f:
            pickle.dump(self.model, f)

        with open(os.path.join(directory, "qpca_train_X.pkl"), "wb") as f:
            pickle.dump(self.train_X, f)

    def load(self, directory: str):
        with open(os.path.join(directory, "qpca.pkl"), "rb") as f:
            self.qpca = pickle.load(f)

        with open(os.path.join(directory, "qpca_kernel.pkl"), "rb") as f:
            self.kernel = pickle.load(f)

        with open(os.path.join(directory, "qpca_model.pkl"), "rb") as f:
            self.model = pickle.load(f)

        with open(os.path.join(directory, "qpca_train_X.pkl"), "rb") as f:
            self.train_X = pickle.load(f)

    def name(self):
        return "QPCA"

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