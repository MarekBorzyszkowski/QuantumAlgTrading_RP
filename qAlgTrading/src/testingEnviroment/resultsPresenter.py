import matplotlib.pyplot as plt


class ResultPresenter:
    def __init__(self):
        pass

    def print_results_single_chart(self, results, title="Results of Algorithms", ylabel="Predicted price"):
        """
        Prezentuje wyniki algorytmu na pojedynczym wykresie.

        :param results: Słownik, gdzie kluczem jest nazwa algorytmu, a wartością lista wyników.
                        {'Algorithm Name': [wyniki]}
        """
        plt.figure(figsize=(10, 6))

        for name, result in results.items():
            plt.plot(result, label=name)

        plt.title(title)
        plt.xlabel("Days")
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.legend()
        plt.show()

    def print_results_separate_chart(self, results, title="Results", ylabel="Predicted price"):
        """
        Prezentuje wyniki algorytmów na osobnych wykresach.

        :param results: Słownik, gdzie kluczem jest nazwa algorytmu, a wartością lista wyników.
                        {'Algorithm Name': [wyniki]}
        """
        num_algorithms = len(results)
        plt.figure(figsize=(10, 6 * num_algorithms))

        for i, (name, result) in enumerate(results.items()):
            plt.subplot(num_algorithms, 1, i + 1)
            plt.plot(result)
            plt.title(f"{name}: {title}")
            plt.xlabel("Days")
            plt.ylabel(ylabel)
            plt.grid(True)

        plt.tight_layout()
        plt.show()
