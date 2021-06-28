# Grover SAT solver
The aim of this project is to build a quantum algorithm that can solve SAT problems. SAT refers to satisfiability of a Boolean formula, meaning that there exists a input where the output of the formula is TRUE.

Grover refers to Grover's algorithm from quantum computing [1]. This algorithm uses an oracle to find the states it is looking for, hence the oracle must be representative of the Boolean formula to find a matching input.

## Documentation

Documentation can be found in the docs directory, that contains documentation on:

* Prerequisites
* Introduction to SAT
* Grover sat solver

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

## Future plans

More long term plans:

* Add documentation.
* Iteratively clean up code and documentation.
* One of the faster classical SAT solver algorithms solves 3-SAT problems with a time-complexity that scales as O((4/3)^n) for n literals [2], which at first glance is faster than the O( sqrt(2^n)) time-complexity of Grover's algorithm. However, the algorithm discussed here is based on a probabilistic result. It is shown that a correct solution is found with a probability scales as (t/(2*(t-1)))^n for a t-sat cnf. Thus, the number of solutions k scales (t/(2*(t-1)))^n 2^n, while the number of entries is N=2^n. The time complexity of Grover's algorithm with multiple solutions is O(sqrt(N/k)), thus in this case it becomes O(sqrt((t/(2*(t-1)))^n)). Or for a 3-sat cnf it is O(sqrt((4/3)^n)), which is O(1.15^n) compared to the O(1.33^n) found in the paper. Might this indicate a quadratic or almost quadratic speed up? Want to look into this deeper.
* Also want to see if symmetries lead to a more favorable time-complexity, since symmetries often give rise to multiple solutions. Because otherwise symmetry is not preserved.

## References

[1]: Grover, L. K. (1996, July). A fast quantum mechanical algorithm for database search. In Proceedings of the twenty-eighth annual ACM symposium on Theory of computing (pp. 212-219).

[2]: Schöning, U. (2002). A probabilistic algorithm for k-SAT based on limited local search and restart. Algorithmica, 32(4), 615-623.
