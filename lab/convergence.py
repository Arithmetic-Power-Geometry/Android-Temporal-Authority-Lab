from __future__ import annotations
from dataclasses import dataclass, field
from typing import Iterable, FrozenSet, Tuple, List

@dataclass(frozen=True)
class World:
    name: str
    decision: str
    observations: tuple
    admissible_probes: FrozenSet[str] = field(default_factory=frozenset)

@dataclass(frozen=True)
class Probe:
    name: str
    outcomes: tuple  # aligned with worlds by caller

def decision_incompatible_class(worlds: Iterable[World]) -> bool:
    ws = list(worlds)
    return len({w.decision for w in ws}) > 1

def decision_neutral_admissible(worlds: Iterable[World], probe: str) -> bool:
    ws = list(worlds)
    return bool(ws) and all(probe in w.admissible_probes for w in ws)

def separates_decisions(worlds: List[World], outcomes: List[str]) -> bool:
    if len(worlds) != len(outcomes):
        raise ValueError("world/outcome length mismatch")
    buckets = {}
    for w, o in zip(worlds, outcomes):
        buckets.setdefault(o, set()).add(w.decision)
    return all(len(ds) <= 1 for ds in buckets.values()) and len(buckets) > 1

def safe_separating_probe(worlds: List[World], probe: str, outcomes: List[str]) -> bool:
    return (
        decision_incompatible_class(worlds)
        and decision_neutral_admissible(worlds, probe)
        and separates_decisions(worlds, outcomes)
    )

def unresolved_authority_obstruction(worlds: List[World], probes: dict[str, List[str]]) -> bool:
    """
    Returns True when worlds require different authorization decisions but every
    candidate resolving probe is either inadmissible in at least one live world
    or fails to separate the decision classes.
    """
    if not decision_incompatible_class(worlds):
        return False
    for probe, outcomes in probes.items():
        if safe_separating_probe(worlds, probe, outcomes):
            return False
    return True
