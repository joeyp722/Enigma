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
