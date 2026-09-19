"""Minimal authorization-deadlock certificates and probe-cut witnesses."""
from itertools import combinations
from lab.authority_fixedpoint import authority_deadlock_kernel

def minimal_deadlocks(decisions,probes):
    dead=set(authority_deadlock_kernel(decisions,probes))
    return frozenset(C for C in dead if not any(D<C for D in dead))

def separating_probes(C,decisions,probes):
    """Probes that split at least one pair requiring different decisions."""
    out=[]
    for p in probes:
      useful=False
      for i,j in combinations(C,2):
        if decisions[i]!=decisions[j] and p.outcomes[i]!=p.outcomes[j]:
          useful=True;break
      if useful: out.append(p)
    return out

def permission_blockers(C,decisions,probes):
    """For each useful probe, worlds in C that prohibit it."""
    return {p.name:frozenset(i for i in C if not p.admissible[i])
            for p in separating_probes(C,decisions,probes)}

def circularity_certificate(C,decisions,probes):
    """A diagnostic certificate, not yet a theorem of minimal duality."""
    blockers=permission_blockers(C,decisions,probes)
    return {
      "worlds":tuple(sorted(C)),
      "decisions":tuple(decisions[i] for i in sorted(C)),
      "useful_probe_blockers":{k:tuple(sorted(v)) for k,v in blockers.items()},
      "all_useful_probes_blocked":bool(blockers) and all(blockers.values()),
    }
