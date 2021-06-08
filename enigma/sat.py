import pycosat
import numpy as np

# Verify potential solution to cnf with true of false.
def verify(cnf, solution):

    # Iterate thru each clause.
    for i in range(len(cnf)):

        # Check if the solution satesfies the clause.
        if not np.in1d(cnf[i],solution).any():
            return False

    return True

# Verify potential solution to cnf based on compare string with true of false.
def verify_max(cnf, solution, compare_string):

    # Define compare string value.
    compare_string_value = 0

    # Get compare string value.
    for i in range(len(compare_string)):
        if compare_string[i] == '1': compare_string_value += 2 ** i

    # Define counter.
    count = 0

    # Iterate thru each clause.
    for i in range(len(cnf)):

        # Check if the solution satesfies the clause.
        if np.in1d(cnf[i],solution).any(): count += 1

        # Compare the counter with the expected value.
        if count >= compare_string_value: return True

    return False

# Solve the cnf with pycosat.
def solve(cnf):
    solution =  pycosat.solve(cnf)
    return solution

# Returns new literal not yet found in the input or cnf.
def new_literal(input, cnf):

    # Get literals from input.
    literals = list(set([abs(i) for i in input]))

    # Add literals from cnf.
    for j in range(len(cnf)):
        literals = list(set(literals) | set([abs(i) for i in cnf[j]]))

    # Generate literal not yet found in input or cnf.
    if literals == []: return 1
    return literals[-1]+1

# Convert decimal number to bit array. By removing hexadecimal 0b, putting zeros in front and mirroring the resulting string.
def decimal2binary(qubits, number):
    return bin(number).replace("0b", "").zfill(len(qubits))[::-1]

# Get clause for phase kickback and gate.
def get_ancilla_adder_clause(ancilla_literals, compare_string):

    # The array that will be returned.
    array = []

    for i in range(len(compare_string)):

        if compare_string[i] == str(1):
            array.append(ancilla_literals[i])
        elif compare_string[i] == str(0):
            array.append(-1*ancilla_literals[i])

    return array
