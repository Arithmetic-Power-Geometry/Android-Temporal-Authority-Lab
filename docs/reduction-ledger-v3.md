# Reduction ledger v3: adaptive authority fixed point

## Attack 1: recursively constrained POMDPs

RC-POMDPs impose history-dependent constraints and recover optimal substructure. Our finite DREA problem can be encoded as a belief-state planning problem with action feasibility determined by the support of the current belief. Therefore the mere existence of a recursive Bellman/fixed-point solution is not novel.

Verdict: FIXED-POINT FORM REDUCED TO KNOWN GENERAL MACHINERY.

## Attack 2: epistemic planning and sensing actions

Epistemic planning already constructs observation-contingent policies and supports sensing actions with preconditions. Thus "branch on observations and only execute enabled sensing actions" is also established general machinery.

Verdict: ADAPTIVE SENSING TREE NOT NOVEL BY ITSELF.

## Attack 3: belief-dependent safety constraints

Modern constrained belief-space planning explicitly supports constraints depending on the belief. Our joint-admissibility condition is representable as a hard belief-support constraint.

Verdict: REPRESENTABILITY IS NOT A NOVELTY ARGUMENT.

## What survives?

A domain-specific interpretation survives: the same latent proposition controls (i) which terminal authorization decision is correct and (ii) whether an evidence-producing action is itself authorized. This creates self-referential-looking epistemic deadlocks, but in finite models they are still representable using existing planning machinery.

## Current scientific conclusion

No field-level theoretical breakthrough has survived the reduction attacks so far.

The DREA/AAFT vocabulary may still be useful as a security specification pattern, diagnostic metric, or application of established machinery. A publishable contribution would now require one of:

1. a complexity separation caused specifically by decision-relative admissibility;
2. an impossibility/duality theorem not inherited immediately from belief-state reachability;
3. empirical discovery of a real authorization failure class predicted by the theory;
4. a demonstrably more efficient algorithm exploiting special DREA structure.

Until one of these is established, STOP LABEL = NO_BREAKTHROUGH_CONTINUE.
