# Test Matrix

| Capability | Acquire state | Transition | Re-acquire in target state | Exercise old capability | Candidate anomaly |
|---|---|---|---|---|---|
| URI grant | unlocked | lock | expected deny | measure | old succeeds / new denied |
| PendingIntent | unlocked | lock | expected deny or constrained | measure | privileged effect persists |
| Binder handle | unlocked | process/profile transition | expected unavailable | measure | protected operation persists |
| Picker grant | unlocked | lock | expected deny | measure | protected content remains readable |
| while-in-use auth | foreground | background/lock | expected deny | measure | operation still succeeds |

Every test must use synthetic content.
