# Testing Oracle.
from qiskit import QuantumCircuit, assemble, IBMQ, Aer

# Initialization
print("Initializing...")

# Variables
qubits = 2


# Define statevector simulator
print('Get statevector simulator...')
svsim = Aer.get_backend('statevector_simulator')
print('Succesfull!')


# Define quantum circuit
print('Build circuit...')
qc = QuantumCircuit(qubits)

# Initial Hadamard gates.
qc.h([0, 1])

# Oracle
qc.cz(0,1)

# # Diffusion operator (U_s)
# qc.h([0,1])
# qc.z([0,1])
# qc.cz(0,1)
# qc.h([0,1])

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
