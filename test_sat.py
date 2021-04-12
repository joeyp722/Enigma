import libraries.sat as sat
import libraries.logical_gates as lg

# Testing SAT solver.
cnf = [[5],[-4,1],[-4,2],[4,-1,-2],[-5,4,3],[5,-4],[5,-3]]
solution = sat.solve(cnf)

print(cnf)
print(solution)

result = sat.verify(cnf, solution)
print(result)

# Testing the generation of new literal.
input = [1,2]
new_literal = sat.new_literal(input, cnf)
print(new_literal)

# Testing OR gate.
cnf = []

input = [1,2]
literal, cnf = lg.or_gate(input, cnf)
output, cnf = lg.output_literal(literal, cnf)
solution = sat.solve(cnf)
print(output)
print(cnf)
print(solution)

# Testing AND gate.
cnf = []

input = [1,2]
literal, cnf = lg.and_gate(input, cnf)
output, cnf = lg.output_literal(literal, cnf)
solution = sat.solve(cnf)
print(output)
print(cnf)
print(solution)

# Constructing and testing XOR gate.
cnf = []

input = [1,2]
literal1, cnf = lg.and_gate(input, cnf)
literal2, cnf = lg.or_gate(input, cnf)

input = [-literal1, literal2]
literal3, cnf = lg.and_gate(input, cnf)

output, cnf = lg.output_literal(literal3, cnf)
solution = sat.solve(cnf)
print(output)
print(cnf)
print(solution)

# Testing OR gate.
cnf = []

input = [1,2,3,4]
literal, cnf = lg.or_n_gate(input, cnf)
output, cnf = lg.output_literal(literal, cnf)
solution = sat.solve(cnf)
print(output)
print(cnf)
print(solution)

# Testing AND gate.
cnf = []

input = [1,2,3,4]
literal, cnf = lg.and_n_gate(input, cnf)
output, cnf = lg.output_literal(literal, cnf)
solution = sat.solve(cnf)
print(output)
print(cnf)
print(solution)
