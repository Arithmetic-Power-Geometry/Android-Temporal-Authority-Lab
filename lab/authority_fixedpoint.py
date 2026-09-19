"""Greatest-fixed-point solver for recursively admissible evidence acquisition.

A belief set C is authority-resolvable when its required decision is already constant,
or some probe is admissible in every world of C and every observation successor is
itself authority-resolvable.  The fixed-point view exposes the viability kernel of
belief states from which correct authorization can be reached without ever executing
a probe whose permission depends on the unresolved world.
"""
from dataclasses import dataclass
from itertools import combinations

@dataclass(frozen=True)
class Probe:
    name:str
    outcomes:tuple[str,...]
    admissible:tuple[bool,...]

def subsets(n):
    for r in range(1,n+1):
        for c in combinations(range(n),r): yield frozenset(c)

def terminal(C,decisions):
    return len({decisions[i] for i in C})==1

def admissible(C,p):
    return all(p.admissible[i] for i in C)

def successors(C,p):
    b={}
    for i in C:b.setdefault(p.outcomes[i],set()).add(i)
    return tuple(frozenset(v) for v in b.values())

def least_resolvable_fixedpoint(decisions,probes):
    """Construct the least set closed under safe backward resolution."""
    K={C for C in subsets(len(decisions)) if terminal(C,decisions)}
    changed=True
    while changed:
        changed=False
        for C in subsets(len(decisions)):
            if C in K: continue
            for p in probes:
                S=successors(C,p)
                if admissible(C,p) and len(S)>1 and all(s in K for s in S):
                    K.add(C);changed=True;break
    return frozenset(K)

def authority_deadlock_kernel(decisions,probes):
    K=least_resolvable_fixedpoint(decisions,probes)
    return frozenset(C for C in subsets(len(decisions)) if not terminal(C,decisions) and C not in K)

def root_resolvable(decisions,probes):
    return frozenset(range(len(decisions))) in least_resolvable_fixedpoint(decisions,probes)

def critical_probe_witness(decisions,probes):
    """Find probes whose addition moves root from deadlocked to resolvable."""
    root=frozenset(range(len(decisions)))
    base=least_resolvable_fixedpoint(decisions,[])
    out=[]
    for p in probes:
        k=least_resolvable_fixedpoint(decisions,[p])
        if root not in base and root in k: out.append(p.name)
    return out
