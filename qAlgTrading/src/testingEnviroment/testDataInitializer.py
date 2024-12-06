import numpy as np
import pandas as pd


from qAlgTrading.src.algorithms.PcaAlgorithm import PcaAlgorithm
from qAlgTrading.src.algorithms.QPcaAlgorithm import QPcaAlgorithm
from qAlgTrading.src.algorithms.QSvmAlgorithm import QSvmAlgorithm
from qAlgTrading.src.algorithms.SvmAlgorithm import SvmAlgorithm
from qAlgTrading.src.testingEnviroment.algorithmTester import AlgorithmTester
from qAlgTrading.src.testingEnviroment.resultsPresenter import ResultPresenter

start_date = '2003-01-01'
num_days = 1000
train_data_precent = 0.7

file_path = '../../../data/wig20/components/PKO.csv'
data = pd.read_csv(file_path)
filtered_data = data[data['Date'] >= start_date].head(num_days)


print("Start of algorithm initialization")
pca_algorithm = PcaAlgorithm()
print("PCA initialized")
svm_algorithm = SvmAlgorithm()
print("SVM initialized")
qpca_algorithm = QPcaAlgorithm()
print("QPCA initialized")
qsvm_algorithm = QSvmAlgorithm()
print("QSVM initialized")
print("End of initialization")
algorithms = [pca_algorithm, svm_algorithm, qpca_algorithm, qsvm_algorithm]

for algorithm in algorithms:
    algorithm.name()

# train_data = filtered_data.iloc[:int(train_data_precent * len(filtered_data))]
# test_data = filtered_data.iloc[int(train_data_precent * len(filtered_data)):]
# print("Training initialized")
# for algorithm in algorithms:
#     algorithm.train(train_data)
# print("Training finished")
#
# algorithm_tester = AlgorithmTester()
# algorithm_results = []
# print("Predictions started")
# for algorithm in algorithms:
#     algorithm_results.append(algorithm_tester.perform_test(algorithm, test_data))
# print("Predictions finished")
#
# test_data_closed = test_data.iloc[5:]['Close']
#
# results = np.add(np.array([test_data_closed]), algorithm_results)
# results_diff = np.array([test_data_closed - algorithm_result for algorithm_result in algorithm_results])
#
# result_presenter = ResultPresenter()
# result_presenter.print_results_single_chart(results)
# # result_presenter.print_results_separate_chart(results)
# result_presenter.print_results_single_chart(results_diff)
