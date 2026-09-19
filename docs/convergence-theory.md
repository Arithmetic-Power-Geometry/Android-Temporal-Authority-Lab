# Convergence Lab: Decision-Relative Authority Closure

## Why TAC alone is insufficient

Temporal Authority Closure (TAC) asks whether previously issued authority remains effective after its justification changes. That is an important security question, but adjacent work already studies stale authorization, revocation, effect-time checks, and temporal capabilities.

The lab therefore treats TAC as the **platform testbed**, not as a novelty claim by itself.

## Stronger candidate: Decision-Relative Authority Closure (DRAC)

Let C be a current equivalence class of possible worlds that remain observationally compatible with the evidence so far.

Each world w has a required authorization decision g(w).

C is **decision-incompatible** when there exist wi,wj in C with g(wi) != g(wj).

A probe e is **decision-neutral admissible on C** iff executing e is admissible in every world in C without assuming which disputed authorization decision is correct.

A probe safely separates C when:

1. it is decision-neutral admissible on C; and
2. its outcomes partition C into leaves on which g is constant.

Define SafeSep(C) as the minimum cost of an adaptive probe tree whose every probe is decision-neutral admissible on the current branch and whose leaves are decision-compatible.

## Candidate obstruction theorem

If C is decision-incompatible and no decision-neutral admissible probe tree separates C, then no policy that refuses to presuppose the disputed authorization decision can always resolve the authorization question from within C.

This is intentionally framed as a theorem candidate, not as an established breakthrough.

## Why this is stronger than ordinary stale-authority logic

TAC asks: "Did old authority persist too long?"

DRAC asks: "Can the system even obtain the missing evidence needed to decide authority, if obtaining that evidence itself may already require the disputed authority?"

That creates a recursive epistemic/authorization boundary that should be attacked from:

- epistemic logic and knowledge-based systems,
- active sensing / POMDPs,
- safe exploration,
- capability security and revocation,
- access-control decision systems,
- Blackwell informativeness / experiment comparison,
- control theory and dual control,
- formal verification,
- distributed systems / stale state,
- philosophy of action and justified intervention.

## Convergence rule

A claim is promoted only if all are true:

- mathematically precise;
- survives counterexample search;
- not subsumed by known theory under straightforward relabeling;
- implemented as executable finite models;
- tested against randomized adversarial instances;
- has at least one domain-specific consequence on Android;
- has at least one second-domain consequence outside Android;
- includes a clear falsifier.

The software must be able to return **KILLED**. Failure to kill a claim is not proof of novelty.
