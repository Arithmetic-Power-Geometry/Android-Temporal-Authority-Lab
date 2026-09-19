from lab.evaluate import Observation, classify

def test_secure_case():
    o = Observation("TAC-001", "denied", "denied", False)
    assert classify(o) == "INVARIANT_HOLDS_FOR_OBSERVATION"

def test_candidate_gap():
    o = Observation("TAC-001", "denied", "succeeded", True)
    assert classify(o) == "CANDIDATE_TEMPORAL_AUTHORITY_GAP"

def test_non_synthetic_invalid():
    o = Observation("TAC-001", "denied", "succeeded", True, synthetic_only=False)
    assert classify(o) == "INVALID_TEST"
