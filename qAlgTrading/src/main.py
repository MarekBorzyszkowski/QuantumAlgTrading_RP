import json
import os
import sys
import time

import numpy as np
import pandas as pd

from algorithms import PcaAlgorithm, SvmAlgorithm, QPcaAlgorithm, QSvmAlgorithm
from testingEnviroment import AlgorithmTester, ResultPresenter

json_file_name = sys.argv[1]
json_output = {}

with open(json_file_name, "r") as file:
    loaded_data = json.load(file)

start_date = loaded_data["start_date"]
num_days = loaded_data["num_days"]
train_data_percent = loaded_data["train_data_percent"]

is_component_of_index = loaded_data["is_component_of_index"]
component = loaded_data["component"]
index = loaded_data["index"]

use_pca = loaded_data["use_pca"]
use_svm = loaded_data["use_svm"]
use_qpca = loaded_data["use_qpca"]
use_qsvm = loaded_data["use_qsvm"]

component_name = f"{index}_{component}"
json_output[component_name] = component_name
newpath = f"../results/{component_name}"

load_models = loaded_data["load_models"]
component_model_to_load = loaded_data["loaded_model_path"] #component_name
loadedModelPath = f"../results/{component_model_to_load}/model"

if not os.path.exists(newpath):
    os.makedirs(newpath)
    os.makedirs(f"{newpath}/figures")
    os.makedirs(f"{newpath}/info")
    os.makedirs(f"{newpath}/model")
print(f"{component} from {index} starts")

if is_component_of_index:
    file_path = f'../data/{index}/components/{component}.csv'
else:
    file_path = f'../data/{index}/{component}.csv'
data = pd.read_csv(file_path)
filtered_data = data[data['Date'] >= start_date].head(num_days)

algorithms = []
print("Start of algorithm initialization")
if use_pca:
    pca_algorithm = PcaAlgorithm()
    print("PCA initialized")
    algorithms.append(pca_algorithm)
if use_svm:
    svm_algorithm = SvmAlgorithm()
    print("SVM initialized")
    algorithms.append(svm_algorithm)
if use_qpca:
    qpca_algorithm = QPcaAlgorithm()
    print("QPCA initialized")
    algorithms.append(qpca_algorithm)
if use_qsvm:
    qsvm_algorithm = QSvmAlgorithm()
    print("QSVM initialized")
    algorithms.append(qsvm_algorithm)
print("End of initialization")

train_data = filtered_data.iloc[:int(train_data_percent * len(filtered_data))]
test_data = filtered_data.iloc[int(train_data_percent * len(filtered_data)):]
print("Training initialized")
for algorithm in algorithms:
    start = 0
    end = 0
    if load_models:
        algorithm.load(loadedModelPath)
        print(f"Model {algorithm.name()} loaded")
    else:
        print(f"Start training of {algorithm.name()}")
        start = time.perf_counter()
        algorithm.train(train_data)
        end = time.perf_counter()
        # print(f"{algorithm.name()} took {end - start} seconds")
        algorithm.save(f"{newpath}/model")
    json_output[algorithm.name()] = {"training_time_seconds": end - start}
print("Training finished")

algorithm_tester = AlgorithmTester()
algorithm_results = []

results = {'Test Data': test_data.iloc[5:]['Close'].values}
results_diff = {}
results_relative_diff = {}
results_squared_diff = {}

print("Predictions started")
for algorithm in algorithms:
    print(f"Start prediction of {algorithm.name()}")
    algorithm_result = algorithm_tester.perform_test(algorithm, test_data)
    algorithm_name = algorithm.name()
    results[algorithm_name] = algorithm_result
    results_diff[algorithm_name] = test_data.iloc[5:]['Close'].values - np.array(algorithm_result)
    results_relative_diff[algorithm_name] = results_diff[algorithm_name] / test_data.iloc[5:]['Close'].values
    results_squared_diff[algorithm_name] = results_diff[algorithm_name] ** 2
    # print(f"Max absolute error: {np.max(results_diff[algorithm_name])}")
    # print(f"Min absolute error: {np.min(results_diff[algorithm_name])}")
    # print(f"Mean absolute error: {np.mean(results_diff[algorithm_name])}")
    # print(f"Median absolute error: {np.median(results_diff[algorithm_name])}")
    # print()
    # print(f"Max relative error: {np.max(results_relative_diff[algorithm_name])}")
    # print(f"Min relative error: {np.min(results_relative_diff[algorithm_name])}")
    # print(f"Mean relative error: {np.mean(results_relative_diff[algorithm_name])}")
    # print(f"Median relative error: {np.median(results_relative_diff[algorithm_name])}")
    # print()
    # print(f"Mean square error: {np.mean(results_squared_diff[algorithm_name])}")
    # print()
    json_output[algorithm.name()]["Max_absolute_error"] = np.max(results_diff[algorithm_name])
    json_output[algorithm.name()]["Min_absolute_error"] = np.min(results_diff[algorithm_name])
    json_output[algorithm.name()]["Mean_absolute_error"] = np.mean(results_diff[algorithm_name])
    json_output[algorithm.name()]["Median_absolute_error"] = np.median(results_diff[algorithm_name])
    json_output[algorithm.name()]["Max_relative_error"] = np.max(results_relative_diff[algorithm_name])
    json_output[algorithm.name()]["Min_relative_error"] = np.min(results_relative_diff[algorithm_name])
    json_output[algorithm.name()]["Mean_relative_error"] = np.mean(results_relative_diff[algorithm_name])
    json_output[algorithm.name()]["Median_relative_error"] = np.median(results_relative_diff[algorithm_name])
    json_output[algorithm.name()]["Mean_square_error"] = np.mean(results_squared_diff[algorithm_name])
print("Predictions finished")

with open(f"{newpath}/info/training_results.json", "w") as file:
    json.dump(json_output, file, indent=4)
result_presenter = ResultPresenter()
result_presenter.print_results_single_chart(results, title=f"{component_name} results of algorithms", component_name=component_name, with_save=True)
result_presenter.print_results_separate_chart(results, title=f"{component_name} results", component_name=component_name, with_save=True)
result_presenter.print_results_single_chart(results_diff, title=f"{component_name} Test data and predicted data difference",
                                            ylabel="Price difference", component_name=component_name, with_save=True)

# json_file = {
#     "start_date": start_date,
#     "num_days": num_days,
#     "train_data_percent": train_data_percent,
#     "is_component_of_index": is_component_of_index,
#     "component": component,
#     "index": index,
#     "use_pca": use_pca,
#     "use_svm": use_svm,
#     "use_qpca": use_qpca,
#     "use_qsvm": use_qsvm
# }
#
# with open("example.json", "w") as file:
#     json.dump(json_file, file, indent=4)
