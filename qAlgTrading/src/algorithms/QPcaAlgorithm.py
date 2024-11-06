from qAlgTrading.src.algorithms.qpca.QPCA import QPCA
from qAlgTrading.src.algorithms.tradingAlgorithm import TradingAlgorithm
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from qAlgTrading.src.constants import FEATURES


class QPcaAlgorithm(TradingAlgorithm):
    def __init__(self):
        self.qpca = QPCA()
        self.scaler = StandardScaler()

    def train(self, historical_data):
        features = ['Open', 'High', 'Low', 'Close', 'Volume']
        data = historical_data[FEATURES]
        scaled_data = self.scaler.fit_transform(data)
        self.qpca.fit(scaled_data)

    def fit(self, current_data, next_day_data):
        current_scaled = self.scaler.transform(current_data)
        next_scaled = self.scaler.transform(next_day_data)

        current_pca = self.qpca.transform(current_scaled)
        next_pca = self.qpca.transform(next_scaled)

        if next_pca[0] > current_pca[0]:
            return "buy"
        else:
            return "sell"

    def history(self):
        raise NotImplementedError

    def save(self, directory: str):
        raise NotImplementedError

    def load(self, directory: str):
        raise NotImplementedError