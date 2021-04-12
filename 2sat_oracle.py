# Testing Oracle.
from qiskit import QuantumCircuit, assemble, IBMQ, Aer

# Initialization
print("Initializing...")

# Variables
qubits = 3


# Define statevector simulator
print('Get statevector simulator...')
svsim = Aer.get_backend('statevector_simulator')
print('Succesfull!')


# Define quantum circuit
print('Build quantum circuit...')
qc = QuantumCircuit(qubits)

# Initial Hadamard gates.
qc.h([0, 1])
qc.i(2)

# Oracle

# Defining literals
qc.x(0)
qc.x(1)

# Oracle phase kickback
qc.x(2)
qc.h(2)
qc.ccx(0,1,2)
qc.h(2)
qc.x(2)

# Defining literals
qc.x(0)
qc.x(1)

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
