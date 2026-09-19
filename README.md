# Android Temporal Authority Lab

A defensive Android/Pixel security research laboratory for studying whether delegated authority remains valid after the security state that justified it has changed.

## Central hypothesis

Let `c` be a capability, `S0` an authorization state, and `S1` a later state in which the original authorization predicate no longer holds.

The security invariant is:

```
Authorized(c, S0) does not imply Authorized(c, S1)
```

A candidate failure exists when:

```
Acquire(c, S0)
  -> transition S0 -> S1
  -> exercise(c)
  -> access succeeds
```

while acquiring equivalent authority directly in `S1` is denied.

## Research method

The lab uses a zig-zag loop:

1. Formalize a claimed security invariant.
2. Generate a narrow falsifiable hypothesis.
3. Test only on owned/emulated devices and synthetic data.
4. Record observations as structured evidence.
5. Reject explanations already covered by documentation or expected behavior.
6. Refine the surviving hypothesis.
7. Never publish exploit details before responsible disclosure.

## Initial capability classes

- URI/content grants
- PendingIntent / IntentSender
- Binder-mediated delegated handles
- Document / photo picker grants
- foreground / while-in-use authorization state

## Initial transitions

- unlocked -> locked
- unlocked -> locked -> unlocked
- unlocked -> process death
- unlocked -> reboot

## Safety

This repository is for defensive security research only. Tests must use devices, accounts, applications, and data you own or are explicitly authorized to test. Do not target third parties, exfiltrate real user data, bypass access controls outside the lab, or deploy exploit chains.

See `SECURITY.md`.
