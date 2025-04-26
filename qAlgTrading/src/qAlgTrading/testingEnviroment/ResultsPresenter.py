from datetime import datetime

import matplotlib.pyplot as plt


class ResultPresenter:
    def __init__(self):
        pass

    def print_results_single_chart(self, results, input_dates, title="Results of Algorithms", ylabel="Predicted price", component_name="NOT_GIVEN", with_save=False, subfolder="predictions"):
        """
        Prezentuje wyniki algorytmu na pojedynczym wykresie.

        :param results: Słownik, gdzie kluczem jest nazwa algorytmu, a wartością lista wyników.
                        {'Algorithm Name': [wyniki]}
        """
        dates = self.convert_dates(input_dates)
        plt.figure(figsize=(10, 6))

        for name, result in results.items():
            plt.plot(dates, result, label=name)

        plt.title(title)
        plt.xlabel("Days")
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.legend()
        if with_save:
            plt.savefig(f"../results/{component_name}/figures/{subfolder}/{title.replace(' ', '_')}.png")
        plt.close()

    def print_results_separate_chart(self, results, input_dates, title="Results", ylabel="Predicted price", component_name="NOT_GIVEN", with_save=False, subfolder="predictions"):
        """
        Prezentuje wyniki algorytmów na osobnych wykresach.

        :param results: Słownik, gdzie kluczem jest nazwa algorytmu, a wartością lista wyników.
                        {'Algorithm Name': [wyniki]}
        """
        dates = self.convert_dates(input_dates)
        num_algorithms = len(results)
        plt.figure(figsize=(10, 6 * num_algorithms))

        for i, (name, result) in enumerate(results.items()):
            plt.subplot(num_algorithms, 1, i + 1)
            plt.plot(dates, result)
            plt.title(f"{name}: {title} ")
            plt.xlabel("Days")
            plt.ylabel(ylabel)
            plt.grid(True)

        plt.tight_layout()
        if with_save:
            plt.savefig(f"../results/{component_name}/figures/{subfolder}/{title.replace(' ', '_')}.png")
        plt.close()

    def convert_dates(self, dates):
        return [datetime.strptime(date, '%Y-%m-%d') for date in dates]