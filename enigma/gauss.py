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
    y = [tuple(sorted(t)) for t in combinations(literals, 2)]

    # Get z helper variables.
    z = [tuple(sorted(t)) for t in combinations(literals, 3)]

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

# Get equation from points.
def get_equation(points):

    # Add constants to points.
    [point.append(1) for point in points]

    # Construct matrix.
    A = sp.Matrix(points)

    # Construct constants.
    b = sp.Matrix(np.zeros(7))

    # Calculate coefficients of equation.
    equation, params = A.gauss_jordan_solve(b)

    # Normalize the coefficients in the equation.
    equation = [coeff/params[0] for coeff in equation]

    return equation

# Returns matrix with the
def get_matrices(cnf):

    # Get variables and combinations of variables.
    variables = get_variables(cnf)
    variables_unpack = list(set(variables[0]) | set(variables[1]) | set(variables[2]))

    # Define coefficient matrix and constant matrix.
    coeff_matrix = np.zeros((len(cnf), len(variables_unpack)))
    const_matrix = np.zeros(len(cnf))

    # Get matrix row forevery clause.
    for clause in cnf:

        # Get necessary data.
        points = get_points(clause)
        equation = get_equation(points)
        variables_clause = get_variables([clause])
        variables_clause_unpack = list(set(variables_clause[0]) | set(variables_clause[1]) | set(variables_clause[2]))

        # Get coefficients into matrix row for x variables.
        coeff_matrix[cnf.index(clause), variables_unpack.index(variables_clause[0][0])] = equation[0]
        coeff_matrix[cnf.index(clause), variables_unpack.index(variables_clause[0][1])] = equation[1]
        coeff_matrix[cnf.index(clause), variables_unpack.index(variables_clause[0][2])] = equation[2]

        # Get coefficients into matrix row for y helper variables.
        coeff_matrix[cnf.index(clause), variables_unpack.index(variables_clause[1][0])] = equation[3]
        coeff_matrix[cnf.index(clause), variables_unpack.index(variables_clause[1][1])] = equation[4]
        coeff_matrix[cnf.index(clause), variables_unpack.index(variables_clause[1][2])] = equation[5]

        # Get coefficients into matrix row for z helper variables.
        coeff_matrix[cnf.index(clause), variables_unpack.index(variables_clause[2][0])] = equation[6]

        # Get constant into matrix row.
        const_matrix[cnf.index(clause)] = -equation[-1]

    return coeff_matrix, const_matrix

# Returns unique solution if possible. Otherwise it returns None or "Multiple" when there are no solutions or multipe solutions respectively.
def get_unique_solution(coeff_matrix, const_matrix, variables):

    # Unpack variables array.
    variables_unpack = list(set(variables[0]) | set(variables[1]) | set(variables[2]))

    # Construct coefficients matrix.
    A = sp.Matrix(coeff_matrix)

    # Construct constants matrix.
    b = sp.Matrix(const_matrix)

    # Determine if the matrix has a unique solution, multipe solutions or no solution.
    try:
        # Solving the matrix.
        solution_matrix, params = A.gauss_jordan_solve(b)

        # Check if the solution is unique.
        if not params:

            # Define solution array.
            solution = []

            # Loop through every variable that reppressents a literal.
            for variable in variables[0]:

                # Get assignment for literal from the solution_matrix.
                solution.append(int(variable*solution_matrix[variables_unpack.index(variable)]))

            # Return unique solution.
            return solution

        # Return "Multiple" when there are multiple solutions.
        return "Multiple"

    # Return None when the exception "Linear system has no solution" is raised.
    except ValueError as e: return None

# Add rows to the matrix representing constraints.
def add_constraints(coeff_matrix, const_matrix, variables, constraints_x):

    # Unpack variables array.
    variables_unpack = list(set(variables[0]) | set(variables[1]) | set(variables[2]))

    # Get y helper constraints.
    constraints_y_abs = combinations([abs(i) for i in constraints_x], 2) # Get absolute values.
    constraints_y_abs = [tuple(sorted(t)) for t in constraints_y_abs]

    constraints_y_pos = list(set(constraints_y_abs) & set(combinations(constraints_x, 2))) # Get list where tuples only contain positive values.
    constraints_y_pos = [tuple(sorted(t)) for t in constraints_y_pos]

    # Get z helper variables.
    constraints_z_abs = combinations([abs(i) for i in constraints_x], 3) # Get absolute values.
    constraints_z_abs = [tuple(sorted(t)) for t in constraints_z_abs]

    constraints_z_pos = list(set(constraints_z_abs) & set(combinations(constraints_x, 3))) # Get list where tuples only contain positive values.
    constraints_z_pos = [tuple(sorted(t)) for t in constraints_z_pos]

    # Merging y and z helper constraints.
    constraints_helper_abs = list(set(constraints_y_abs) | set(constraints_z_abs))
    constraints_helper_pos = list(set(constraints_y_pos) | set(constraints_z_pos))

    # Add matrix rows based on constraints_x.
    for constraint in constraints_x:

        # Create and add row.
        row = np.zeros(len(variables_unpack))
        row[variables_unpack.index(abs(constraint))] = constraint/abs(constraint)
        coeff_matrix = np.vstack([coeff_matrix,row])
        const_matrix = np.hstack([const_matrix,1])

    # Add matrix rows based on constraints_helper.
    for constraint in constraints_helper_abs:

        # Create and add row.
        row = np.zeros(len(variables_unpack))
        if constraint in constraints_helper_pos: row[variables_unpack.index(constraint)] = 1
        else: row[variables_unpack.index(constraint)] = -1
        coeff_matrix = np.vstack([coeff_matrix,row])
        const_matrix = np.hstack([const_matrix,1])

    return coeff_matrix, const_matrix

# Get solution to cnf via gaussian elimination.
def get_solution(cnf):

    # Get all variables and helper variables.
    variables = get_variables(cnf)

    # Atempt to calculate unique solution.
    coeff_matrix, const_matrix = get_matrices(cnf)
    solution_unique = get_unique_solution(coeff_matrix, const_matrix, variables)

    # If unsatisfiable or a unique solution exists return the answer.
    if solution_unique == None or solution_unique != "Multiple":  return solution_unique

    # Define constraints array.
    constraints_x = []

    # Solving the cnf by applying constraints.
    for variable_x in variables[0]:

        # Add x constraint.
        constraints_x.append(variable_x)

        # Get solution
        coeff_matrix, const_matrix = get_matrices(cnf)
        coeff_matrix, const_matrix = add_constraints(coeff_matrix, const_matrix, variables, constraints_x)
        solution_unique = get_unique_solution(coeff_matrix, const_matrix, variables)

        # If unsatisfiable change constraint_x.
        if solution_unique == None:

            # Changing x constraint.
            constraints_x[-1] = -constraints_x[-1]

            # Get solution
            coeff_matrix, const_matrix = get_matrices(cnf)
            coeff_matrix, const_matrix = add_constraints(coeff_matrix, const_matrix, variables, constraints_x)
            solution_unique = get_unique_solution(coeff_matrix, const_matrix, variables)

            # If still unsatisfiable stop the algorithm.
            if solution_unique == None: return None

    # When the algorithm is done and satisfiable the x constraints are equal to a solution.
    solution = constraints_x
    return solution
