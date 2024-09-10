from qAlgTrading.src.algorithms.tradingAlgorithm import TradingAlgorithm
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


class PcaAlgorithm(TradingAlgorithm):
    def __init__(self, n_components=2):
        self.pca = PCA(n_components=n_components)
        self.scaler = StandardScaler()
        self.pca_fitted = False

    def train(self, historical_data):
        features = ['Open', 'High', 'Low', 'Volume']
        data = historical_data[features]
        scaled_data = self.scaler.fit_transform(data)
        self.pca.fit(scaled_data)
        self.pca_fitted = True

    def fit(self, current_data, next_day_data):
        if not self.pca_fitted:
            raise ValueError("Model PCA not trained.")

        current_scaled = self.scaler.transform([current_data])
        next_scaled = self.scaler.transform([next_day_data])

        current_pca = self.pca.transform(current_scaled)
        next_pca = self.pca.transform(next_scaled)

        if next_pca[0][0] > current_pca[0][0]:
            return "buy"
        else:
            return "sell"

    def history(self):
        raise NotImplementedError

    def save(self, directory: str):
        raise NotImplementedError

    def load(self, directory: str):
        raise NotImplementedError