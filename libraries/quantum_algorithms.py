# Defining several quantum algorithms
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, assemble, IBMQ, Aer, BasicAer, execute
from qiskit.circuit.library.standard_gates import HGate, XGate, ZGate
from qiskit.visualization import plot_histogram

from math import sqrt

import libraries.quantum_gates as qg
import libraries.sat as sat

# Grover sat solver function.
def grover_sat_solver(cnf, shots):

    # Determine literals.
    literals = []
    for j in range(len(cnf)):
        literals = list(set(literals) | set([abs(i) for i in cnf[j]]))

    # Repeating the cnf grover solver for different number of iterations.
    for k in range(len(literals)):

        # Get required qubits.
        qubits = list(range(0, qg.req_qubits_oracle(cnf)))

        # Get the number of iterations for this repetition.
        iterations = round(sqrt(2 ** k))

        # Define registers.
        qreg = QuantumRegister(len(qubits))
        qc = QuantumCircuit(qreg)

        # Determine literal qubits.
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

        # # Measure all the qubits.
        qc.measure_all()

        # Get backend.
        backend = BasicAer.get_backend('qasm_simulator')

        # Execute job.
        job = execute(qc, backend, shots=shots)

        # Get counts form job.
        counts = job.result().get_counts()

        # Creating iteratable object.
        count_iterator = iter(counts)

        # Iterate thru the counts.
        for j in range(len(counts)):

            # Going to the next measurent.
            measurement = next(count_iterator)

            # Constructing propositional solution.
            solution = []
            for i in range(1,len(literals)+1):

                # Converting the measurent string to solution array.
                solution.append(i) if bool(int(measurement[-i])) else solution.append(-i)

            # Return the proposed solution if correct.
            if sat.verify(cnf, solution): return solution

        # Return None if no solution was found.
        return None
