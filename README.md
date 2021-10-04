# Grover SAT solver
The aim of this project is to build a quantum algorithm that can solve SAT problems. SAT refers to satisfiability of a Boolean formula, meaning that there exists a input where the output of the formula is TRUE.

Grover refers to Grover's algorithm from quantum computing [1]. This algorithm uses an oracle to find the states it is looking for, hence the oracle must be representative of the Boolean formula to find a matching input.

## Documentation

Documentation can be found in the docs directory, that contains documentation on:

* Prerequisites
* Introduction to SAT
* Grover sat solver
* Proposition for Gaussian elimination SAT solver algorithm

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
* One of the faster classical SAT solver algorithms solves 3-SAT problems with a time-complexity that scales as O((4/3)^n) for n literals [2], which is indeed faster for 3-SAT problems. The reason for this is that it takes advantage of the structure in the CNF. However, according to the paper the time-complexity, O((2(k-1)/k)^n), gets worse when the value of k gets larger. Here k refers to the k in k-SAT. Because Grover's algorithm has a time-complexity of O(sqrt(2^n)) it might be faster for larger values of k. Also consider that k-SAT can be converted to 3-SAT, this however usually introduces more literals, thus is not necessarily faster. All this seems to indicate some threshold of k that separates the advantages of this classical algorithm and Grover's algorithm. The paper assumes the CNF has one solution.    
* Also want to see if symmetries lead to a more favorable time-complexity, since symmetries could give rise to multiple solutions. Because in some cases different solutions could arise from symmetric transformations. For example a literal permutation between x0 and x1 gives one extra solution for 0100 that is 1000, where x0 x1 x2 x3. But not for 1100, since it remains the same, being 1100.
* Does this work?. Fails for random 3-sat cnf's. Not sure if it can be fixed or not. Seems to fail when number of clauses increases.

Proposition for new classical algorithm that converts Boolean 3-SAT formulas to a set of linear equations, that are then solved by Gaussian elimination. The solutions to the linear equations should yield the solution to the 3-SAT problem.

See this doc file for more information:

> gaussian_sat_solver_algorithm.ipynb

And the test file and library that are still under construction:

> test_gauss.py

> enigma.gauss.py

* Just as classical NP-Complete problems exist quantum QMA-Complete problems also exist, one example of these problems is finding the ground state for a k-local Hamiltonian [3].
* Is it possible to build a verifier that performs a bit-flip when the correct state is found, while the ancilla remains unchanged for an incorrect state? If a superposition of correct and incorrect states in fed into the verifier will the following entanglement happen: |"Incorrect states">|0>+|"Correct states">|1> ? One might choose such a superposition in the beginning. However, if one measures the ancilla state |1>, then the superposition automatically collapses to the "Correct" state.
* A drawback of the method above might be that the probability of measuring the |1> state might be very low. This probability might be increased by applying Grover's algorithm before verification.
* The same verifier might be used as an Oracle by performing a phase-flip instead of a bit-flip.
* Normally the eigenstates of an Oracle are in the Z-basis. In beginning the Hadamard transformation is used to transform the vacuum state to a superposition of all the relevant eigenstates. From now on a transformation from the vacuum state to a superposition of eigenstates is defined by the transformation M : |"vacuum"> -> |s>.
* In the case of the diffuser the inverse transformation of M is performed first, then the vacuum state receives a phase-flip, and finally the transformation M is applied again.
* However, a verifier Oracle might have different eigenstates, thus could also use a different transformation. If M: |"vacuum"> -> |s>, then |s> must contain at least one the "Correct" states, since it is one of the relevant eigenstates we where looking for.
* To build a verifier that can verify if the eigenenergy of an eigenstate is below a certain value the phase estimation algorithm might be used.
* By measuring the qubit that represents the divide between the upper and lower part of the range first. It can decided if the energy is in the upper or lower part of the range. The upper and lower parts can again be divided into their own upper and lower parts (quadrants), this is represented by the output second qubit. Thus, by running the algorithm once one can decide in what half of the range the energy lies. By running the algorithm again but by measuring the second output qubit instead, one can decide in what quadrant the energy lies. So by induction it performs like a binary search.
* In order to combine multiple constraints one might use quantum AND and OR gates. The input qubits for these gates are the output qubits of the verifiers.
* The effect of different verifiers might also be compared with each other. When a extra qubit is introduced to activate verifier 1 when in the |0> state and verifier 2 when in the |1> state the quadratic speed up provided by Grover's algorithm might be utilized, since the introduced qubit is part of the Hilbert space which the Oracle acts on. Note that more verifiers might be added as well. However, they all must use the same transformation M. Thus, this feature might be used to compare Hamiltonian's that have minor differences among them.

## References

[1]: Grover, L. K. (1996, July). A fast quantum mechanical algorithm for database search. In Proceedings of the twenty-eighth annual ACM symposium on Theory of computing (pp. 212-219).

[2]: Schöning, U. (2002). A probabilistic algorithm for k-SAT based on limited local search and restart. Algorithmica, 32(4), 615-623.

[3]: Bookatz, A. D. (2012). QMA-complete problems. arXiv preprint arXiv:1212.6312.
