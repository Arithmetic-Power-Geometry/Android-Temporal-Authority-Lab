from lab.authority_fixedpoint import *

def test_deadlock_is_fixedpoint_property():
    d=("deny","allow")
    p=Probe("forbidden-in-deny",("0","1"),(False,True))
    assert not root_resolvable(d,[p])
    assert frozenset({0,1}) in authority_deadlock_kernel(d,[p])

def test_safe_probe_removes_root_from_deadlock_kernel():
    d=("deny","allow")
    p=Probe("public",("0","1"),(True,True))
    assert root_resolvable(d,[p])
    assert frozenset({0,1}) not in authority_deadlock_kernel(d,[p])

def test_branch_relative_admissibility():
    d=("deny","allow","deny","allow")
    root=Probe("root",("L","L","R","R"),(True,True,True,True))
    left=Probe("left",("0","1","x","x"),(True,True,False,False))
    right=Probe("right",("x","x","0","1"),(False,False,True,True))
    assert root_resolvable(d,[root,left,right])
