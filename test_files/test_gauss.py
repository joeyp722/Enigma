import enigma.gauss as gs

# Define cnf.
cnf = [[1,2,3],[-1,2,3],[1,4,5]]

# Get all variables and helper variables.
variables = gs.get_variables(cnf)
print(variables)

# Get points for clause.
points = gs.get_points(cnf[2])
print(points)

# Get equation for clause.
equation = gs.get_equation(points)
print(equation)

#################################################

# Under construction.
gs.get_matrix(cnf)
