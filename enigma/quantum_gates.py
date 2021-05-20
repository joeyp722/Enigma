# Defining several quantum gates.
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library.standard_gates import HGate, XGate, ZGate, rz

from math import pi

import enigma.sat as sat

# Diffuser gate for Grover algorithm.
def diffuser(target):

    # Define quantum circuit.
    qc = QuantumCircuit(len(target), name = 'Diffuser')

    # Execute Hadamard and X gates for all target qubits.
    for i in range(len(target)):
        qc.h(i)
        qc.x(i)

    # Perform a phase flip when all target qubits are in the 1 state.
    gate = ZGate().control(len(target)-1)
    qc.append(gate, list(range(0, len(target))))

    # Execute Hadamard and X gates for all target qubits.
    for i in range(len(target)):
        qc.x(i)
        qc.h(i)

    return qc.to_gate()

# Performs a controlled X gate based on the output for n-bit OR gate for the input literals.
def or_gate_x(input, target):

    # Define quantum circuit.
    qc = QuantumCircuit(len(input)+1, name = 'Or_gate_x')

    # Perform a bit flip on target qubit.
    qc.x(len(input))

    # Performing necessary negations.
    for i in range(len(input)):
        qc.i(i) if input[i] < 0 else qc.x(i)

    # Peform the required controlled X gate.
    gate = XGate().control(len(input))
    qc.append(gate, list(range(0, len(input)+1)))

    # Performing necessary negations. (reset)
    for i in range(len(input)):
        qc.i(i) if input[i] < 0 else qc.x(i)

    return qc.to_gate()

# Performs a controlled X gate based on the output for n-bit AND gate for the input literals.
def and_gate_x(input, target):

    # Define quantum circuit.
    qc = QuantumCircuit(len(input)+1, name = 'And_gate_x')

    # Performing necessary negations.
    for i in range(len(input)):
        qc.x(i) if input[i] < 0 else qc.i(i)

    # Peform the required controlled X gate.
    gate = XGate().control(len(input))
    qc.append(gate, list(range(0, len(input)+1)))

    # Performing necessary negations. (reset)
    for i in range(len(input)):
        qc.x(i) if input[i] < 0 else qc.i(i)

    return qc.to_gate()

# Performs a controlled Z gate based on the output for n-bit OR gate for the input literals.
def or_gate_z(input, target):

    # Define quantum circuit.
    qc = QuantumCircuit(len(input)+1, name = 'Or_gate_z')

    # Perform a phase flip on target qubit.
    qc.z(len(input))

    # Performing necessary negations.
    for i in range(len(input)):
        qc.i(i) if input[i] < 0 else qc.x(i)

    # Peform the required controlled Z gate.
    gate = ZGate().control(len(input))
    qc.append(gate, list(range(0, len(input)+1)))

    # Performing necessary negations. (reset)
    for i in range(len(input)):
        qc.i(i) if input[i] < 0 else qc.x(i)

    return qc.to_gate()

# Performs a controlled Z gate based on the output for n-bit AND gate for the input literals.
def and_gate_z(input, target):

    # Define quantum circuit.
    qc = QuantumCircuit(len(input)+1, name = 'And_gate_z')

    # Performing necessary negations.
    for i in range(len(input)):
        qc.x(i) if input[i] < 0 else qc.i(i)

    # Peform the required controlled Z gate.
    gate = ZGate().control(len(input))
    qc.append(gate, list(range(0, len(input)+1)))

    # Performing necessary negations. (reset)
    for i in range(len(input)):
        qc.x(i) if input[i] < 0 else qc.i(i)

    return qc.to_gate()

