"""Dual trap certificates for finite decision-relative authority problems."""
from dataclasses import dataclass
from itertools import combinations
from lab.authority_fixedpoint import Probe,least_resolvable_fixedpoint,terminal,admissible,successors

def allsets(n):
    for r in range(1,n+1):
      for c in combinations(range(n),r): yield frozenset(c)

def deadsets(decisions,probes):
    K=least_resolvable_fixedpoint(decisions,probes)
    return {C for C in allsets(len(decisions)) if not terminal(C,decisions) and C not in K}

def trap_witness(C,decisions,probes):
    """For each admissible refining probe choose a deadlocked successor."""
    D=deadsets(decisions,probes)
    if C not in D:return None
    witness={}
    for p in probes:
      if not admissible(C,p): continue
      S=successors(C,p)
      if len(S)<=1: continue
      bad=[s for s in S if s in D]
      if not bad:return None
      witness[p.name]=min(bad,key=lambda x:(len(x),tuple(sorted(x))))
    return witness

def verify_trap(C,witness,decisions,probes):
    D=deadsets(decisions,probes)
    if C not in D:return False
    by={p.name:p for p in probes}
    for p in probes:
      if admissible(C,p) and len(successors(C,p))>1:
        if p.name not in witness:return False
        if witness[p.name] not in successors(C,p):return False
        if witness[p.name] not in D:return False
    return True

def minimal_trap_certificates(decisions,probes):
    D=deadsets(decisions,probes)
    mins=[C for C in D if not any(E<C for E in D)]
    return [(C,trap_witness(C,decisions,probes)) for C in mins]
