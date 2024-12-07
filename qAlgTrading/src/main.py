import numpy as np
import pandas as pd

from algorithms import PcaAlgorithm, SvmAlgorithm, QPcaAlgorithm, QSvmAlgorithm
from testingEnviroment import AlgorithmTester, ResultPresenter

start_date = '2003-01-01'
num_days = 10000
train_data_percent = 0.7

file_path = '../data/sp500/^SPX.csv'
data = pd.read_csv(file_path)
filtered_data = data[data['Date'] >= start_date].head(num_days)


print("Start of algorithm initialization")
pca_algorithm = PcaAlgorithm()
print("PCA initialized")
svm_algorithm = SvmAlgorithm()
print("SVM initialized")
# qpca_algorithm = QPcaAlgorithm()
# print("QPCA initialized")
# qsvm_algorithm = QSvmAlgorithm()
# print("QSVM initialized")
print("End of initialization")
algorithms = [pca_algorithm, svm_algorithm]#, qpca_algorithm, qsvm_algorithm]

train_data = filtered_data.iloc[:int(train_data_percent * len(filtered_data))]
test_data = filtered_data.iloc[int(train_data_percent * len(filtered_data)):]
print("Training initialized")
for algorithm in algorithms:
    print(f"Start training of {algorithm.name()}")
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
