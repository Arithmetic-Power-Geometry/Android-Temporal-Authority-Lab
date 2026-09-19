# Empirical Prediction: Local-Pass / Sequence-Fail

## Prediction

A test regime that checks only whether an equivalent authority can be acquired in each state can pass while failing to detect that authority acquired earlier remains usable after the policy state changes.

Synthetic witness:

1. S0 permits capability acquisition.
2. transition to S1.
3. S1 correctly denies equivalent reacquisition.
4. the previously acquired capability remains effective.
5. therefore all local acquisition checks pass, while the transition sequence fails the temporal authority invariant.

## Why this matters

This is not a claim of an Android vulnerability. It is a benchmark-level prediction about test coverage.

The discriminating experiment compares:
- Local suite: test fresh authorization independently in S0 and S1.
- Sequence suite: acquire in S0, transition, exercise old authority in S1, and compare with fresh reacquisition in S1.

The theory predicts a strict coverage separation whenever authority lifetime crosses a state transition without revocation or use-time revalidation.

## Breakthrough status

The synthetic separation is real but elementary. Temporal/capability revocation is established security territory. Therefore this benchmark does NOT by itself establish a breakthrough.

A stronger empirical result would require a reproducible, nontrivial platform behavior on owned/emulated devices where:
- documented semantics predict authority should not survive;
- conventional state-local tests pass;
- sequence differential testing reveals persistence;
- the effect crosses a meaningful security boundary;
- the result survives current supported builds and independent reproduction.

Until then: NO BREAKTHROUGH.
