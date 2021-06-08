# Test custom gates via simmulation.

from qiskit import QuantumCircuit, QuantumRegister, assemble, IBMQ, Aer, BasicAer, execute
from qiskit.circuit.library.standard_gates import HGate, XGate, ZGate
from qiskit.visualization import plot_histogram

import enigma.quantum_gates as qg

# Cnf Grover gate.
# cnf = [[1, 2, 3], [-1, 2, -4], [1, 2, -5]]
# cnf = [[1, 2]]
# cnf = [[1, 2], [3, 4]]
# cnf = [[1, 2], [1, 3]]
cnf = [[1, 2, 3], [1, 2, -3], [1, -2, 3], [1, -2, -3], [-1, 2, 3], [-1, 2, -3], [-1, -2, 3]]


qubits = list(range(0, qg.req_qubits_oracle(cnf, False, len(cnf)*[1])))
iterations = 1

qc = QuantumCircuit(len(qubits))

# Determine literal qubits.
literal_qubits = []
for j in range(len(cnf)):
    literal_qubits = list(set(literal_qubits) | set([abs(i) for i in cnf[j]]))

# Hadamards for literal qubits.
for i in range(len(literal_qubits)):
    qc.h(i)

# Bit flip for phase kickback qubit.
qc.x(qubits[-1])

# Grover gate for cnf.
cnf_grover = qg.cnf_grover(cnf, iterations)
qc.append(cnf_grover, qubits)

# Reset bit flip for phase kickback qubit for ease of use of statevector
qc.x(qubits[-1])

print(qc)

# Select the StatevectorSimulator from the Aer provider
simulator = Aer.get_backend('statevector_simulator')

# Execute and get counts
result = execute(qc, simulator).result()
statevector = result.get_statevector(qc)
print(statevector[:(2 ** len(literal_qubits))])
