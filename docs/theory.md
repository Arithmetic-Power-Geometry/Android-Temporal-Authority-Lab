# Theory: Temporal Authority Closure

## 1. State-relative authority

Model a system state as:

```
S = (principal, profile_state, process_state, boot_epoch, policy_state)
```

and a delegated capability as:

```
c = (issuer, holder, object, rights, creation_state, lifetime)
```

Define:

```
Valid(c, S) = Rights(c) AND Policy(c, S) AND Lifetime(c, S)
```

## 2. Temporal Authority Closure (TAC)

For a state transition `tau: S0 -> S1`, a system satisfies Temporal Authority Closure when every capability whose justification becomes false is either revoked or rendered unusable before protected effects can occur.

```
Justified(c,S0) AND NOT Justified(c,S1)
    => NOT Effective(c,S1)
```

## 3. Revocation-completeness gap

A candidate gap exists when creation checks and use checks are not equivalent across time:

```
CreateEquivalent(c,S1) = denied
UsePreviouslyCreated(c,S1) = allowed
```

This is the key differential oracle.

## 4. Novelty filter

A result is not automatically a vulnerability. Before promotion, test whether the behavior is:

1. documented,
2. intentionally persistent,
3. restricted to non-sensitive synthetic data,
4. reproducible on a fully updated supported build,
5. caused by the platform rather than the test app,
6. security-boundary relevant.

Only a result surviving all six filters becomes a disclosure candidate.
