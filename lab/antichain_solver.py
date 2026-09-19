"""Antichain solver for authority-resolution under downward-closed structure.

Key fact: safe resolvability is downward closed under subset inclusion.
Therefore it is enough to store maximal resolvable belief sets (an antichain),
rather than the entire family of resolvable subsets.
"""
from dataclasses import dataclass
from itertools import combinations

@dataclass(frozen=True)
class Probe:
    name:str
    outcomes:tuple[str,...]
    admissible:tuple[bool,...]

def powerset(n):
    for r in range(1,n+1):
      for c in combinations(range(n),r): yield frozenset(c)

def terminal(C,d): return len({d[i] for i in C})==1
def admissible(C,p): return all(p.admissible[i] for i in C)
def succ(C,p):
    b={}
    for i in C:b.setdefault(p.outcomes[i],set()).add(i)
    return tuple(frozenset(v) for v in b.values())

def maximize(family):
    fam=set(family)
    return frozenset(C for C in fam if not any(C<D for D in fam))

def covered(C,antichain): return any(C<=M for M in antichain)

def exact_antichain(decisions,probes):
    """Reference algorithm: fixed point represented only by maximal members."""
    n=len(decisions)
    A=maximize(C for C in powerset(n) if terminal(C,decisions))
    changed=True
    while changed:
      changed=False
      candidates=[]
      for C in powerset(n):
        if covered(C,A): continue
        for p in probes:
          S=succ(C,p)
          if admissible(C,p) and len(S)>1 and all(covered(s,A) for s in S):
            candidates.append(C);break
      B=maximize(set(A)|set(candidates))
      if B!=A:A=B;changed=True
    return A

def root_resolvable(decisions,probes):
    root=frozenset(range(len(decisions)))
    return covered(root,exact_antichain(decisions,probes))

def downward_closure_check(decisions,probes):
    A=exact_antichain(decisions,probes)
    return all((not covered(C,A)) or all(covered(D,A) for r in range(1,len(C)+1)
        for D in combinations(C,r)) for C in powerset(len(decisions)))
