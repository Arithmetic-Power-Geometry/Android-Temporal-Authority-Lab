from lab.semantics_oracle import *
from lab.contracts import CONTRACTS

def test_expected_persistable_uri_not_false_positive():
    c=CONTRACTS["persistable_uri_until_explicit_revoke"]
    o=Observation(True,False,True,True)
    assert differential(o)
    assert classify(c,o)=="DOCUMENTED_OR_EXPECTED"

def test_documented_stop_mismatch_is_candidate_only():
    c=CONTRACTS["private_profile_execution_while_locked"]
    o=Observation(True,False,True,True)
    assert classify(c,o)=="SEMANTIC_MISMATCH_CANDIDATE"

def test_no_sensitive_effect_is_not_promoted():
    c=CONTRACTS["temporary_uri_activity_lifetime"]
    o=Observation(True,False,True,False)
    assert classify(c,o)=="INCONCLUSIVE"
