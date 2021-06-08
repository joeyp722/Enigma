import enigma.quantum_algorithms as qa
from math import ceil, log

# Defining cnf with solution.
#cnf = [[1, 2, 3], [1, 2, -3], [1, -2, 3], [1, -2, -3], [-1, 2, 3], [-1, 2, -3], [-1, -2, 3]]
cnf1 = [[1, 2, 4], [1, 2, -5], [1, -2, 6], [1, -2, -7], [-1, 8, 3], [-1, 2, -3], [-1, -2, 3], [4, 5, 6]]

# Defining cnf without solution.
cnf2 = [[1, 2, 3], [1, 2, -3], [1, -2, 3], [1, -2, -3], [-1, 2, 3], [-1, 2, -3], [-1, -2, 3], [-1, -2, -3]]

# Testing grover sat solver.
lamb = 6/5          # Increment factor for iteration upper bound.
shots = 100         # Number of shots for job.

number = [1]*8

compare_string = ['1','1','1']

print(sum(number))
print(ceil(log(sum(number))/log(2)))

print(number)

# Test adder oracle for satisfiable cnf.
result = qa.grover_sat_solver_adder(cnf1, number, compare_string, lamb, shots)
print(result)

# Test adder oracle for unsatisfiable cnf.
result = qa.grover_sat_solver_adder(cnf2, number, compare_string, lamb, shots)
print(result)

# Test adder oracle for unsatisfiable cnf, and get the max-sat answer.
result, compare_string = qa.grover_sat_solver_max(cnf2, number, lamb, shots)
print(result)
print(compare_string)
