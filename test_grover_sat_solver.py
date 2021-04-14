import enigma.quantum_algorithms as qa

# Defining cnf.
# cnf = [[1, 2, 3], [1, 2, -3], [1, -2, 3], [1, -2, -3], [-1, 2, 3], [-1, 2, -3], [-1, -2, 3]]
cnf = [[1, 2, 4], [1, 2, -5], [1, -2, 6], [1, -2, -7], [-1, 8, 3], [-1, 2, -3], [-1, -2, 3], [4, 5, 6]]

# Testing grover sat solver.
shots = 100
result = qa.grover_sat_solver(cnf, shots)
print(result)
