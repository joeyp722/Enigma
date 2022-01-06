# Grover SAT solver
The aim of this project is to build a quantum algorithm that can solve SAT problems. SAT refers to satisfiability of a Boolean formula, meaning that there exists a input where the output of the formula is TRUE.

Grover refers to Grover's algorithm from quantum computing [1]. This algorithm uses an oracle to find the states it is looking for, hence the oracle must be representative of the Boolean formula to find a matching input.

## Documentation

Documentation can be found in the docs directory, that contains documentation on:

* Prerequisites
* Introduction to SAT
* Grover sat solver
* Proposition for Gaussian elimination SAT solver algorithm (doesn't work)
* Ideas

## Oracle

In order for the oracle to work all the states of interest must receive a phase-flip, meaning that the coefficient in the state vector is multiplied with -1.

The oracle is always succeeded by a diffuser. This part of the algorithm can be repeated multiple times depending on the number of iterations.

In order to construct an oracle for a cnf. All the clauses have their own ancilla qubit on which a bit-flip is performed if the clause is TRUE. If a clauses are true then a phase-flip is performed via a quantum AND gate, again via a new ancillary qubit that provides a phase kickback.

Note that the bit-flips on the ancilla qubits have to be undone, thus the gates responsible for this are performed once more.

To gain a better understanding I would suggest looking at:

> cnf_oracle.py

Or it's subroutine counterpart:

> enigma.quantum_gates.cnf_oracle

## Further remarks

I hope the idea became clear even though the documentation is perhaps rather primitive. The two main take away points are:

* The oracle works via phase kickback from ancilla qubits.
* Not knowing how many solutions there are doesn't matter for the time complexity. It is still O( sqrt(N/k) )

The heart of the algorithm lies in the functions:

* enigma.quantum_gates.cnf_oracle
* enigma.quantum_algorithms.grover_sat_solver

## References

[1]: Grover, L. K. (1996, July). A fast quantum mechanical algorithm for database search. In Proceedings of the twenty-eighth annual ACM symposium on Theory of computing (pp. 212-219).
