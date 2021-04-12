# Testing Oracle.
from qiskit import QuantumCircuit, assemble, IBMQ, Aer
from qiskit.circuit.library.standard_gates import C3XGate

# Initialization
print("Initializing...")

# Variables
qubits = 4


# Define statevector simulator
print('Get statevector simulator...')
svsim = Aer.get_backend('statevector_simulator')
print('Succesfull!')


# Define quantum circuit
print('Build quantum circuit...')
qc = QuantumCircuit(qubits)

# Initial Hadamard gates.
qc.h([0, 1, 2])
qc.i(3)

# Oracle

# Defining literals, choose x or i gate
qc.x(0)
qc.x(1)
qc.x(2)

# Oracle phase kickback
qc.x(3)
qc.h(3)
qc.append(C3XGate(), [0, 1, 2, 3])
qc.h(3)
qc.x(3)

# Defining literals, choose x or i gate
qc.x(0)
qc.x(1)
qc.x(2)

# Show quantum circuit.
print(qc)

# Simulate quantum circuit.
print('Simutaling quantum circuit...')

qobj = assemble(qc)
result = svsim.run(qobj).result()
statevec = result.get_statevector()


# Show result.
print('Returned statevector:')
print(statevec)
