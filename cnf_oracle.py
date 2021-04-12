# Testing Oracle.
from qiskit import QuantumCircuit, assemble, IBMQ, Aer
from qiskit.circuit.library.standard_gates import C3XGate

# Initialization
print("Initializing...")

# Variables
qubits = 7


# Define statevector simulator
print('Get statevector simulator...')
svsim = Aer.get_backend('statevector_simulator')
print('Succesfull!')


# Define quantum circuit
print('Build quantum circuit...')
qc = QuantumCircuit(qubits)

# Initial Hadamard gates.
qc.h([0, 1, 2, 3])

# Oracle

#Clause 1

# Defining literals for clause 1, choose x or i gate, i is not x is normal.
qc.x(0)
qc.i(1)
qc.x(2)

qc.i(3)

# OR gate clause 1

qc.x(4)
qc.append(C3XGate(), [0, 1, 2, 4])

# Defining literals for clause 1, choose x or i gate, i is not x is normal.
qc.x(0)
qc.i(1)
qc.x(2)

qc.i(3)

# Clause 2

# Defining literals for clause 2, choose x or i gate, i is not x is normal.
qc.x(0)
qc.x(1)
qc.i(3)

qc.i(2)

# OR gate clause 2

qc.x(5)
qc.append(C3XGate(), [0, 1, 3, 5])

# Defining literals for clause 2, choose x or i gate, i is not x is normal.
qc.x(0)
qc.x(1)
qc.i(3)

qc.i(2)

# Oracle phase kickback
qc.x(6)
qc.h(6)
qc.ccx(4,5,6)
qc.h(6)
qc.x(6)

#Clause 1

# Defining literals for clause 1, choose x or i gate, i is not x is normal.
qc.x(0)
qc.i(1)
qc.x(2)

qc.i(3)

# OR gate clause 1
qc.x(4)

qc.append(C3XGate(), [0, 1, 2, 4])

# Defining literals for clause 1, choose x or i gate, i is not x is normal.
qc.x(0)
qc.i(1)
qc.x(2)

qc.i(3)

# Clause 2

# Defining literals for clause 2, choose x or i gate, i is not x is normal.
qc.x(0)
qc.x(1)
qc.i(3)

qc.i(2)

# OR gate clause 2
qc.x(5)
qc.append(C3XGate(), [0, 1, 3, 5])

# Defining literals for clause 2, choose x or i gate, i is not x is normal.
qc.x(0)
qc.x(1)
qc.i(3)

qc.i(2)


# Show quantum circuit.
print(qc)

# Simulate quantum circuit.
print('Simutaling quantum circuit...')

qobj = assemble(qc)
result = svsim.run(qobj).result()
statevec = result.get_statevector()

print('Succesfull!')

# Show cnf
print('cnf:')
print('f = ( x2 -x1  x0) ^ (-x3  x1  x0)')

# Show truth table.
print('Truth table:')
print('0	0000	1    %+.2f' % round(statevec[0].real,2) ,' \n'
      '1	0001	1    %+.2f' % round(statevec[1].real,2) ,' \n'
      '2	0010	0    %+.2f' % round(statevec[2].real,2) ,' \n'
      '3	0011	1    %+.2f' % round(statevec[3].real,2) ,' \n'
      '4	0100	1    %+.2f' % round(statevec[4].real,2) ,' \n'
      '5	0101	1    %+.2f' % round(statevec[5].real,2) ,' \n'
      '6	0110	1    %+.2f' % round(statevec[6].real,2) ,' \n'
      '7	0111	1    %+.2f' % round(statevec[7].real,2) ,' \n'
      '8	1000	0    %+.2f' % round(statevec[8].real,2) ,' \n'
      '9	1001	1    %+.2f' % round(statevec[9].real,2) ,' \n'
      '10	1010	0    %+.2f' % round(statevec[10].real,2) ,' \n'
      '11	1011	1    %+.2f' % round(statevec[11].real,2) ,' \n'
      '12	1100	0    %+.2f' % round(statevec[12].real,2) ,' \n'
      '13	1101	1    %+.2f' % round(statevec[13].real,2) ,' \n'
      '14	1110	1    %+.2f' % round(statevec[14].real,2) ,' \n'
      '15	1111	1    %+.2f' % round(statevec[15].real,2) ,' \n')


# Show result.
print('Returned statevector:')
print(statevec[:16])
