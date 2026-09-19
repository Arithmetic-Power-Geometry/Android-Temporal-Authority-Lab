"""Synthetic defensive benchmark: local authorization tests vs temporal sequence tests.

No platform exploit logic. Models only abstract state machines and synthetic resources.
"""
from dataclasses import dataclass
from itertools import product

@dataclass(frozen=True)
class Model:
    revoke_on_transition: bool
    recheck_on_use: bool

def run(m:Model):
    # S0: policy permits acquisition. S1: equivalent new acquisition is denied.
    acquired=True
    capability_live=acquired
    # transition S0 -> S1
    if m.revoke_on_transition: capability_live=False
    reacquire_allowed=False
    # old capability use
    old_use_allowed=capability_live and (not m.recheck_on_use)
    if capability_live and m.recheck_on_use:
        old_use_allowed=False
    return {
      "s0_acquire":True,
      "s1_reacquire":reacquire_allowed,
      "s1_old_use":old_use_allowed,
      "sequence_gap":(not reacquire_allowed) and old_use_allowed
    }

def conventional_local_suite(m:Model):
    r=run(m)
    # Conventional checks test acquisition under each current state.
    return r["s0_acquire"] is True and r["s1_reacquire"] is False

def sequence_suite(m:Model):
    return not run(m)["sequence_gap"]

def census():
    rows=[]
    for rev,recheck in product((False,True),repeat=2):
      m=Model(rev,recheck);r=run(m)
      rows.append({"revoke":rev,"recheck":recheck,
                   "local_pass":conventional_local_suite(m),
                   "sequence_pass":sequence_suite(m),**r})
    return rows

if __name__=="__main__":
    for r in census():print(r)
