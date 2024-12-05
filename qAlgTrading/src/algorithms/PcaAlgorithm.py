from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression

from qAlgTrading.src.algorithms.tradingAlgorithm import TradingAlgorithm
from qAlgTrading.src.constants import FEATURES

# po prostu stąd: https://stackoverflow.com/questions/41866841/using-pca-on-linear-regression

class PcaAlgorithm(TradingAlgorithm):
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.pca = PCA(n_components=n_components)
        self.model = LinearRegression()
        self.history_data = None

    def train(self, historical_data):
        if not set(FEATURES).issubset(historical_data.columns):
            raise ValueError(f"Historical data must contain columns: {FEATURES}")

        X = historical_data[FEATURES[:-1]].values
        y = historical_data['Close'].values

        X_reduced = self.pca.fit_transform(X)

        self.model.fit(X_reduced, y)

        self.history_data = historical_data

    def fit(self, historical_data):
        if not set(FEATURES).issubset(historical_data.columns):
            raise ValueError(f"Recent data must contain columns: {FEATURES}")

        if len(historical_data) < len(FEATURES):
            raise ValueError("Insufficient data for prediction.")

        X = historical_data[FEATURES[:-1]].values

        X_reduced = self.pca.transform(X)

        return self.model.predict(X_reduced)[-1]

    def history(self):
        raise NotImplementedError

    def save(self, directory: str):
        raise NotImplementedError

    def load(self, directory: str):
        raise NotImplementedError