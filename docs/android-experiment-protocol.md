# Android / Pixel experiment protocol

## Purpose

Produce reproducible evidence for or against TAC/DRAC without targeting third parties or using real private content.

## Phase A — emulator baseline

For each capability class already listed in the repository:

1. Create two lab apps: issuer and holder.
2. Use synthetic content generated inside the test profile.
3. Acquire the delegated capability in state S0.
4. Record a harmless read/effect confirming the capability works in S0.
5. Transition to S1 (for example lock, profile lock, process death, or reboot).
6. Attempt to acquire an equivalent fresh capability in S1.
7. Exercise the previously acquired capability in S1.
8. Record both results plus OS build, emulator/device class and repetitions.
9. Repeat enough times to distinguish deterministic behavior from race/noise.
10. Treat old-success/new-denial only as a candidate anomaly.

## Phase B — explanation kill tests

Before promotion, test:

- documented lifetime semantics;
- explicit persistence contract;
- app-side caching;
- process resurrection;
- profile/user boundary;
- reboot persistence;
- issuer behavior;
- target SDK differences;
- current supported build behavior.

## Phase C — DRAC test

For any live ambiguous state, list every probe that could distinguish the authorization decision. Mark whether each probe is admissible in every still-live world *without assuming the disputed decision*.

If every resolving probe is decision-dependent, record a DRAC obstruction candidate.

## Phase D — physical Pixel replication

Only after emulator evidence survives. Use an owned/authorized fully updated Pixel, synthetic accounts/data, and the same evidence schema. No exploit chaining, persistence, credential access, third-party targeting, or data exfiltration.

## Promotion

One observation never establishes a vulnerability or a new theory. Promotion requires reproducibility, security-boundary relevance, documentation review, prior-art review, and an explicit falsifier.
