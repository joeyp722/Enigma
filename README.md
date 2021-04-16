# Grover SAT solver
The aim of this project is to build a quantum algorithm that can solve SAT problems. SAT refers to satisfiability of a Boolean formula, meaning that there exists a input where the output of the formula is TRUE.

Grover refers to Grover's algorithm from quantum computing [1]. This algorithm uses an oracle to find the states it is looking for, hence the oracle must be representative of the Boolean formula to find a matching input.

## Boolean formulas

There are three types of Boolean operators:
* conjunctions denoted by ^, think of AND gates.
* disjunctions denoted by v, think of OR gates.
* negations denoted by -, think of NOT gates.

A formula might look like:

> f = (-x0 v x1)^(x0 v -x1)

This is the formula for an XOR gate. The x variables here are the literals, these are the inputs of the Boolean formula and can be TRUE of FALSE. Here f is the output that can be TRUE or FALSE as well.

Note that here the disjunctions are within the brackets, where the conjunctions are outside of the brackets. When the formula is in this form it is called the conjunctive normal form (cnf), here the expressions within the brackets are called clauses. Often the Tseytin transformation is used to convert a arbitrary Boolean formula to such a form.

In order to satisfy the formula one must find a input that where the output is TRUE as a result.

## NP-Complete problems

NP-Complete is a complexity class in which the problem P must obey two criteria:

* Must be in NP.
* Every problem in NP must be reducible to P within polynomial time.

For a problem to be in the NP complexity class the solution to the problem must must verifiable in polynomial time.

Polynomial time refers to polynomial time complexity, where time complexity refers to the number of steps a algorithm has to take to get to the answer. When there are n literals the time complexity might scale as O(n), O(n^2), O(n^3), ... . But not as O(2^n), since this is exponential time complexity.

Cook [2] showed that SAT problems are NP-Complete. Thus, according to the first criterion it is possible to see if a given input gives TRUE as the output, within polynomial time.

Karp [3] showed that many combinatorial problems can also be reduced to SAT problems, again within polynomial time. Thus, if one can solve SAT problems one can also solve other NP-Complete problems.

## Oracle

In order for the oracle to work all the states of interest must receive a phase-flip, meaning that the coefficient in the state vector is multiplied with -1.

The oracle is always succeeded by a diffuser. This part of the algorithm can be repeated multiple times depending on the number of iterations.

In order to construct an oracle for a cnf. All the clauses have their own ancilla qubit on which a bit-flip is performed if the clause is TRUE. If a clauses are true then a phase-flip is performed via a quantum AND gate, again via a new ancillary qubit that provides a phase kickback.

Note that the bit-flips on the ancilla qubits have to be undone, thus the gates responsible for this are performed once more.

To gain a better understanding i would suggest looking at:

> cnf_oracle.py

Or it's subroutine counterpart:

> enigma.quantum_gates.cnf_oracle


## Multiple solutions

The required number of iterations for Grover's algorithm is pi/4 sqrt(N/k), where N is the number of entries given by the number of literals n, via N = 2^n. And where k is the number of solutions.

However, if the number of solutions is unknown the number of iterations should be guessed. Fortunately, there is a algorithm [4] that does this with sacrificing the time complexity. This algorithm is used in the code.

## Further remarks

I hope the idea became clear even though the documentation is perhaps rather primitive. The two main take away points are:

* The oracle works via phase kickback from ancilla qubits.
* Not knowing how many solutions there are doesn't matter for the time complexity. It is still O( sqrt(N/k) )

The heart of the algorithm lies in the functions:

* enigma.quantum_gates.cnf_oracle
* enigma.quantum_algorithms.grover_sat_solver

## Future plans

Short term plans:

* Research how to organize the code better.
* Organize the code better.
* Research how jupyter notebooks work.

Intermediate term plans:

* Make jupyter notebooks, that function as documentation.

More long term plans:

* Investigate the quantum adders, from the paper [5].
* Research if quantum adders can be used as counters. To see how many clauses are activated, this way the number of required ancilla qubits scales logarithmically instead of linearly. Here phase kickback is provided if the right number of clauses are activated.
* Research if it is useful to ignore some qubits from the counter, perhaps a phase kickback can also be provided if the number of activated clauses is greater or equal to some value. For example consider the counter literals x2 x1 x0. If x2 = True then the value of the counter is greater than or equal to 4. And also how this works for values other than powers of 2.
* Investigate if this can be used to solve MAX-SAT and weighted MAX-SAT problems.
* And if it all works out documenting everything to make it more comprehensive.

## References

[1]: Grover, L. K. (1996, July). A fast quantum mechanical algorithm for database search. In Proceedings of the twenty-eighth annual ACM symposium on Theory of computing (pp. 212-219).

[2]: Cook, S. A. (1971, May). The complexity of theorem-proving procedures. In Proceedings of the third annual ACM symposium on Theory of computing (pp. 151-158).

[3]: Karp, R. M. (1972). Reducibility among combinatorial problems. In Complexity of computer computations (pp. 85-103). Springer, Boston, MA.

[4]: Boyer, M., Brassard, G., Høyer, P., & Tapp, A. (1998). Tight bounds on quantum searching. Fortschritte der Physik: Progress of Physics, 46(4‐5), 493-505.

[5]: Draper, T. G. (2000). Addition on a quantum computer. arXiv preprint quant-ph/0008033.
