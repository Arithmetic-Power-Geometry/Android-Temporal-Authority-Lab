from __future__ import annotations
from dataclasses import dataclass, field
from typing import Iterable, FrozenSet, List

@dataclass(frozen=True)
class World:
    name: str
    decision: str
    observations: tuple
    admissible_probes: FrozenSet[str] = field(default_factory=frozenset)

def decision_incompatible_class(worlds: Iterable[World]) -> bool:
    return len({w.decision for w in worlds}) > 1

def decision_neutral_admissible(worlds: Iterable[World], probe: str) -> bool:
    ws=list(worlds)
    return bool(ws) and all(probe in w.admissible_probes for w in ws)

def separates_decisions(worlds: List[World], outcomes: List[str]) -> bool:
    if len(worlds)!=len(outcomes): raise ValueError("world/outcome length mismatch")
    buckets={}
    for w,o in zip(worlds,outcomes): buckets.setdefault(o,set()).add(w.decision)
    return len(buckets)>1 and all(len(ds)<=1 for ds in buckets.values())

def safe_separating_probe(worlds: List[World], probe: str, outcomes: List[str]) -> bool:
    return decision_incompatible_class(worlds) and decision_neutral_admissible(worlds,probe) and separates_decisions(worlds,outcomes)

def _safe_tree(worlds: List[World], probes: dict[str,List[str]], indices: tuple[int,...], seen:frozenset)->bool:
    live=[worlds[i] for i in indices]
    if not decision_incompatible_class(live): return True
    if indices in seen: return False
    for probe, outcomes in probes.items():
        if not decision_neutral_admissible(live,probe): continue
        buckets={}
        for i in indices: buckets.setdefault(outcomes[i],[]).append(i)
        if len(buckets)<=1: continue
        if all(_safe_tree(worlds,probes,tuple(v),seen|{indices}) for v in buckets.values()):
            return True
    return False

def unresolved_authority_obstruction(worlds: List[World], probes: dict[str,List[str]]) -> bool:
    """True iff no adaptive decision-neutral probe tree resolves the live worlds."""
    if any(len(v)!=len(worlds) for v in probes.values()):
        raise ValueError("every probe outcome vector must align with worlds")
    return not _safe_tree(worlds,probes,tuple(range(len(worlds))),frozenset())
