from qAlgTrading.src.algorithms.tradingAlgorithm import TradingAlgorithm
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from qAlgTrading.src.constants import FEATURES


class PcaAlgorithm(TradingAlgorithm):
    def __init__(self, n_components=2):
        self.pca = PCA(n_components=n_components)
        self.scaler = StandardScaler()
        self.pca_fitted = False

    def train(self, historical_data):
        data = historical_data[FEATURES]
        scaled_data = self.scaler.fit_transform(data)
        self.pca.fit(scaled_data)
        self.pca_fitted = True

    def fit(self, historical_data):
        return NotImplementedError

    def history(self):
        raise NotImplementedError

    def save(self, directory: str):
        raise NotImplementedError

    def load(self, directory: str):
        raise NotImplementedError