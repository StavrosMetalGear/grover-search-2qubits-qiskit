#!/usr/bin/env python
# coding: utf-8

# In[1]:


# grover_2qubit.py

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


def grover_oracle_mark_11(qc, q0, q1):
    """
    Oracle that flips the phase of the |11> state.
    For 2 qubits, a controlled-Z acts as a phase flip on |11>.
    """
    qc.cz(q0, q1)


def diffuser(qc, q0, q1):
    """
    Grover diffuser (inversion about the mean) for 2 qubits.

    This amplifies the amplitude of the marked state after the oracle.
    """
    # Hadamard on both qubits
    qc.h([q0, q1])
    # X on both qubits
    qc.x([q0, q1])

    # Controlled-Z in the |11> subspace
    qc.h(q1)
    qc.cx(q0, q1)
    qc.h(q1)

    # X on both qubits again
    qc.x([q0, q1])
    # Hadamard on both qubits again
    qc.h([q0, q1])


def build_grover_circuit_2qubit():
    """
    Build a 2-qubit Grover search circuit for N=4 items,
    with the target state marked as |11>.
    """
    qc = QuantumCircuit(2, 2)

    # 1. Start in equal superposition over all 4 basis states
    qc.h([0, 1])

    # 2. Apply oracle that marks |11>
    grover_oracle_mark_11(qc, 0, 1)

    # 3. Apply diffuser
    diffuser(qc, 0, 1)

    # 4. Measure in computational basis
    qc.measure([0, 1], [0, 1])

    return qc


def run_grover_2qubit(shots=1024):
    """
    Build and run the Grover circuit on the qasm_simulator.
    """
    qc = build_grover_circuit_2qubit()
    print("Grover 2-qubit circuit (target = |11>):")
    print(qc.draw())

    backend = Aer.get_backend("qasm_simulator")
    qc_t = transpile(qc, backend)
    job = backend.run(qc_t, shots=shots)
    result = job.result()
    counts = result.get_counts()

    print("\nMeasurement counts:")
    print(counts)

    plot_histogram(counts)
    plt.show()


if __name__ == "__main__":
    run_grover_2qubit()


# In[ ]:




