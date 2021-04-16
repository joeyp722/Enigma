import enigma.quantum_algorithms as qa

# Defining cnf with solution.
#cnf = [[1, 2, 3], [1, 2, -3], [1, -2, 3], [1, -2, -3], [-1, 2, 3], [-1, 2, -3], [-1, -2, 3]]
cnf = [[1, 2, 4], [1, 2, -5], [1, -2, 6], [1, -2, -7], [-1, 8, 3], [-1, 2, -3], [-1, -2, 3], [4, 5, 6]]

# Defining cnf without solution.
# cnf = [[1, 2, 3], [1, 2, -3], [1, -2, 3], [1, -2, -3], [-1, 2, 3], [-1, 2, -3], [-1, -2, 3], [-1, -2, -3]]

# Testing grover sat solver.
lamb = 6/5          # Increment factor for iteration upper bound.
shots = 100         # Number of shots for job.
result = qa.grover_sat_solver(cnf, lamb, shots)
print(result)
