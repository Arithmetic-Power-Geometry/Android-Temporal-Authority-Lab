# Minimal Authorization-Deadlock Certificates

A minimal deadlock is an inclusion-minimal decision-mixed belief set that lies outside the authority-resolution kernel.

For each such set C, construct a diagnostic map from every decision-separating probe to the worlds in C that prohibit that probe.

This yields a compact explanation of the circularity:

> these worlds require different authorization decisions; these probes could reveal which decision is correct; but each revealing probe is prohibited in at least one still-possible world.

For a two-world minimal deadlock this is already a complete obstruction certificate.

For larger adaptive problems, merely blocking every one-step decision-separating probe is not necessarily sufficient, because a nonterminal probe may first split C into smaller safely resolvable branches. Therefore we deliberately do NOT claim a general cut duality yet.

## Candidate next theorem

Seek an AND/OR hypergraph duality:

- OR nodes: choice among jointly admissible probes;
- AND nodes: all possible observation successors must resolve;
- terminal nodes: decision-homogeneous beliefs.

Resolution is existence of a finite winning AND/OR tree. Deadlock should admit a dual closed trap certificate selecting, for every admissible probe, at least one successor remaining in the trap.

This resembles standard game attractor/trap duality. The novelty burden is therefore to show an authorization-specific certificate with additional semantics or complexity advantage, not merely rename losing regions.

Current status: useful certificate machinery; NO BREAKTHROUGH.