# Oracle gate for cnf.
def cnf_oracle(cnf):

    # Determine number of required qubits for oracle.
    req = req_qubits_oracle(cnf)

    # Define quantum circuit.
    qc = QuantumCircuit(req, name = 'Cnf_oracle')

    # Determine literals.
    literals = []
    for j in range(len(cnf)):
        literals = list(set(literals) | set([abs(i) for i in cnf[j]]))

    # Determine ancilla qubits and literals.
    ancillas = []
    for i in range(len(cnf)+1):
        ancillas.append(len(literals)+i)

    ancilla_literals = list(set([abs(i)+1 for i in ancillas]))

    # OR gate for each clause.
    for j in range(len(cnf)):

        # Get clause literals.
        literals_clause = list(set([abs(i) for i in cnf[j]]))

        # Get clause literal qubits.
        qubits_clause = list(set([literals_clause.index(i) for i in literals_clause]))

        # Get target qubit.
        qubits_clause.append(len(literals)+j)

        # Peforming the OR gate.
        gate = or_gate_x(cnf[j], len(literals)+j)
        qc.append(gate, qubits_clause)

    # AND gate for phase kickback.
    gate = and_gate_z(ancilla_literals[:-1], ancillas[-1])
    qc.append(gate, ancillas)

    # OR gate for each clause. (reset)
    for j in range(len(cnf)):

        # Get clause literals.
        literals_clause = list(set([abs(i) for i in cnf[j]]))

        # Get clause literal qubits.
        qubits_clause = list(set([literals_clause.index(i) for i in literals_clause]))

        # Get target qubit.
        qubits_clause.append(len(literals)+j)

        # Peforming the OR gate.
        gate = or_gate_x(cnf[j], len(literals)+j)
        qc.append(gate, qubits_clause)

    return qc.to_gate()

# Get number of required qubits for oracle.
def req_qubits_oracle(cnf):

    # Determine literals.
    literals = []
    for j in range(len(cnf)):
        literals = list(set(literals) | set([abs(i) for i in cnf[j]]))

    return len(literals) + len(cnf) + 1

# Grover gate for cnf.
def cnf_grover(cnf, iterations):

    # Determine number of required qubits for oracle.
    req = req_qubits_oracle(cnf)

    # Defining the required qubits for oracle.
    qubits = list(range(0, req_qubits_oracle(cnf)))

    # Define quantum circuit.
    qc = QuantumCircuit(req, name = 'Cnf_grover^'+str(iterations))

    # Determine target qubits for diffuser.
    target = []
    for j in range(len(cnf)):

        # Get clause literals.
        literals_clause = list(set([abs(i) for i in cnf[j]]))

        # Get target qubits.
        target = list(set([literals_clause.index(i) for i in literals_clause]))

    # Define oracle and diffuser gates.
    cnf_oracle_gate = cnf_oracle(cnf)
    diffuser_gate = diffuser(target)

    # Constructing the circuit for a specific number of iterations.
    for i in range(0, iterations):
        qc.append(cnf_oracle_gate, qubits)
        qc.append(diffuser_gate, target)

    return qc.to_gate()

# Quantum Fourier Transformation (QFT), and inverse QFT.
def qft(qubits, invert):

    # Define quantum circuit.
    qc = QuantumCircuit(len(qubits), name = 'QFT')

    # Peform quantum circuit for Quantum Fourier Transform.
    for i in range(len(qubits)):
        qc.h(len(qubits)-1-i)

        # Perform controlled phase gates.
        for j in range(i+1, len(qubits)):
            qc.cp(2*pi*(2 ** (i-j-1)), len(qubits)-1-j, len(qubits)-1-i)

    # Invert QFT if applicable.
    if invert: qc = qc.inverse()

    return qc.to_gate()

# Peforming addition with the qubit register in the Hadamard basis.
def adder(qubits, number):

    # Define quantum circuit.
    qc = QuantumCircuit(len(qubits), name = '+' + str(number))

    # Convert number to bit string.
    bit_array = sat.decimal2binary(qubits, number)

    # Peform quantum circuit for quantum adder.
    for i in range(len(qubits)):

        # Perform controlled phase gates.
        for j in range(i+1):
            if bit_array[j] == '1': qc.rz(2*pi*(2 ** (-i+j-1)), i)

    return qc.to_gate()
