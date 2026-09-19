from lab.antichain_solver import *
from lab.authority_fixedpoint import root_resolvable as fp_root, Probe as FP

def cv(p): return FP(p.name,p.outcomes,p.admissible)

def test_matches_fixedpoint_examples():
    d=("deny","allow","deny","allow")
    ps=[Probe("root",("L","L","R","R"),(1,1,1,1)),
        Probe("left",("0","1","x","x"),(1,1,0,0)),
        Probe("right",("x","x","0","1"),(0,0,1,1))]
    assert root_resolvable(d,ps)==fp_root(d,[cv(p) for p in ps])
    assert downward_closure_check(d,ps)

def test_deadlock_case_matches():
    d=("deny","allow")
    ps=[Probe("x",("0","1"),(0,1))]
    assert not root_resolvable(d,ps)
    assert root_resolvable(d,ps)==fp_root(d,[cv(p) for p in ps])
