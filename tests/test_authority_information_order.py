from lab.authority_information_order import *

def test_more_raw_information_can_be_worse_for_authorization():
    # A reveals every relevant distinction but is forbidden in one live world.
    a=Experiment("strong",("0","1"),(False,True))
    # B is admissible everywhere and still separates the required decisions.
    b=Experiment("weak",("x","y"),(True,True))
    d=("deny","allow")
    assert refines(a,b) and refines(b,a)  # equal raw partition here
    assert authority_information_reversal(a,b,d)

def test_strict_raw_refinement_can_reverse():
    # decisions 0 and 1 agree; 2 differs. Strong distinguishes all three,
    # weak merges 0/1 but still resolves the decision.
    a=Experiment("strong",("a","b","c"),(True,False,True))
    b=Experiment("weak",("x","x","y"),(True,True,True))
    d=("deny","deny","allow")
    assert refines(a,b) and not refines(b,a)
    assert authority_information_reversal(a,b,d)

def test_search_finds_reversals():
    assert enumerate_reversals(3)
