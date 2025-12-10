# grover-search-2qubits-qiskit
This project implements a simple version of **Grover's search algorithm** on a 2-qubit system using Qiskit.
We consider a small database of 4 items represented by the computational basis states:

- |00>
- |01>
- |10>
- |11>

The goal is to find a **single marked item**, which in this example is chosen to be **|11>**, using fewer queries than a classical search.

---

## Idea of the Algorithm

1. **Initialize** the 2-qubit system in the equal superposition of all 4 basis states using Hadamard gates.
2. Apply an **oracle** that flips the phase of the target state |11>.
3. Apply the **diffuser** (inversion about the mean), which amplifies the amplitude of the marked state.
4. **Measure** the qubits in the computational basis.

For a database of size N = 4, a single Grover iteration (oracle + diffuser) is sufficient to strongly amplify the target state.

---

## Files in this Repository

- `grover_2qubit.py`  
  Main Python script that builds and runs the 2-qubit Grover circuit.

- `grover_2qubit.ipynb` (optional)  
  Jupyter notebook version with step-by-step explanations and visualizations.

- `requirements.txt`  
  Python dependencies needed to run the project.

---

## How to Run

### 1. Create and activate a Python environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
# or
venv\Scripts\activate         # Windows
