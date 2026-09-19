# Authority Trap Duality

For a finite deterministic DREA instance, let K* be the least fixed point of safely resolvable belief sets and D* its decision-mixed complement.

## Dual certificate theorem

A decision-mixed belief C is deadlocked iff there exists a closed trap family containing C such that for every belief B in the family and every jointly admissible probe at B, either:

1. the probe does not refine B; or
2. at least one possible observation successor remains in the trap family.

This is the dual of the resolution attractor.

### Proof

If B is outside K*, then by complementarity it cannot have an admissible refining probe all of whose successors lie in K*. Hence every admissible refining probe has a successor outside K*. Iterating this choice gives a closed trap.

Conversely, if such a trap contains C, no finite evidence tree can force a terminal decision-homogeneous leaf on every observation branch: at every admissible refining node the environment can select a successor still in the trap. Therefore C is not safely resolvable.

## Scientific assessment

This theorem gives machine-checkable counter-certificates: a successful policy is a proof of resolvability; a closed trap is a proof of deadlock.

However, attractor/trap duality and AND/OR winning/losing certificates are standard in games and verification. Therefore this duality is **NOT a breakthrough by itself**.

## Authorization-specific semantic layer

What is distinctive is the interpretation of disabled actions: a probe is unavailable not because of physics or scheduler choice, but because at least one unresolved world says executing that evidence-producing action would itself be unauthorized. This produces a useful audit certificate:

- unresolved worlds;
- incompatible required decisions;
- evidence actions considered;
- authorization blockers;
- adversarial observation successor preserving uncertainty.

This may be publishable as an application/security diagnostic if it predicts failures conventional authorization testing misses, but it does not clear the theory breakthrough gate.

## Next route

The theoretical routes have now repeatedly reduced to established machinery. The next high-value experiment is empirical and defensive: construct synthetic authorization state machines and compare conventional per-state/per-action tests against DREA sequence tests. Search for cases where every individual state/action check passes locally, yet a sequence exposes an unresolved-authority circularity or stale delegated authority.
