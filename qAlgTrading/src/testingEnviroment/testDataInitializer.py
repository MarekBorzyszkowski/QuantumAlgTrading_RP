import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from qAlgTrading.src.algorithms.PcaAlgorithm import PcaAlgorithm
from qAlgTrading.src.testingEnviroment.algorithmTester import AlgorithmTester
from qAlgTrading.src.testingEnviroment.resultsPresenter import ResultPresenter

start_date = '2005-04-02'  # data nieprzypadkowa
num_days = 2137

file_path = '../../../data/sp500/components/AAPL.csv'
data = pd.read_csv(file_path)
filtered_data = data[data['Date'] >= start_date].head(num_days)

pca_algorithm = PcaAlgorithm(n_components=2)
train_data = filtered_data.iloc[:int(0.7 * len(filtered_data))]
test_data = filtered_data.iloc[int(0.7 * len(filtered_data)):]
pca_algorithm.train(train_data)

tester = AlgorithmTester()
results = tester.perform_test(pca_algorithm, test_data)

results = np.array([results])

result_presenter = ResultPresenter()
result_presenter.print_results_single_chart(results)
result_presenter.print_results_separate_chart(results)
