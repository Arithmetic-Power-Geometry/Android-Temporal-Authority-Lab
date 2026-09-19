# Reduction ledger v2

## Candidate: authority-information reversal

**Status: REDUCED / NOT BREAKTHROUGH.**

The observation that more raw information can be less useful after feasibility constraints is imposed is too close to existing constrained information-acquisition and endogenous-feasibility results to support a novelty claim.

## Survivor: safe-garbling restoration

For deterministic finite experiments E1,E2, suppose E1 refines E2. The ordinary "observe E1 then garble/ignore information to simulate E2" argument is operationally available under state-dependent authorization only when acquisition of E1 is admissible wherever acquisition of E2 is admissible.

Sufficient condition:

    E1 >=I E2
    and Adm(E2,w) => Adm(E1,w) for every w
    ------------------------------------------------
    E1 can serve as an authorized source for simulating E2 wherever E2 is authorized.

Failure witness: if some world authorizes E2 but not E1, ordinary Blackwell refinement alone cannot justify source-then-garble substitution in that world because the source acquisition is prohibited.

This is useful clarification, but currently appears to be a constrained-feasibility corollary rather than a field-level breakthrough.

## Strongest remaining DREA question

The potentially nontrivial object is not single-experiment ordering. It is **branch-relative admissibility of adaptive evidence acquisition when admissibility itself depends on unresolved decision-critical worlds**.

That recursive coupling remains the target. We do not claim novelty until a theorem about that adaptive structure survives explicit reduction to:
- recursively constrained POMDPs,
- history-dependent information choice,
- epistemic authorization logics,
- safe active sensing,
- constrained experiment comparison.

## Stop rule

Current state: CONTINUE RESEARCH. No paper-level breakthrough declared.
