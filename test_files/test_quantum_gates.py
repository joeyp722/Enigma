from qiskit import QuantumCircuit, QuantumRegister, assemble, IBMQ, Aer
from qiskit.circuit.library.standard_gates import HGate, XGate, ZGate

import enigma.quantum_gates as qg

# 3 Controlled Hadamard
gate = HGate().control(3)

qc = QuantumCircuit(4)
qc.append(gate, [0, 1, 2, 3])

print(qc)

# 3 Controlled X gate
gate = XGate().control(3)

qc = QuantumCircuit(6)
qc.append(gate, [0, 1, 2, 5])

print(qc)

# 3 Controlled Z gate
gate = ZGate().control(3)

qc = QuantumCircuit(6)
qc.append(gate, [0, 1, 2, 5])

print(qc)

# 6 Controlled Z gate
gate = ZGate().control(6)

qc = QuantumCircuit(10)
qc.append(gate, [0, 1, 2, 3, 4, 5, 9])

print(qc)

# Diffusor gate.
qc = QuantumCircuit(6)

target = [0, 1, 2, 3, 4, 5]
diffuser = qg.diffuser(target)
qc.append(diffuser, target)

print(qc)

# OR gate based on clause.
qc = QuantumCircuit(10)

input = [1, -2, 3]
target = 6

qubits = list(set([abs(i)-1 for i in input]) | set([target-1]))

or_gate_x = qg.or_gate_x(input, target)
qc.append(or_gate_x, qubits)

print(qc)

# OR gate based on clause.
qc = QuantumCircuit(10)

input = [1, -2, 3, -5, 6]
target = 4

qubits = list(set([abs(i)-1 for i in input]) | set([target-1]))

or_gate_z = qg.or_gate_z(input, target)
qc.append(or_gate_z, qubits)

print(qc)

# AND gate based on clause.
qc = QuantumCircuit(10)

input = [1, -2, 3]
target = 6

qubits = list(set([abs(i)-1 for i in input]) | set([target-1]))

and_gate_x = qg.and_gate_x(input, target)
qc.append(and_gate_x, qubits)

print(qc)

# AND gate based on clause.
qc = QuantumCircuit(10)

input = [1, -2, 3]
target = 6

qubits = list(set([abs(i)-1 for i in input]) | set([target-1]))

and_gate_z = qg.and_gate_z(input, target)
qc.append(and_gate_z, qubits)

print(qc)

# Cnf oracle gate.
cnf = [[1, 2, 3], [-1, 2, -4], [1, 2, -5]]
qubits = list(range(0, qg.req_qubits_oracle(cnf)))

qc = QuantumCircuit(len(qubits))
cnf_oracle = qg.cnf_oracle(cnf)
qc.append(cnf_oracle, qubits)

print(qc)

# Cnf Grover gate.
cnf = [[1, 2, 3], [-1, 2, -4], [1, 2, -5]]
qubits = list(range(0, qg.req_qubits_oracle(cnf)))
iterations = 3

qc = QuantumCircuit(len(qubits))

# Determine literals.
literal_qubits = []
for j in range(len(cnf)):
    literal_qubits = list(set(literal_qubits) | set([abs(i) for i in cnf[j]]))

# Hadamards for literal qubits.
for i in range(len(literal_qubits)):
    qc.h(i)

# Bit flip for phase kick-back qubit.
qc.x(qubits[-1])

# Grover gate for cnf.
cnf_grover = qg.cnf_grover(cnf, iterations)
qc.append(cnf_grover, qubits)

# Reset bit flip for phase kick-back qubit for ease of use of statevector
qc.x(qubits[-1])

print(qc)
