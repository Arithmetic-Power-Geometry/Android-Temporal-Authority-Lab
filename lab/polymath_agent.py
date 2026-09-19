"""Adversarial multi-lens theory-convergence engine.

This is deliberately not an LLM simulator. Each "agent" is an independently
checkable mathematical lens. A candidate survives only if all applicable
falsifiers fail to kill it.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations
from typing import FrozenSet, Iterable

@dataclass(frozen=True)
class World:
    name: str
    decision: str

@dataclass(frozen=True)
class Probe:
    name: str
    admissible: FrozenSet[str]
    outcome: tuple[tuple[str,str], ...]
    cost: int = 1
    def observe(self,w:str)->str:
        return dict(self.outcome)[w]

@dataclass(frozen=True)
class Problem:
    worlds: tuple[World,...]
    probes: tuple[Probe,...]

def decision_mixed(names: Iterable[str], p: Problem)->bool:
    d={w.decision for w in p.worlds if w.name in set(names)}
    return len(d)>1

def neutral(probe:Probe, names:FrozenSet[str])->bool:
    """Probe is decision-neutral admissible iff it is allowed in every still-possible world."""
    return names <= probe.admissible

def refine(names:FrozenSet[str], probe:Probe)->list[FrozenSet[str]]:
    buckets={}
    for n in names:
        buckets.setdefault(probe.observe(n),set()).add(n)
    return [frozenset(v) for v in buckets.values()]

def safe_separable(p:Problem, names:FrozenSet[str]|None=None, seen=None)->bool:
    names=names or frozenset(w.name for w in p.worlds)
    if not decision_mixed(names,p): return True
    seen=seen or frozenset()
    key=tuple(sorted(names))
    if key in seen: return False
    for e in p.probes:
        if neutral(e,names):
            children=refine(names,e)
            if len(children)>1 and all(safe_separable(p,c,seen|{key}) for c in children):
                return True
    return False

def obstruction_kernel(p:Problem)->list[tuple[str,str]]:
    """Minimal pair witnesses: different decisions and no neutral probe separates them."""
    out=[]
    for a,b in combinations(p.worlds,2):
        if a.decision==b.decision: continue
        pair=frozenset((a.name,b.name))
        if not any(neutral(e,pair) and e.observe(a.name)!=e.observe(b.name) for e in p.probes):
            out.append((a.name,b.name))
    return out

def lens_report(p:Problem)->dict[str,object]:
    root=frozenset(w.name for w in p.worlds)
    return {
      "logic_consistency": all(w.name for w in p.worlds),
      "information_separable_ignoring_authority": any(
          len({e.observe(w.name) for w in p.worlds})>1 for e in p.probes),
      "authorization_safe_separable": safe_separable(p,root),
      "minimal_obstruction_pairs": obstruction_kernel(p),
      "physics_lens": "state transition must preserve admissibility invariant before protected effect",
      "philosophy_lens": "knowledge cannot justify the act used to obtain it when that act presupposes the disputed justification",
      "distributed_systems_lens": "local evidence is insufficient if admissibility differs across indistinguishable global states",
    }
