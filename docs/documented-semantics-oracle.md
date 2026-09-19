# Documented-Semantics Differential Oracle

## Why this layer is necessary

A Local-Pass / Sequence-Fail differential is not automatically a security flaw. Some Android authorities are intentionally persistent. For example, persistable URI permissions can survive reboot until explicit revocation. A benchmark that flags persistence without modeling documented lifetime would manufacture false positives.

The oracle therefore separates:

1. **Differential:** fresh equivalent authority is denied after transition while previously acquired authority remains effective.
2. **Contract:** public/documented semantics say whether the old authority should remain effective for the particular capability and transition.
3. **Sensitive effect:** the old authority actually reaches the protected synthetic resource.
4. **Classification:** expected behavior, stronger-than-required invalidation, inconclusive, or semantic-mismatch candidate.

## Important consequence

Temporal differential and semantic violation are distinct predicates.

    Differential != Vulnerability

A candidate anomaly requires both a differential and a bound contract predicting invalidation.

## Current research status

This is a methodological improvement over the earlier synthetic benchmark because it prevents expected persistent capabilities from being mislabeled. It is not itself a breakthrough.

The next empirical gate requires actual emulator/device observations on synthetic resources. GitHub Actions can verify the oracle and model logic, but ordinary hosted CI cannot establish Android/Pixel platform behavior unless an emulator/device execution environment is explicitly attached.
