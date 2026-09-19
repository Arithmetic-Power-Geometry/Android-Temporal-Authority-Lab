# Adaptive Authority Fixed-Point Theory (AAFT)

## Construction

Let B be the finite lattice of nonempty belief/world sets. Let T be the terminal sets on which the required authorization decision g is constant.

Define the monotone operator

F(K) = T union { C : there exists probe e such that
                 e is admissible in every w in C,
                 e produces a nontrivial partition Succ(C,e),
                 and every C' in Succ(C,e) belongs to K }.

The least fixed point K* obtained by iteration from T is the **authority-resolution kernel**.
Its complement among decision-mixed belief sets is the **authority-deadlock kernel** D*.

## Fixed-point characterization theorem

For a finite deterministic model, C belongs to K* if and only if there exists a finite adaptive evidence tree that:
1. executes only probes jointly admissible in the current branch's remaining worlds; and
2. terminates at leaves on which g is constant.

### Proof sketch

Forward: membership enters at finite fixed-point iteration rank. Induct on rank. Rank zero is terminal. At rank k+1, the witnessing probe has successors of smaller rank; attach their inductively existing trees.

Reverse: induct on the height of any valid finite evidence tree. Leaves are terminal. At an internal node the root probe is jointly admissible and each child has a smaller valid tree, so all children enter an earlier iteration and the parent enters next.

Thus recursive safe separability is exactly a reachability fixed point on the belief lattice.

## Deadlock closure theorem

If C is in D*, then every jointly admissible probe either fails to refine C or has at least one successor still in D*. Therefore no compliant finite adaptive policy can force escape from D*.

This follows immediately from fixed-point complementarity: otherwise C would satisfy F(K*) and enter K*.

## Interpretation

D* is a viability-style obstruction in epistemic/authorization state space. It identifies uncertainty sets from which evidence sufficient for a correct authorization decision cannot be forced without either:
- acquiring new externally supplied evidence,
- changing the authorization policy,
- permitting abstention, or
- executing a probe whose admissibility is disputed.

## Novelty status

The fixed-point characterization is mathematically stronger than the earlier pair obstruction and correctly handles branch-relative admissibility. However, reachability/viability fixed points are standard mathematical machinery, and recursively constrained POMDPs already reason about history-dependent constraints. Therefore the fixed-point form itself is NOT declared a breakthrough.

The remaining novelty question is whether the coupling "the hidden state determines both the correct authorization decision and which information-gathering actions may legally/safely be used to identify that state" yields a distinct theorem or measurable phenomenon beyond a constrained belief-MDP encoding.
