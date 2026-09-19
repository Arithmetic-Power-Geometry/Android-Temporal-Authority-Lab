from lab.authority_fixedpoint import Probe
from lab.trap_certificate import *

def test_trap_certificate_two_world():
    d=("deny","allow")
    ps=[Probe("blocked",("0","1"),(False,True))]
    C=frozenset({0,1}); w=trap_witness(C,d,ps)
    assert w=={}
    assert verify_trap(C,w,d,ps)

def test_branching_deadlock_selects_bad_successor():
    d=("deny","allow","deny")
    ps=[Probe("split",("L","R","R"),(True,True,True)),
        Probe("blocked",("x","0","1"),(True,False,True))]
    C=frozenset({0,1,2});w=trap_witness(C,d,ps)
    assert w is not None and verify_trap(C,w,d,ps)

def test_resolvable_has_no_trap():
    d=("deny","allow")
    ps=[Probe("safe",("0","1"),(True,True))]
    assert trap_witness(frozenset({0,1}),d,ps) is None
