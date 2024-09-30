import numpy as np
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.circuit.library import CU3Gate, CPhaseGate
from qiskit_aer import Aer
import math


class QPCA:
    def __init__(self):
        self.qc = None
        self.n_qubits = None
        self.data_state = None

    def _prepare_qpca_circuit(self, data_state):
        q = QuantumRegister(self.n_qubits)
        c = ClassicalRegister(self.n_qubits)
        qc = QuantumCircuit(q, c)

        qc.initialize(data_state, q[:len(data_state)])

        if self.n_qubits > 1:
            qc.h(q[0])
            qc.h(q[1])

            theta1, phi1, lambda1 = 1.59899, -1.11512, 2.02647
            qc.append(CU3Gate(theta1, phi1, lambda1), [q[1], q[2]])

            theta2, phi2, lambda2 = 2.22862, 0.513123, 3.65472
            qc.append(CU3Gate(theta2, phi2, lambda2), [q[0], q[2]])

            qc.h(q[0])
            qc.append(CPhaseGate(-np.pi / 2), [q[0], q[1]])
            qc.h(q[1])

        self.qc = qc

    def fit(self, data):
        self.data_state, self.n_qubits = self.load_and_prepare_data(data)
        self._prepare_qpca_circuit(self.data_state)

    def transform(self, new_data=None):
        if new_data is not None:
            new_data, self.n_qubits = self.load_and_prepare_data(new_data)
            self._prepare_qpca_circuit(new_data)

        backend_state = Aer.get_backend('statevector_simulator')
        job_state = transpile(self.qc, backend_state)
        result_state = backend_state.run(job_state).result()

        outputstate = result_state.get_statevector(self.qc, decimals=3)
        return outputstate

    def load_and_prepare_data(self, data):
        averaged_data = np.mean(data, axis=0)

        norm = np.linalg.norm(averaged_data)
        normalized_data = averaged_data / norm

        n_qubits = int(np.ceil(np.log2(len(normalized_data))))

        target_length = 2 ** n_qubits
        padded_state = np.zeros(target_length)
        padded_state[:len(normalized_data)] = normalized_data

        return padded_state, n_qubits
