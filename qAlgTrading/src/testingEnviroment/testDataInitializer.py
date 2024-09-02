import numpy as np
import pandas as pd

from qAlgTrading.src.algorithms.classicAlgorithm import ClassicAlgorithm
from qAlgTrading.src.algorithms.quantumAlgorithm import QuantumAlgorithm
from qAlgTrading.src.testingEnviroment.algorithmTester import AlgorithmTester
from qAlgTrading.src.testingEnviroment.resultsPresenter import ResultPresenter

startDate = '2005-04-02'  # data nieprzypadkowa
numDays = 14

wig20 = pd.read_csv('../../../data/wig20/WIG20.csv')
filteredWig20 = wig20[wig20['Date'] >= startDate].head(numDays)
wig20Assets = filteredWig20[['Open', 'High', 'Low', 'Close']].values
wig20AssetsArray = np.array(wig20Assets)

sp500 = pd.read_csv('../../../data/sp500/^SPX.csv')
filteredSp500 = sp500[sp500['Date'] >= startDate].head(numDays)
sp500Assets = filteredSp500[['Open', 'High', 'Low', 'Close']].values
sp500AssetsArray = np.array(sp500Assets)

classicAlgorithm = ClassicAlgorithm()
quantumAlgorithm = QuantumAlgorithm()

tester = AlgorithmTester()
tester.perform_test(classicAlgorithm, wig20AssetsArray)
tester.perform_test(quantumAlgorithm, sp500AssetsArray)

results = np.array([wig20AssetsArray, sp500AssetsArray])

resultPresenter = ResultPresenter()
resultPresenter.print_results_single_chart(results)
resultPresenter.print_results_separate_chart(results)
