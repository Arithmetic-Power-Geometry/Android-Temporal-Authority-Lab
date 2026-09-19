from lab.authority_fixedpoint import Probe
from lab.deadlock_certificate import *

def test_two_world_circularity_certificate():
    d=("deny","allow")
    ps=[Probe("learn",("0","1"),(False,True))]
    m=minimal_deadlocks(d,ps)
    assert frozenset({0,1}) in m
    c=circularity_certificate(frozenset({0,1}),d,ps)
    assert c["all_useful_probes_blocked"]
    assert c["useful_probe_blockers"]["learn"]==(0,)

def test_safe_probe_destroys_minimal_deadlock():
    d=("deny","allow")
    ps=[Probe("learn",("0","1"),(True,True))]
    assert minimal_deadlocks(d,ps)==frozenset()
