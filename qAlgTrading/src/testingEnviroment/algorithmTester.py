class AlgorithmTester:
    def __init__(self):
        pass

    def perform_test(self, algorithm, data):
        """
        Wykonuje test na zadanym algorytmie przy użyciu dostarczonych danych.

        :param algorithm: Obiekt będący instancją klasy dziedziczącej po TradingAlgorithm.
        :param data: Tablica dwuwymiarowa (numpy array) z wartościami akcji dla danego przedziału czasu.
                     Wiersze reprezentują różne dni, a kolumny różne aktywa.
        :return: Wyniki modelu w postaci tabeli (numpy array) zawierającej predykcje algorytmu.
        """
        results = algorithm.fit(data)

        return results
