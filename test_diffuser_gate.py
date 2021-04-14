# Test custom gates via simmulation.

from qiskit import QuantumCircuit, QuantumRegister, assemble, IBMQ, Aer, execute
from qiskit.circuit.library.standard_gates import HGate, XGate, ZGate

import enigma.quantum_gates as qg

# Diffuser gate.
target = [0, 1]

qc = QuantumCircuit(len(target))

# Hadamards for literal qubits.
for i in range(len([0, 1])):
    qc.h(i)

# Oracle gate.
qc.cz(0,1)

# Diffuser gate.
diffuser = qg.diffuser(target)
qc.append(diffuser, target)

print(qc)

# Select the StatevectorSimulator from the Aer provider
simulator = Aer.get_backend('statevector_simulator')

# Execute and get counts
result = execute(qc, simulator).result()
statevector = result.get_statevector(qc)
print(statevector)
