from lab.novelty_gate import ClaimAudit, gate, can_call_breakthrough

def test_incomplete_claim_is_unresolved():
    a = ClaimAudit(True, True, True, True, False, True, True, True)
    assert gate(a) == "UNRESOLVED"

def test_full_audit_only_survives_current_tests():
    a = ClaimAudit(True, True, True, True, True, True, True, True)
    assert gate(a) == "SURVIVES_CURRENT_TESTS"

def test_breakthrough_requires_proof_and_empirical_support():
    assert not can_call_breakthrough(["SURVIVES_CURRENT_TESTS"])
    assert not can_call_breakthrough(["THEOREM_PROVED"])
    assert can_call_breakthrough(["THEOREM_PROVED", "EMPIRICALLY_SUPPORTED"])
