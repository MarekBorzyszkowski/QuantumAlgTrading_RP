import pandas as pd
from qAlgTrading.src.algorithms.tradingAlgorithm import TradingAlgorithm
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

from qAlgTrading.src.constants import FEATURES


class SvmAlgorithm(TradingAlgorithm):
    def __init__(self, kernel='linear'):
        self.svm = SVC(kernel=kernel)
        self.scaler = StandardScaler()
        self.svm_fitted = False
        self.labels = None
        self.features = None

    def set_labels(self, labels):
        self.labels = labels

    def train(self, historical_data):
        if self.labels is None:
            self.labels = self.prepare_labels(historical_data)

        features = ['Open', 'High', 'Low', 'Volume']
        data = historical_data[FEATURES]
        self.features = FEATURES
        scaled_data = self.scaler.fit_transform(data)

        self.svm.fit(scaled_data, self.labels)
        self.svm_fitted = True

    def fit(self, current_data, next_day_data):
        if not self.svm_fitted:
            raise ValueError("Model SVM not trained.")

        current_scaled = self.scaler.transform(current_data)
        next_scaled = self.scaler.transform(next_day_data)

        current_prediction = self.svm.predict(current_scaled)
        next_prediction = self.svm.predict(next_scaled)
        if next_prediction[0] > current_prediction[0]:
            return "buy"
        else:
            return "sell"

    def history(self):
        raise NotImplementedError

    def save(self, directory: str):
        raise NotImplementedError

    def load(self, directory: str):
        raise NotImplementedError

    def prepare_labels(self, historical_data):
        labels = []
        for i in range(0, len(historical_data)):
            if historical_data['Close'].iloc[i] > historical_data['Close'].iloc[i - 1]:
                labels.append(1)  # Kupno
            elif historical_data['Close'].iloc[i] < historical_data['Close'].iloc[i - 1]:
                labels.append(-1)  # Sprzedaż
            else:
                labels.append(0)  # Brak akcji (lub neutralne)
        return labels