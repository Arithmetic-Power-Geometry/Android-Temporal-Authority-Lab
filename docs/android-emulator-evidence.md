# Android emulator evidence gate

This directory adds the first real Android execution layer to the temporal-authority lab.

## Scientific purpose

The initial experiment is deliberately a **documented baseline**, not a vulnerability hunt. It checks whether the CI/emulator pipeline can reproduce a known Android security boundary before any unexpected observation is trusted.

The baseline records:

1. successful construction of an immutable package-scoped PendingIntent; and
2. the Android 14+ restriction on creating mutable PendingIntents around implicit intents for a modern target SDK.

A cross-version difference that matches Android documentation is labelled **EXPECTED_BASELINE**, never a vulnerability.

## Safety boundary

- owned GitHub-hosted Android emulator only;
- this package only;
- synthetic intent actions only;
- no third-party packages;
- no credentials, personal data, exfiltration, persistence, privilege escalation, or exploit delivery.

## Evidence ladder

An observation can advance only through:

EMULATOR_OBSERVED -> REPRODUCED -> CONTRACT_MISMATCH -> SECURITY_BOUNDARY_EFFECT -> PRIOR_ART_CLEARED -> CANDIDATE_BREAKTHROUGH

A CI crash, emulator hang, flaky test, documented behavior, or test-app bug stops below CONTRACT_MISMATCH.

## Next experiment after baseline

Only after the baseline runs reproducibly do we add lifecycle experiments for temporary URI authority using two synthetic packages. That phase must compare old authority, fresh equivalent authority, and the public Android lifetime contract after a precisely named transition.
