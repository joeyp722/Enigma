import sympy as sp
import numpy as np
from itertools import combinations

# Returns -1 if there is a negative element in the array. Otherwise 1 is returned.
def sign_check_array(array):

    # Check if the array is an integer. And check for the sign.
    if isinstance(array, int):
        if array < 0: return -1
        return 1

    # Check array for negative elements.
    for i in array:
        if i < 0: return -1
    return 1

# Get the variables and helper variables from the cnf.
def get_variables(cnf):

    # Define empty literals array.
    literals = []

    # Get literals from cnf.
    for j in range(len(cnf)):
        literals = list(set(literals) | set([abs(i) for i in cnf[j]]))

    # Get x variables.
    x = literals

    # Get y helper variables.
    y = list(combinations(literals, 2))

    # Get z helper variables.
    z = list(combinations(literals, 3))

    return x, y, z

# Get points from clause.
def get_points(clause):

    # Get negation array. This is the only assignment that does not satisfy the clause.
    neg_array = [-sign_check_array(clause[0]), -sign_check_array(clause[1]), -sign_check_array(clause[2])]

    # Define empty points array.
    points = []

    # Create all the points
    for j in range(0,8):

        # Construct point.
        point = [int(i) for i in list('{0:0b}'.format(j))] # Get binary representayion.
        point = list([0 for i in range(0,3-len(point))]) + point # Put zeros in front in array.
        point = [-1 if j==0 else j for j in point] # Replace 0's with -1's.
        point = point[::-1] # Flip order elements.

        # Add new point to existing points.
        points = points + [point]

    # Remove the negation array from the list on points.
    points.remove(neg_array)

    # Append values for helper variables
    for point in points:

        point.append(1) if point[0] == 1 and point[1] == 1 else point.append(-1) # Append for first and second literal.
        point.append(1) if point[0] == 1 and point[2] == 1 else point.append(-1) # Append for first and third literal.
        point.append(1) if point[1] == 1 and point[2] == 1 else point.append(-1) # Append for second and third literal.
        point.append(1) if point[0] == 1 and point[1] == 1 and point[2] == 1 else point.append(-1) # Append for first, second and third literal.

    return points

# Get exquation from points.
def get_equation(points):

    # Add constants to points.
    [point.append(1) for point in points]

    # Construct matrix.
    A = sp.Matrix(points)

    # Construct constants.
    b = sp.Matrix(np.zeros(7))

    # Calculate coefficients of equation.
    equation, params = A.gauss_jordan_solve(b)

    # Normalize the coefficients
    equation = [coeff/params[0] for coeff in equation]

    return equation

######################################################################

# Under construction.
def get_matrix(cnf):

    variables = get_variables(cnf)
    variables_unpack = list(set(variables[0]) | set(variables[1]) | set(variables[2]))

    print(variables_unpack)

    equations = []

    for clause in cnf:
        points = get_points(clause)
        equation = get_equation(points)
        variables_clause = get_variables([clause])
        variables_clause_unpack = list(set(variables_clause[0]) | set(variables_clause[1]) | set(variables_clause[2]))


        print(equation)
        print(variables_clause)
        print(variables)
        print(variables_unpack.index(variables_clause_unpack[6]))
