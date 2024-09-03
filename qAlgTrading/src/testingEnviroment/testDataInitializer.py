import numpy as np
import pandas as pd

from qAlgTrading.src.algorithms.classicAlgorithm import ClassicAlgorithm
from qAlgTrading.src.algorithms.quantumAlgorithm import QuantumAlgorithm
from qAlgTrading.src.testingEnviroment.algorithmTester import AlgorithmTester
from qAlgTrading.src.testingEnviroment.resultsPresenter import ResultPresenter

start_date = '2005-04-02'  # data nieprzypadkowa
num_days = 14

wig20 = pd.read_csv('../../../data/wig20/WIG20.csv')
filtered_wig20 = wig20[wig20['Date'] >= start_date].head(num_days)
wig20_assets = filtered_wig20[['Open', 'High', 'Low', 'Close']].values
wig20_assets_array = np.array(wig20_assets)

sp500 = pd.read_csv('../../../data/sp500/^SPX.csv')
filtered_sp500 = sp500[sp500['Date'] >= start_date].head(num_days)
sp500_assets = filtered_sp500[['Open', 'High', 'Low', 'Close']].values
sp500_assets_array = np.array(sp500_assets)

classic_algorithm = ClassicAlgorithm()
quantum_algorithm = QuantumAlgorithm()

tester = AlgorithmTester()
tester.perform_test(classic_algorithm, wig20_assets_array)
tester.perform_test(quantum_algorithm, sp500_assets_array)

results = np.array([wig20_assets_array, sp500_assets_array])

result_presenter = ResultPresenter()
result_presenter.print_results_single_chart(results)
result_presenter.print_results_separate_chart(results)
