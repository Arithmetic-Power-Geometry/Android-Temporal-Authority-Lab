from lab.sequence_gap import *
def test_local_suite_can_miss_sequence_gap():
    m=Model(False,False)
    assert conventional_local_suite(m)
    assert not sequence_suite(m)
    assert run(m)["sequence_gap"]
def test_revocation_closes_gap():
    m=Model(True,False)
    assert conventional_local_suite(m) and sequence_suite(m)
def test_use_time_recheck_closes_gap():
    m=Model(False,True)
    assert conventional_local_suite(m) and sequence_suite(m)
