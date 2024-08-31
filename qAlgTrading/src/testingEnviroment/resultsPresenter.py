import matplotlib.pyplot as plt
import numpy as np

class ResultPresenter:
    def __init__(self):
        pass

    def print_results_single_chart(self, results):
        """
        Prezentuje wyniki algorytmu na pojedynczym wykresie.

        :param results: Tablica trójwymiarowa (numpy array) z wynikami algorytmów.
                        Wymiary tablicy: [liczba_algorytmów, liczba_dni, liczba_aktywow].
        """
        plt.figure(figsize=(10, 6))

        for i, result in enumerate(results):
            mean_result = np.mean(result, axis=1)
            days = np.arange(1, result.shape[0] + 1)
            plt.plot(mean_result, label=f'Algorithm {i + 1}')

        plt.title("Results of Algorithms")
        plt.xlabel("Days")
        plt.ylabel("Mean Value of Assets")
        plt.xticks(days)
        plt.legend()
        plt.show()

    def print_results_separate_chart(self, results):
        """
        Prezentuje wyniki algorytmów na osobnych wykresach.

        :param results: Tablica trójwymiarowa (numpy array) z wynikami algorytmów.
                        Wymiary tablicy: [liczba_algorytmów, liczba_dni, liczba_aktywow].
        """
        num_algorithms = results.shape[0]
        plt.figure(figsize=(10, 6 * num_algorithms))

        for i, result in enumerate(results):
            plt.subplot(num_algorithms, 1, i + 1)
            mean_result = np.mean(result, axis=1)
            days = np.arange(1, result.shape[0] + 1)
            plt.plot(mean_result)
            plt.title(f"Algorithm {i + 1} Results")
            plt.xlabel("Days")
            plt.ylabel("Mean Value of Assets")
            plt.xticks(days)

        plt.tight_layout()
        plt.show()

