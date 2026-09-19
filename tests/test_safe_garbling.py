from lab.safe_garbling import *

def test_coverage_restores_safe_simulation_condition():
    a=Exp(("0","1","2"),(True,True,True))
    b=Exp(("x","x","y"),(True,True,True))
    assert safe_garbling_restored(a,b)

def test_missing_authority_breaks_source_then_garble_argument():
    a=Exp(("0","1","2"),(True,False,True))
    b=Exp(("x","x","y"),(True,True,True))
    assert refines(a,b)
    assert not safe_garbling_restored(a,b)
    assert witness_failure(a,b)["world"]==1
