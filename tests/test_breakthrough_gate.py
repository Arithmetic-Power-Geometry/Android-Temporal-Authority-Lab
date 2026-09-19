from lab.breakthrough_gate import *
def test_current_work_cannot_self_promote():
    assert verdict(CURRENT)=="NO_BREAKTHROUGH_CONTINUE"
def test_ci_alone_never_equals_breakthrough():
    e=Evidence(exact_theorem=True,exhaustive_small_models=True)
    assert verdict(e)=="NO_BREAKTHROUGH_CONTINUE"
def test_stop_requires_replication():
    e=Evidence(True,True,True,True,False,True)
    assert verdict(e)=="BREAKTHROUGH_CANDIDATE_STOP_AND_WRITE"
