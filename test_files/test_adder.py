from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, assemble, IBMQ, Aer, BasicAer, execute

import enigma.quantum_gates as qg
import enigma.sat as sat

# Define numbers using in the addition.
number1 = 1
number2 = 2
number3 = 4
number4 = 8

# Define number of shots.
shots = 10

# Define qubits.
qubits = [0, 1, 2, 3, 4, 5, 6]

# Define quantum circuit.
qc = QuantumCircuit(len(qubits), name = 'Test circuit')

# Perform quantum Fourier Transform.
qft = qg.qft(qubits, invert = False)
qc.append(qft, qubits)

# Add number1.
adder = qg.adder(qubits, number1)
qc.append(adder, qubits)

# Add number2.
adder = qg.adder(qubits, number2)
qc.append(adder, qubits)

# Add number3.
adder = qg.adder(qubits, number3)
qc.append(adder, qubits)

# Add number4.
adder = qg.adder(qubits, number4)
qc.append(adder, qubits)

# Perform inverse quantum Fourier Transform.
qft_dg = qg.qft(qubits, invert = True)
qc.append(qft_dg, qubits)

# Show quantum circuit.
print(qc)

# Select the StatevectorSimulator from the Aer provider
simulator = Aer.get_backend('statevector_simulator')

# Measure all the qubits.
qc.measure_all()

# Get backend.
backend = BasicAer.get_backend('qasm_simulator')

# Execute job.
job = execute(qc, backend, shots = shots)

# Get counts form job.
counts = job.result().get_counts()

# Show the counts.
print(counts)
