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

    def fit(self, historical_data):
        return NotImplemented

    def history(self):
        raise NotImplementedError

    def save(self, directory: str):
        raise NotImplementedError

    def load(self, directory: str):
        raise NotImplementedError