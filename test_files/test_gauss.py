import enigma.gauss as gs
import enigma.sat as sat
import sympy as sp
import random

# Define cnf
print("Some cnf:")
cnf = [[1,-2,3],[1,-2,-3],[1,2,3]]

# Get all variables and helper variables.
print("Get variables and first literal.")

variables = gs.get_variables(cnf)
print(variables)
print(variables[0][0])

# Unpack variables array.
print("Unpack the variables.")

variables_unpack = list(set(variables[0]) | set(variables[1]) | set(variables[2]))
print(variables_unpack)

# Get points for clause.
print("Get the points of the third clause.")

points = gs.get_points(cnf[2])
print(points)

# Get equation for clause.
print("Get the equation the variables and helper variables must obey.")

equation = gs.get_equation(points)
print(equation)

# Get matrix that contains the coefficients and constants from the equations.
print("Get coefficient and constant matrix.")

coeff_matrix, const_matrix = gs.get_matrices(cnf)
print(coeff_matrix)
print(const_matrix)

# 0 Test for cnf with unique solution.
print("Test the function get_unique_solution.")

cnf = [[-1,-2,3],[-1,2,-3],[-1,2,3],[1,-2,-3],[1,-2,3],[1,2,-3],[1,2,3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

print(sat.verify(cnf, solution))

# 1 Test for cnf with unique solution.
cnf = [[-1,-2,-3],[-1,2,-3],[-1,2,3],[1,-2,-3],[1,-2,3],[1,2,-3],[1,2,3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

print(sat.verify(cnf, solution))

# 2 Test for cnf with unique solution.
cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,3],[1,-2,-3],[1,-2,3],[1,2,-3],[1,2,3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

print(sat.verify(cnf, solution))

# 3 Test for cnf with unique solution.
cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,-3],[1,-2,-3],[1,-2,3],[1,2,-3],[1,2,3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

print(sat.verify(cnf, solution))

# 4 Test for cnf with unique solution.
cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,-3],[-1,2,3],[1,-2,3],[1,2,-3],[1,2,3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

print(sat.verify(cnf, solution))

# 5 Test for cnf with unique solution.
cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,-3],[-1,2,3],[1,-2,-3],[1,2,-3],[1,2,3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

print(sat.verify(cnf, solution))

# 6 Test for cnf with unique solution.
cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,-3],[-1,2,3],[1,-2,-3],[1,-2,3],[1,2,3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

print(sat.verify(cnf, solution))

# 7 Test for cnf with unique solution.
cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,-3],[-1,2,3],[1,-2,-3],[1,-2,3],[1,2,-3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

print(sat.verify(cnf, solution))

# Test for cnf with multipe solutions.
print("Now for a cnf with multipe solutions.")

cnf = [[1,2,3],[-1,2,3],[1,-2,3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

# Test for cnf with no solution.
print("And now a cnf with no solutions.")

cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,-3],[-1,2,3],[1,-2,-3],[1,-2,3],[1,2,-3],[1,2,3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

# Test for cnf with unique solution and add constraint.
print("Test again without and with constraint.")

cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,-3],[-1,2,3],[1,-2,-3],[1,-2,3],[1,2,-3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

print(sat.verify(cnf, solution))

# Add constraint.
print("Add constraint.")
constraints=[1]

coeff_matrix, const_matrix = gs.add_constraints(coeff_matrix, const_matrix, variables, constraints)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)

print(cnf)
print(constraints)
print(solution)

# Test for cnf with unique solution and add constraint.
print("Now for another cnf.")

cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,-3],[-1,2,3],[1,-2,-3],[1,-2,3],[1,2,-3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

print(sat.verify(cnf, solution))

# Add constraint.
print("Add constraint")

constraints=[1]

coeff_matrix, const_matrix = gs.add_constraints(coeff_matrix, const_matrix, variables, constraints)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)

print(cnf)
print(constraints)
print(solution)

# Test for cnf with unique solution and add multipe constraints.
print("Another cnf.")

cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,3],[1,-2,-3],[1,-2,3],[1,2,-3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

# Add constraint.
print("Add constaint.")
constraints=[1]

coeff_matrix, const_matrix = gs.add_constraints(coeff_matrix, const_matrix, variables, constraints)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)

print(cnf)
print(constraints)
print(solution)

print(sat.verify(cnf, solution))

# Add constraints.
print("Add another constraint.")
constraints=[1,2]

coeff_matrix, const_matrix = gs.add_constraints(coeff_matrix, const_matrix, variables, constraints)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)

print(cnf)
print(constraints)
print(solution)


# Test for shorter cnf with multiple solutions and add multipe constraints.
print("some cnf:")

cnf = [[-1,-2,3],[-1,2,3],[1,-2,-3],[1,-2,3],[1,2,-3]]
print(cnf)

coeff_matrix, const_matrix = gs.get_matrices(cnf)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)
print(solution)

# Add constraint.
print("Add constraint.")

constraints_x=[1]

coeff_matrix, const_matrix = gs.add_constraints(coeff_matrix, const_matrix, variables, constraints_x)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)

print(cnf)
print(constraints_x)
print(solution)

# Add constraints.
print("Add another constraint.")

constraints_x=[1,-2]

coeff_matrix, const_matrix = gs.add_constraints(coeff_matrix, const_matrix, variables, constraints_x)
solution = gs.get_unique_solution(coeff_matrix, const_matrix, variables)

print(cnf)
print(constraints)
print(solution)

# Testing the actual algorithm.
############################################
print("Some cnf's to test the final function: get_solution.")

# cnf1
cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,4]]
solution = gs.get_solution(cnf)

print(cnf)
print(solution)
print(sat.verify(cnf, solution))

# cnf2
cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,4],[4,5,-6],[4,6,7],[4,-9,5]]
solution = gs.get_solution(cnf)

print(cnf)
print(solution)
print(sat.verify(cnf, solution))

# cnf3, Unique solution
cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,-3],[-1,2,3],[1,-2,-3],[1,-2,3],[1,2,-3]]
solution = gs.get_solution(cnf)

print(cnf)
print(solution)

# cnf4, No solution
cnf = [[-1,-2,-3],[-1,-2,3],[-1,2,-3],[-1,2,3],[1,-2,-3],[1,-2,3],[1,2,-3],[1,2,3]]
solution = gs.get_solution(cnf)

print(cnf)
print(solution)

# cnf5
cnf = [[-1,-2,-6],[-11,-2,3],[-1,10,4],[8,5,-6],[4,6,7],[4,-9,5],[4,5,-7],[8,-10,1]]
solution = gs.get_solution(cnf)

print(cnf)
print(solution)
print(sat.verify(cnf, solution))

# cnf6
cnf = [[-5,-6,-3],[-1,4,3],[-1,5,7],[4,5,-11],[10,-6,7],[4,9,5],[2,-7,-4],[10,-8,3],[1,-2,9],[3,5,-2],[-1,6,3]]
solution = gs.get_solution(cnf)

print(cnf)
print(solution)
print(sat.verify(cnf, solution))

# Testing the algorithm for random cnf.
print("Testing the algorithm for random cnf.")

number_literals = 10 # Total number of literals
number_clauses = 30 # Total number of clauses.
number_literals_within_clause = 3 # Because 3-SAT.

cnf = sat.get_random_cnf(number_literals, number_clauses, number_literals_within_clause)

solution = gs.get_solution(cnf)

print(cnf)
print(solution)
print(sat.verify(cnf, solution))
