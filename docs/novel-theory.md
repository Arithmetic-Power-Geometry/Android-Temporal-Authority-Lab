# Candidate theory: Decision-Relative Epistemic Authority (DREA)

## Problem

Ordinary observability asks whether worlds can be distinguished. Authorization asks whether an action is allowed. DREA couples them: **can the worlds be distinguished using only probes whose admissibility does not presuppose which unresolved authorization decision is correct?**

Let a decision-critical class C contain observationally compatible worlds and let g(w) be the required authorization decision. A probe e is **decision-neutral admissible** on C when e is admissible in every world in C without assuming the disputed value of g.

Define SafeSep(C) recursively: C is safely separable when either g is constant on C, or there exists a decision-neutral admissible probe whose outcome partitions C into children that are each safely separable.

## Candidate obstruction theorem

If C contains worlds w_i,w_j with g(w_i) != g(w_j), and every probe that distinguishes the pair is inadmissible in at least one of the two worlds, then no policy restricted to decision-neutral admissible probes can guarantee the correct authorization decision on C.

### Proof

Any compliant policy may execute only probes admissible in both worlds. By hypothesis none of those probes distinguishes w_i from w_j. Therefore the policy receives the same admissible observation history in both worlds. A deterministic policy must return the same decision in both; a randomized policy cannot guarantee two different required decisions with probability one. Since g differs, at least one world is decided incorrectly. QED.

## Stronger concept: Epistemic Authority Debt

For unresolved class C, define EAD(C) as the minimum total cost of probes required to make g constant at every leaf, with infinity when no decision-neutral admissible experiment tree exists.

This separates three cases:

1. EAD=0: current evidence already resolves authority.
2. 0<EAD<infinity: authority is resolvable at measurable information cost.
3. EAD=infinity: the system has an **authorization deadlock**; correctness requires either an external trusted oracle, a policy relaxation, or abstention.

This is a candidate research contribution, not yet a novelty claim. It must survive broader literature review, independent proof checking, larger exhaustive searches, and real-system experiments.

## Why it is not just revocation or value of information

Revocation asks whether previously granted authority remains effective. Value of information prices observations. DREA instead constrains the *admissible observation language itself* by unresolved authority and asks whether the authorization decision is identifiable inside that restricted language.

## Falsification targets

- Reduction to constrained POMDP/safe exploration without loss.
- Reduction to existing authorization logics or epistemic logic.
- Counterexample to the recursive SafeSep criterion.
- A protocol that guarantees correct decisions despite an obstruction pair without adding information, authority, or abstention.
