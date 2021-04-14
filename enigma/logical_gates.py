# Defining logical gates that take input literals and input cnf,
# and give output literals, intermediate literals and output cnf.
# The inputs and outputs of gates are linked via the idea of the Tseytin
# transformation and are written in 3-sat cnf form.

import enigma.sat as sat

# Logical OR gate.
def or_gate(input, cnf):

    # Generate new output literal.
    output = sat.new_literal(input, cnf)

    # Add necessary clauses to cnf.
    cnf.append([input[0], input[1], -output])
    cnf.append([-input[0], output])
    cnf.append([-input[1], output])

    return output, cnf

# Logical AND gate.
def and_gate(input, cnf):

    # Generate new output literal.
    output = sat.new_literal(input, cnf)

    # Add necessary clauses to cnf.
    cnf.append([-input[0], -input[1], output])
    cnf.append([input[0], -output])
    cnf.append([input[1], -output])

    return output, cnf

# Define output literal.
def output_literal(input, cnf):
    output = input
    cnf.append([input])

    return output, cnf

# Logical n-bit OR gate.
def or_n_gate(input, cnf):

    # Construct the circuit by repeating 2-bit OR gates.
    literal = input[0]
    for i in range(len(input)-1):
        literal, cnf = or_gate([literal, input[i+1]], cnf)

    return literal, cnf

# Logical n-bit AND gate.
def and_n_gate(input, cnf):

    # Construct the circuit by repeating 2-bit AND gates.
    literal = input[0]
    for i in range(len(input)-1):
        literal, cnf = and_gate([literal, input[i+1]], cnf)

    return literal, cnf
