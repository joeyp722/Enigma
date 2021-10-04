import pycosat
import numpy as np
import random

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

# Returns random cnf based on the number of literals, clauses and number of literals with the clause.
def get_random_cnf(number_literals, number_clauses, number_literals_within_clause):

    # Define literals and negations.
    literals = range(1,number_literals+1)
    negations = [2*(i % 2)-1 for i in range(1,2*number_literals_within_clause+1)]

    # Define cnf empty array.
    cnf = []

    # printing n elements from list
    for i in range(number_clauses):

        # Construct and add clause.
        clause_literals = random.sample(literals, number_literals_within_clause)
        clause_negations = random.sample(negations, number_literals_within_clause)
        cnf.append(list([clause_literals[i]*clause_negations[i] for i in range(number_literals_within_clause)]))

    return cnf
