# Grover SAT solver
The aim of this project is to build a quantum algorithm, that solves SAT problems. SAT refers to the satisfiability of Boolean formulas, which means that there is a input where the formula returns TRUE.

"Grover" refers to Grover's algorithm, which is a well known quantum algorithm [1]. This algorithm possesses a oracle, that is used to find the states that satisfy the formula.

## Documentation

Documentation can be found in the docs directory, that contains documentation on:

* Prerequisites
* Introduction to SAT
* Grover sat solver
* Proposition for Gaussian elimination SAT solver algorithm (doesn't work)
* Ideas

## Oracle

The oracle gives all satisfying states a phase-flip, thus the coefficients are multiplied by -1. It is always succeeded by a diffuser, together they can be repeated multiple times depending on the number of iterations.

# How the Oracle works

Each clause in the cnf has it's own ancilla qubit, which is bit-flipped when the clause is TRUE. When all clauses are TRUE a phase-flip is performed on a new ancilla qubit, this provides a phase kickback. Finally the bit-flips are reversed, so that the ancillas can be reused.

To gain a better understanding I would suggest looking at:

> cnf_oracle.py

Or it's subroutine counterpart:

> enigma.quantum_gates.cnf_oracle

## Further remarks

I hope the idea became clear even though the documentation is perhaps rather primitive.

In short:

* The oracle works via phase kickback from ancilla qubits.

The heart of the algorithm lies in these functions:

* enigma.quantum_gates.cnf_oracle
* enigma.quantum_algorithms.grover_sat_solver

## References

[1]: Grover, L. K. (1996, July). A fast quantum mechanical algorithm for database search. In Proceedings of the twenty-eighth annual ACM symposium on Theory of computing (pp. 212-219).
