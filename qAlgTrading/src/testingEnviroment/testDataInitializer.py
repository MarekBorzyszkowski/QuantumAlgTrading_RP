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

train_data = filtered_data.iloc[:int(train_data_precent * len(filtered_data))]
test_data = filtered_data.iloc[int(train_data_precent * len(filtered_data)):]
print("Training initialized")
for algorithm in algorithms:
    algorithm.train(train_data)
print("Training finished")

algorithm_tester = AlgorithmTester()
algorithm_results = []

results = {'Test Data': test_data.iloc[5:]['Close'].values}
results_diff = {}

print("Predictions started")
for algorithm in algorithms:
    algorithm_result = algorithm_tester.perform_test(algorithm, test_data)
    algorithm_name = algorithm.name()
    results[algorithm_name] = algorithm_result
    results_diff[algorithm_name] = test_data.iloc[5:]['Close'].values - np.array(algorithm_result)
print("Predictions finished")

result_presenter = ResultPresenter()
result_presenter.print_results_single_chart(results)
result_presenter.print_results_separate_chart(results)
result_presenter.print_results_single_chart(results_diff, title="Test data and predicted data difference", ylabel="Price difference")
