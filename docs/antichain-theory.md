# Downward Closure and Antichain Compression

## Theorem 1: Downward closure of safe resolvability

If a belief set C has a finite decision-neutral admissible evidence tree, then every nonempty subset D subseteq C also has such a tree.

### Proof

Restrict the tree to worlds in D. Every probe used at a node was admissible in every world remaining at that node in the C-tree, hence remains admissible after worlds are removed. Remove empty outcome branches. If restriction makes a node decision-homogeneous, terminate there. The resulting finite tree resolves D.

Therefore the family K* of safely resolvable belief sets is downward closed.

## Corollary: antichain representation

Every finite downward-closed family is uniquely determined by its maximal elements. Hence K* can be represented exactly by Max(K*), an antichain.

This can drastically reduce storage on structured instances, but worst-case antichains can still be exponentially large (Sperner phenomenon). Therefore this is an exact structural compression, not a polynomial-time breakthrough.

## Theorem 2: upward closure of deadlock

Among decision-mixed sets, if C is deadlocked and C subseteq D, then D cannot be safely resolvable; otherwise downward closure would imply C resolvable.

Caution: D may become decision-homogeneous only if the model changes; under ordinary subset inclusion with fixed decisions, a superset of a mixed set remains mixed.

## Research significance

The authority problem has a monotone geometry:
- resolvability flows downward under information gain;
- deadlock flows upward under added uncertainty.

This gives an exact antichain boundary between resolvable and deadlocked uncertainty.

The boundary can support symbolic algorithms, minimal deadlock certificates, and benchmark generation.

## Novelty status

Antichain methods and downward-closed state sets are well established in verification, games, and planning. Therefore the mathematical use of an antichain is NOT itself a breakthrough. The candidate contribution would require showing that the authorization semantics yields a new certificate, algorithmic advantage, or empirically meaningful boundary not already captured by those frameworks.
